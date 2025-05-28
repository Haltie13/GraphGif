"""
Factory classes for creating AST nodes.
This module provides factory methods for convenient AST node creation.
"""

from typing import List, Optional, Union
from .values import Value, Attribute, AttributeOperator, EdgeOperator
from .expressions import EdgeDecl, AttrList, AttrVarRef
from .statements import Statement
from .ast_nodes import VarDecl, VarType, GraphDecl, GraphDirection, GlobalAttrDecl, VarValue


class ASTFactory:
    """Factory class for creating AST nodes."""
    
    @staticmethod
    def create_value(value: Union[str, int], value_type: str) -> Value:
        """Create a Value node."""
        return Value(value, value_type)
    
    @staticmethod
    def create_attribute(key: str, operator: str, value: Value) -> Attribute:
        """Create an Attribute node."""
        op = AttributeOperator.EQUALS if operator == "=" else AttributeOperator.COLON
        return Attribute(key, op, value)
    
    @staticmethod
    def create_edge_decl(source: str, operator: str, target: str, 
                        attributes: Optional[Union[AttrList, AttrVarRef]] = None) -> EdgeDecl:
        """Create an EdgeDecl node."""
        edge_op = {
            "--": EdgeOperator.UNDIRECTED,
            "->": EdgeOperator.DIRECTED_RIGHT,
            "<-": EdgeOperator.DIRECTED_LEFT
        }[operator]
        return EdgeDecl(source, edge_op, target, attributes)
    
    @staticmethod
    def create_graph_decl(direction: str, name: str, 
                         global_attributes: List[GlobalAttrDecl],
                         statements: List[Statement]) -> GraphDecl:
        """Create a GraphDecl node."""
        graph_dir = GraphDirection.DIRECTED if direction == "directed" else GraphDirection.UNDIRECTED
        return GraphDecl(graph_dir, name, global_attributes, statements)
    
    @staticmethod
    def create_var_decl(var_type: str, name: str, value: VarValue) -> VarDecl:
        """Create a VarDecl node."""
        vtype = {
            "node": VarType.NODE,
            "edge": VarType.EDGE,
            "attributes": VarType.ATTRIBUTES
        }[var_type]
        return VarDecl(vtype, name, value)
