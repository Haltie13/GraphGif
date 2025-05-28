"""
Main AST node types for GraphGif.
This module contains the primary AST nodes like Program, VarDecl, GraphDecl.
"""

from dataclasses import dataclass
from typing import List, Union
from .values import ASTNode, VarType, GraphDirection, GlobalAttrType
from .expressions import VarValue, AttributeExpression
from .statements import Statement, Command


@dataclass
class VarDecl(ASTNode):
    """Variable declaration: var type name = value."""
    var_type: VarType
    name: str
    value: VarValue


@dataclass
class GlobalAttrDecl(ASTNode):
    """Global attribute declaration for graph, node, or edge."""
    attr_type: GlobalAttrType
    attributes: AttributeExpression


@dataclass
class GraphDecl(ASTNode):
    """Graph declaration with direction, name, global attributes, and statements."""
    direction: GraphDirection
    name: str
    global_attributes: List[GlobalAttrDecl]
    statements: List[Statement]


@dataclass
class Program(ASTNode):
    """Root program containing variable declarations, graph declarations, and commands."""
    variable_declarations: List[VarDecl]
    graph_declarations: List[GraphDecl]
    commands: List[Command]
