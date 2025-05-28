"""
Statement and command types for GraphGif AST.
This module contains commands, arguments, paths and other statement types.
"""

from dataclasses import dataclass
from typing import List, Optional, Union
from .values import ASTNode, AttributeOperator
from .expressions import NodeExpression, AttributeExpression


@dataclass
class NodeDecl(ASTNode):
    """Node declaration with optional attributes."""
    nodes: NodeExpression
    attributes: Optional[AttributeExpression] = None


@dataclass
class Path(ASTNode):
    """Path expression: id.field.subfield."""
    components: List[str]


@dataclass
class Argument(ASTNode):
    """Command argument: name = path."""
    name: str
    operator: AttributeOperator
    path: Path


@dataclass
class Command(ASTNode):
    """Command execution: run graphName with (arg1=path1, arg2=path2)."""
    graph_name: str
    arguments: List[Argument]


# Statement union type - import EdgeDecl from expressions
from .expressions import EdgeDecl
Statement = Union[NodeDecl, EdgeDecl]
