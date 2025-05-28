grammar Graphgif;

// Main program structure with typed variables support
program: (varDecl ';')* (graphDecl ';')* (command ';')* EOF;

// Variable declarations with explicit typing
varDecl: 'var' varType ID '=' varValue;
varType: 'node' | 'edge' | 'attributes';
varValue:
	nodeVarRef
	| edgeVarRef
	| attrVarRef
	| nodeList
	| edgeList
	| attrList;

// Graph declaration
graphDecl: ('directed' | 'undirected') ('graph') ID '{' (
		globalAttrDecl ';'
	)* (statement ';')* '}';
globalAttrDecl: ('graph' | 'node' | 'edge') (
		attrList
		| attrVarRef
	);
statement: nodeDecl | edgeDecl;

// Node and edge declarations
nodeDecl: (nodeList | nodeVarRef) (attrList | attrVarRef)?;
edgeDecl: ID edgeOp ID (attrList | attrVarRef)?;
edgeOp: '--' | '->' | '<-';

// Lists and literals
nodeList: ID (',' ID)*;
edgeList: edgeDecl (',' edgeDecl)*;
attrList: '[' (attribute (',' attribute)* ','?)? ']';
attribute: ID ('=' | ':') value;
value: ID | NUMBER | STRING;

nodeVarRef: '$' ID;
edgeVarRef: '$' ID;
attrVarRef: '$' ID;

// Commands
command: 'run' ID 'with' '(' argList? ')';
argList: argument (',' argument)*;
argument: ID ('=' | ':') (path | value);
path: ID ('.' ID)*;

// Lexical rules
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
STRING: '\'' (~[\r\n'\\] | '\\' .)* '\'';
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
COMMENT_LINE: '//' ~[\r\n]* -> skip;