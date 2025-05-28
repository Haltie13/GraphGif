"""
Expression types for GraphGif AST.
This module contains list and collection types like NodeList, EdgeList, AttrList.
"""

from dataclasses import dataclass
from typing import List, Optional, Union
from .values import ASTNode, Attribute, AttributeOperator, EdgeOperator, AttrVarRef


@dataclass
class NodeList(ASTNode):
    """List of node IDs."""
    nodes: List[str]


@dataclass
class AttrList(ASTNode):
    """List of attributes [attr1=val1, attr2=val2, ...]."""
    attributes: List[Attribute]


@dataclass
class EdgeDecl(ASTNode):
    """Edge declaration: nodeA -> nodeB [attributes]."""
    source: str
    operator: EdgeOperator
    target: str
    attributes: Optional[Union[AttrList, AttrVarRef]] = None


@dataclass
class EdgeList(ASTNode):
    """List of edge declarations."""
    edges: List[EdgeDecl]


# Import VarRef classes
from .values import NodeVarRef, EdgeVarRef, AttrVarRef

# Node expressions for variable values
NodeExpression = Union[NodeList, NodeVarRef]
EdgeExpression = Union[EdgeList, EdgeVarRef] 
AttributeExpression = Union[AttrList, AttrVarRef]

# Variable values union type
VarValue = Union[NodeVarRef, EdgeVarRef, AttrVarRef, NodeList, EdgeList, AttrList]
