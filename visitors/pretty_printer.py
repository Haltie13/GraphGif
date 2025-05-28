"""
Pretty printer for GraphGif AST.
This module provides a visitor that converts AST back to readable GraphGif code.
"""

from .base_visitor import BaseASTVisitor
from models import (
    Program, VarDecl, GraphDecl, NodeDecl, EdgeDecl, Command,
    AttrList, NodeList, EdgeList, Path, Value
)


class GraphgifPrettyPrinter(BaseASTVisitor):
    """A visitor that pretty-prints the AST back to Graphgif source code."""
    
    def __init__(self):
        self.output = []
        self.indent_level = 0
    
    def indent(self) -> str:
        return "  " * self.indent_level
    
    def visit_program(self, node: Program) -> None:
        """Visit a Program node and print variable declarations, graphs, and commands."""
        self.output = []
        
        if node.variable_declarations:
            self.output.append("Variable Declarations:\n")
            self.indent_level += 1
            for var_decl in node.variable_declarations:
                self.visit_var_decl(var_decl)
            self.indent_level -= 1
            self.output.append("\n")
        
        if node.graph_declarations:
            self.output.append("Graph Declarations:\n")
            self.indent_level += 1
            for graph_decl in node.graph_declarations:
                self.visit_graph_decl(graph_decl)
            self.indent_level -= 1
            self.output.append("\n")
        
        if node.commands:
            self.output.append("Commands:\n")
            self.indent_level += 1
            for command in node.commands:
                self.visit_command(command)
            self.indent_level -= 1
    
    def visit_var_decl(self, node: VarDecl) -> None:
        self.output.append(f"{self.indent()}{node.var_type.value} {node.name} = ")
        if isinstance(node.value, NodeList):
            self.output.append(f"[{', '.join(node.value.nodes)}]\n")
        elif isinstance(node.value, AttrList):
            self.visit_attr_list(node.value)
            self.output.append("\n")
        elif isinstance(node.value, EdgeList):
            self.output.append("edge_list\n")
        else:
            self.output.append(f"${node.value.name}\n")
    
    def visit_graph_decl(self, node: GraphDecl) -> None:
        self.output.append(f"{self.indent()}{node.direction.value} graph {node.name} {{\n")
        self.indent_level += 1
        
        for global_attr in node.global_attributes:
            self.output.append(f"{self.indent()}{global_attr.attr_type.value} ")
            if isinstance(global_attr.attributes, AttrList):
                self.visit_attr_list(global_attr.attributes)
            else:
                self.output.append(f"${global_attr.attributes.name}")
            self.output.append("\n")
        
        for statement in node.statements:
            if isinstance(statement, NodeDecl):
                self.visit_node_decl(statement)
            elif isinstance(statement, EdgeDecl):
                self.visit_edge_decl(statement)
        
        self.indent_level -= 1
        self.output.append(f"{self.indent()}}}\n")
    
    def visit_node_decl(self, node: NodeDecl) -> None:
        self.output.append(f"{self.indent()}")
        if isinstance(node.nodes, NodeList):
            self.output.append(f"{', '.join(node.nodes.nodes)}")
        else:
            self.output.append(f"${node.nodes.name}")
        
        if node.attributes:
            self.output.append(" ")
            if isinstance(node.attributes, AttrList):
                self.visit_attr_list(node.attributes)
            else:
                self.output.append(f"${node.attributes.name}")
        self.output.append("\n")
    
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        self.output.append(f"{self.indent()}{node.source} {node.operator.value} {node.target}")
        if node.attributes:
            self.output.append(" ")
            if isinstance(node.attributes, AttrList):
                self.visit_attr_list(node.attributes)
            else:
                self.output.append(f"${node.attributes.name}")
        self.output.append("\n")
    
    def visit_command(self, node: Command) -> None:
        self.output.append(f"{self.indent()}run {node.graph_name} with (")
        for i, arg in enumerate(node.arguments):
            if i > 0:
                self.output.append(", ")
            
            # Handle both path and value arguments
            if isinstance(arg.argument_value, Path):
                value_str = '.'.join(arg.argument_value.components)
            elif isinstance(arg.argument_value, Value):
                if arg.argument_value.value_type == "STRING":
                    value_str = f'"{arg.argument_value.value}"'
                else:
                    value_str = str(arg.argument_value.value)
            else:
                value_str = str(arg.argument_value)
            
            self.output.append(f"{arg.name}{arg.operator.value}{value_str}")
        self.output.append(")\n")
    
    def visit_attr_list(self, node: AttrList) -> None:
        self.output.append("[")
        for i, attr in enumerate(node.attributes):
            if i > 0:
                self.output.append(", ")
            value_str = f'"{attr.value.value}"' if attr.value.value_type == "STRING" else str(attr.value.value)
            self.output.append(f"{attr.key}{attr.operator.value}{value_str}")
        self.output.append("]")
    
    def visit_node_list(self, node: NodeList) -> None:
        pass  # Handled in parent methods
    
    def get_output(self) -> str:
        """Get the generated output as a string."""
        return "".join(self.output)
