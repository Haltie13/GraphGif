"""
Statistics visitor for GraphGif AST.
This module provides a visitor that collects statistics about the graph structure.
"""

from .base_visitor import BaseASTVisitor
from models import (
    Program, VarDecl, GraphDecl, NodeDecl, EdgeDecl, Command,
    AttrList, NodeList, EdgeList
)


class GraphStatisticsVisitor(BaseASTVisitor):
    """A visitor that collects statistics about the graph structure."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset all statistics counters."""
        self.node_count = 0
        self.edge_count = 0
        self.graph_count = 0
        self.variable_count = 0
        self.command_count = 0
        self.nodes = set()
        self.edges = []
    
    def visit_program(self, node: Program) -> None:
        """Visit program and reset statistics."""
        self.reset()
        super().visit_program(node)
    
    def visit_var_decl(self, node: VarDecl) -> None:
        """Count variable declarations."""
        self.variable_count += 1
        super().visit_var_decl(node)
    
    def visit_graph_decl(self, node: GraphDecl) -> None:
        """Count graph declarations."""
        self.graph_count += 1
        super().visit_graph_decl(node)
    
    def visit_node_decl(self, node: NodeDecl) -> None:
        """Count node declarations and collect node names."""
        if isinstance(node.nodes, NodeList):
            self.nodes.update(node.nodes.nodes)
        super().visit_node_decl(node)
    
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        """Count edge declarations and collect edge information."""
        self.edge_count += 1
        self.edges.append((node.source, node.target))
        self.nodes.add(node.source)
        self.nodes.add(node.target)
        super().visit_edge_decl(node)
    
    def visit_command(self, node: Command) -> None:
        """Count commands."""
        self.command_count += 1
        super().visit_command(node)
    
    def visit_node_list(self, node: NodeList) -> None:
        """Collect nodes from node lists."""
        self.nodes.update(node.nodes)
    
    def get_statistics(self) -> dict:
        """Get collected statistics as a dictionary."""
        return {
            "total_nodes": len(self.nodes),
            "total_edges": self.edge_count,
            "total_graphs": self.graph_count,
            "total_variables": self.variable_count,
            "total_commands": self.command_count,
            "node_list": sorted(list(self.nodes)),
            "edge_list": self.edges
        }
