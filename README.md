# GraphGif
Translator of a custom graph describing language into graphviz animation.
# Student data
- Jakub Mikołajczyk jmikolaj@student.agh.edu.pl
- Maciej Maj maciejmaj@student.agh.edu.pl
- Kamil Mróz kamroz@student.agh.edu.pl
# Introduction
This project is an interpreter for a custom graph-oriented language that translates user-defined graph structures and algorithm commands into animations using Graphviz.
The language allows for the definition of graphs, nodes, edges, as well as variables for reuse. You can also customize attributes such as colors and shapes.
Once graphs and variables are defined, users can apply algorithms like Breadth-First Search and export the resulting animation.
# Project goals
The goal of this project is to:
- Create an interpreter that enables building and configuring graphs through a custom domain-specific language,
- Implement commands that execute algorithms on these graphs. For example BFS,
 - Generate animated visualizations using Graphviz based on the defined graph structure and the chosen algorithm.
# Program assumptions
- #### Type of translator:
  Interpreter
- #### Planned result:
  Loading a file with code in a graph language → interpretation → generating a .dot file and a file with an animation presenting the subsequent steps of the algorithm.
- #### Planned implementation language:
  Python
- #### Scanner/ Parser implementation:
  [to be completed]
# Token definitions
[to be completed]
# Grammar
##### PROGRAM STRUCTURE
program       ::= { var_decl ";" } { graph_decl ";" } { command ";" }

##### VARIABLE DECLARATIONS 
var_decl      ::= "var" identifier "=" var_value
var_value     ::= node_decl
                | edge_decl
                | literal_attr_list
                | node_group
                | edge_group

node_group    ::= "nodes" "(" [node_decl { "," node_decl }] ")"
edge_group    ::= "edges" "(" [edge_decl { "," edge_decl }] ")"

##### GRAPH DEFINITION 
graph_decl    ::= graph_head "{" { global_attr_decl ";" } { statement ";" } "}"
graph_head    ::= [ "graph" ] identifier

##### GLOBAL ATTRIBUTES 
global_attr_decl ::= ("graph" | "node" | "edge") ( literal_attr_list | var_ref )

##### LOCAL DECLARATIONS 
statement     ::= node_decl | edge_decl | var_ref

##### NODE DECLARATION 
node_decl     ::= node_id [ ( literal_attr_list | var_ref ) ]
node_id       ::= identifier | node_list
node_list     ::= "(" identifier { "," identifier } ")"

##### EDGE DECLARATION 
edge_decl     ::= node_id edge_op node_id [ ( literal_attr_list | var_ref ) ]
edge_op       ::= "--" | "->" | "<-"

##### ATTRIBUTES LIST 
literal_attr_list ::= "[" [ attribute { "," attribute } [ "," ] ] "]"
attribute     ::= identifier ( "=" | ":" ) value
value         ::= identifier | number | string

##### VARIABLE REFERENCE 
var_ref       ::= "$" identifier

##### COMMANDS 
command       ::= identifier "(" [ arg_list ] ")"
arg_list      ::= argument { "," argument }
argument      ::= [ identifier ":" ] ( path | var_ref )
path          ::= identifier { "." identifier }

##### LEXICAL ELEMENTS 
identifier    ::= letter { letter | digit | "_" }
number        ::= digit { digit } [ "." digit { digit } ]
string        ::= "'" { char } "'" | "\"" { char } "\""
letter        ::= "A" | "B" | ... | "Z" | "a" | "b" | ... | "z"
digit         ::= "0" | "1" | ... | "9"
char          ::= any_character_except_the_terminating_quote
# Scanner/Parser Tools
[to be completed]
# External Libraries / Packages
We may ues Graphviz and libraries for code visuaization
# Usage Instructions
- Write the graph you need to visualize using custom language syntax,
- Run the interpreter with your file as input,
- The interpreter prses and processes graph declarations and commands,
- Graph animations are generated in Graphviz format.
# Example Usage
// Deklaracja grafu  
graph MyGraph {  
    graph $graph_attrs;  
    node $node_attrs;   
    edge $edge_attrs;  
  
  // Lokalne deklaracje  
  F [shape="diamond"];  
  G [label="End", color="darkred"];  
    
  $my_nodes;  
  $important_edges;
    
  D -> E;  
  E -> F [arrowhead="vee"];  
  F -- G;  
}
  
// Inny graf z krótszą składnią  
Network {  
  node [shape="box"];
    
  (Server1, Server2, Client1, Client2);  
  Server1 -- Server2 [weight=5];  
  Client1 -> Server1;  
  Client2 -> Server1;  
  }
