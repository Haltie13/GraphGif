"""
Parser helper for building AST from ANTLR parse tree.
This module provides utilities to convert ANTLR parse trees to our structured AST model.
"""

import sys
import os

# Add current directory and parent directory to path
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, current_dir)

from antlr4 import *
from .grammar.GraphgifLexer import GraphgifLexer
from .grammar.GraphgifParser import GraphgifParser
from .grammar.GraphgifListener import GraphgifListener

from models import *


class ASTBuilder(GraphgifListener):
    """ANTLR listener that builds our AST model from the parse tree."""
    
    def __init__(self):
        self.ast_stack = []
        self.program = None
    
    def enterProgram(self, ctx: GraphgifParser.ProgramContext):
        """Enter program rule."""
        self.variable_declarations = []
        self.graph_declarations = []
        self.commands = []
    
    def exitProgram(self, ctx: GraphgifParser.ProgramContext):
        """Exit program rule and create Program AST node."""
        self.program = Program(
            self.variable_declarations,
            self.graph_declarations,
            self.commands
        )
    
    def exitVarDecl(self, ctx: GraphgifParser.VarDeclContext):
        """Exit variable declaration and create VarDecl AST node."""
        var_type = ctx.varType().getText()
        name = ctx.ID().getText()
        
        # Get the variable value from the stack
        var_value = self.ast_stack.pop()
        
        var_decl = ASTFactory.create_var_decl(var_type, name, var_value)
        self.variable_declarations.append(var_decl)
    
    def exitVarValue(self, ctx: GraphgifParser.VarValueContext):
        """Exit variable value and push appropriate value to stack."""
        if ctx.nodeList():
            # Node list already on stack
            pass
        elif ctx.edgeList():
            # Edge list already on stack
            pass
        elif ctx.attrList():
            # Attribute list already on stack
            pass
        elif ctx.nodeVarRef():
            name = ctx.nodeVarRef().ID().getText()
            self.ast_stack.append(NodeVarRef(name))
        elif ctx.edgeVarRef():
            name = ctx.edgeVarRef().ID().getText()
            self.ast_stack.append(EdgeVarRef(name))
        elif ctx.attrVarRef():
            name = ctx.attrVarRef().ID().getText()
            self.ast_stack.append(AttrVarRef(name))
    
    def exitGraphDecl(self, ctx: GraphgifParser.GraphDeclContext):
        """Exit graph declaration and create GraphDecl AST node."""
        direction = ctx.getChild(0).getText()  # 'directed' or 'undirected'
        name = ctx.ID().getText()
        
        # Collect global attributes and statements from stack
        statements = []
        global_attributes = []
        
        # Process statements and global attributes
        for _ in range(len(ctx.statement())):
            statements.insert(0, self.ast_stack.pop())
        
        for _ in range(len(ctx.globalAttrDecl())):
            global_attributes.insert(0, self.ast_stack.pop())
        
        graph_decl = ASTFactory.create_graph_decl(direction, name, global_attributes, statements)
        self.graph_declarations.append(graph_decl)
    
    def exitGlobalAttrDecl(self, ctx: GraphgifParser.GlobalAttrDeclContext):
        """Exit global attribute declaration."""
        attr_type_str = ctx.getChild(0).getText()
        attr_type = {
            "graph": GlobalAttrType.GRAPH,
            "node": GlobalAttrType.NODE,
            "edge": GlobalAttrType.EDGE
        }[attr_type_str]
        
        # Get attributes from stack (either AttrList or AttrVarRef)
        attributes = self.ast_stack.pop()
        
        global_attr = GlobalAttrDecl(attr_type, attributes)
        self.ast_stack.append(global_attr)
    
    def exitNodeDecl(self, ctx: GraphgifParser.NodeDeclContext):
        """Exit node declaration."""
        attributes = None
        if ctx.attrList() or ctx.attrVarRef():
            attributes = self.ast_stack.pop()
        
        # Get nodes (NodeList or NodeVarRef)
        nodes = self.ast_stack.pop()
        
        node_decl = NodeDecl(nodes, attributes)
        self.ast_stack.append(node_decl)
    
    def exitEdgeDecl(self, ctx: GraphgifParser.EdgeDeclContext):
        """Exit edge declaration."""
        source = ctx.ID(0).getText()
        target = ctx.ID(1).getText()
        operator = ctx.edgeOp().getText()
        
        attributes = None
        if ctx.attrList() or ctx.attrVarRef():
            attributes = self.ast_stack.pop()
        
        edge_decl = ASTFactory.create_edge_decl(source, operator, target, attributes)
        self.ast_stack.append(edge_decl)
    
    def exitNodeList(self, ctx: GraphgifParser.NodeListContext):
        """Exit node list."""
        nodes = [id_node.getText() for id_node in ctx.ID()]
        node_list = NodeList(nodes)
        self.ast_stack.append(node_list)
    
    def exitEdgeList(self, ctx: GraphgifParser.EdgeListContext):
        """Exit edge list."""
        # Collect edge declarations from stack
        edges = []
        for _ in range(len(ctx.edgeDecl())):
            edges.insert(0, self.ast_stack.pop())
        
        edge_list = EdgeList(edges)
        self.ast_stack.append(edge_list)
    
    def exitAttrList(self, ctx: GraphgifParser.AttrListContext):
        """Exit attribute list."""
        # Collect attributes from stack
        attributes = []
        for _ in range(len(ctx.attribute())):
            attributes.insert(0, self.ast_stack.pop())
        
        attr_list = AttrList(attributes)
        self.ast_stack.append(attr_list)
    
    def exitAttribute(self, ctx: GraphgifParser.AttributeContext):
        """Exit attribute."""
        key = ctx.ID().getText()
        operator = ctx.getChild(1).getText()  # '=' or ':'
        
        # Get value from stack
        value = self.ast_stack.pop()
        
        attribute = ASTFactory.create_attribute(key, operator, value)
        self.ast_stack.append(attribute)
    
    def exitValue(self, ctx: GraphgifParser.ValueContext):
        """Exit value."""
        if ctx.ID():
            value = ASTFactory.create_value(ctx.ID().getText(), "ID")
        elif ctx.NUMBER():
            value = ASTFactory.create_value(int(ctx.NUMBER().getText()), "NUMBER")
        elif ctx.STRING():
            # Remove quotes from string
            string_text = ctx.STRING().getText()[1:-1]  # Remove surrounding quotes
            value = ASTFactory.create_value(string_text, "STRING")
        
        self.ast_stack.append(value)
    
    def exitCommand(self, ctx: GraphgifParser.CommandContext):
        """Exit command."""
        graph_name = ctx.ID().getText()
        
        # Collect arguments from stack
        arguments = []
        if ctx.argList():
            for _ in range(len(ctx.argList().argument())):
                arguments.insert(0, self.ast_stack.pop())
        
        command = Command(graph_name, arguments)
        self.commands.append(command)
    
    def exitArgument(self, ctx: GraphgifParser.ArgumentContext):
        """Exit argument."""
        name = ctx.ID().getText()
        operator_text = ctx.getChild(1).getText()
        operator = AttributeOperator.EQUALS if operator_text == "=" else AttributeOperator.COLON
        
        # Get path from stack
        path = self.ast_stack.pop()
        
        argument = Argument(name, operator, path)
        self.ast_stack.append(argument)
    
    def exitPath(self, ctx: GraphgifParser.PathContext):
        """Exit path."""
        components = [id_node.getText() for id_node in ctx.ID()]
        path = Path(components)
        self.ast_stack.append(path)


def parse_graphgif(input_text: str) -> Program:
    """Parse Graphgif source code and return AST."""
    
    # Create input stream
    input_stream = InputStream(input_text)
    
    # Create lexer
    lexer = GraphgifLexer(input_stream)
    
    # Create token stream
    token_stream = CommonTokenStream(lexer)
    
    # Create parser
    parser = GraphgifParser(token_stream)
    
    # Parse starting from program rule
    tree = parser.program()
    
    # Create AST builder and walk the tree
    ast_builder = ASTBuilder()
    walker = ParseTreeWalker()
    walker.walk(ast_builder, tree)
    
    return ast_builder.program


def parse_graphgif_file(file_path: str) -> Program:
    """Parse Graphgif file and return AST."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return parse_graphgif(content)


# Example usage and testing
def test_parser():
    """Test the parser with example Graphgif code."""
    
    test_code = """
    var node myNodes = A, B, C;
    var attributes defaultAttrs = [color='red', size=10];
    
    directed graph testGraph {
        node [shape='circle'];
        A, B, C [color='blue'];
        A -> B [weight=5];
        B -> C;
    }
    
    run testGraph with (output='result.png');
    """
    
    try:
        # Parse the code
        ast = parse_graphgif(test_code)
        
        # Pretty print the result
        from visitors import GraphgifPrettyPrinter, GraphStatisticsVisitor
        
        printer = GraphgifPrettyPrinter()
        printer.visit_program(ast)
        print("Parsed AST:")
        print("=" * 50)
        print(printer.get_output())
        
        # Show statistics
        stats_visitor = GraphStatisticsVisitor()
        stats_visitor.visit_program(ast)
        stats = stats_visitor.get_statistics()
        
        print("\nStatistics:")
        print("=" * 50)
        for key, value in stats.items():
            print(f"{key}: {value}")
            
        return ast
        
    except Exception as e:
        print(f"Error parsing code: {e}")
        return None


if __name__ == "__main__":
    test_parser()
