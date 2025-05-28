"""
Base visitor classes for GraphGif AST traversal.
This module provides the visitor pattern implementation for AST traversal.
"""

from abc import ABC, abstractmethod
from models import (
    Program, VarDecl, GraphDecl, NodeDecl, EdgeDecl, Command,
    AttrList, NodeList, EdgeList
)


class ASTVisitor(ABC):
    """Abstract visitor for traversing the AST."""
    
    @abstractmethod
    def visit_program(self, node: Program) -> None:
        """Visit a Program node."""
        pass
    
    @abstractmethod
    def visit_var_decl(self, node: VarDecl) -> None:
        """Visit a VarDecl node."""
        pass
    
    @abstractmethod
    def visit_graph_decl(self, node: GraphDecl) -> None:
        """Visit a GraphDecl node."""
        pass
    
    @abstractmethod
    def visit_node_decl(self, node: NodeDecl) -> None:
        """Visit a NodeDecl node."""
        pass
    
    @abstractmethod
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        """Visit an EdgeDecl node."""
        pass
    
    @abstractmethod
    def visit_command(self, node: Command) -> None:
        """Visit a Command node."""
        pass
    
    @abstractmethod
    def visit_attr_list(self, node: AttrList) -> None:
        """Visit an AttrList node."""
        pass
    
    @abstractmethod
    def visit_node_list(self, node: NodeList) -> None:
        """Visit a NodeList node."""
        pass


class BaseASTVisitor(ASTVisitor):
    """Base implementation of AST visitor with default traversal behavior."""
    
    def visit_program(self, node: Program) -> None:
        """Visit a Program node and traverse its children."""
        for var_decl in node.variable_declarations:
            self.visit_var_decl(var_decl)
        for graph_decl in node.graph_declarations:
            self.visit_graph_decl(graph_decl)
        for command in node.commands:
            self.visit_command(command)
    
    def visit_var_decl(self, node: VarDecl) -> None:
        """Visit a VarDecl node."""
        if isinstance(node.value, NodeList):
            self.visit_node_list(node.value)
        elif isinstance(node.value, AttrList):
            self.visit_attr_list(node.value)
        elif isinstance(node.value, EdgeList):
            for edge in node.value.edges:
                self.visit_edge_decl(edge)
    
    def visit_graph_decl(self, node: GraphDecl) -> None:
        """Visit a GraphDecl node and traverse its children."""
        for global_attr in node.global_attributes:
            if isinstance(global_attr.attributes, AttrList):
                self.visit_attr_list(global_attr.attributes)
        for statement in node.statements:
            if isinstance(statement, NodeDecl):
                self.visit_node_decl(statement)
            elif isinstance(statement, EdgeDecl):
                self.visit_edge_decl(statement)
    
    def visit_node_decl(self, node: NodeDecl) -> None:
        """Visit a NodeDecl node."""
        if isinstance(node.nodes, NodeList):
            self.visit_node_list(node.nodes)
        if isinstance(node.attributes, AttrList):
            self.visit_attr_list(node.attributes)
    
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        """Visit an EdgeDecl node."""
        if isinstance(node.attributes, AttrList):
            self.visit_attr_list(node.attributes)
    
    def visit_command(self, node: Command) -> None:
        """Visit a Command node."""
        pass
    
    def visit_attr_list(self, node: AttrList) -> None:
        """Visit an AttrList node."""
        pass
    
    def visit_node_list(self, node: NodeList) -> None:
        """Visit a NodeList node."""
        pass
