"""
Value types and enums for GraphGif AST.
This module contains basic value types, operators, and enums.
"""

from abc import ABC
from dataclasses import dataclass
from typing import Union
from enum import Enum


class GraphDirection(Enum):
    """Graph direction types."""
    DIRECTED = "directed"
    UNDIRECTED = "undirected"


class VarType(Enum):
    """Variable types in Graphgif."""
    NODE = "node"
    EDGE = "edge"
    ATTRIBUTES = "attributes"


class EdgeOperator(Enum):
    """Edge operator types."""
    UNDIRECTED = "--"
    DIRECTED_RIGHT = "->"
    DIRECTED_LEFT = "<-"


class GlobalAttrType(Enum):
    """Global attribute declaration types."""
    GRAPH = "graph"
    NODE = "node"
    EDGE = "edge"


class AttributeOperator(Enum):
    """Attribute assignment operators."""
    EQUALS = "="
    COLON = ":"


# Base classes
@dataclass
class ASTNode(ABC):
    """Base class for all AST nodes."""
    pass


@dataclass
class Value(ASTNode):
    """Represents a value (ID, NUMBER, or STRING)."""
    value: Union[str, int]
    value_type: str  # 'ID', 'NUMBER', or 'STRING'


@dataclass
class VarRef(ASTNode):
    """Base class for variable references."""
    name: str


@dataclass
class NodeVarRef(VarRef):
    """Reference to a node variable ($ID)."""
    pass


@dataclass
class EdgeVarRef(VarRef):
    """Reference to an edge variable ($ID)."""
    pass


@dataclass
class AttrVarRef(VarRef):
    """Reference to an attributes variable ($ID)."""
    pass


@dataclass
class Attribute(ASTNode):
    """Single attribute with key-value pair."""
    key: str
    operator: AttributeOperator
    value: Value
