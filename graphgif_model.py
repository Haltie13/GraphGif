"""
Structured Python model for the Graphgif language AST.
This module contains classes representing the Abstract Syntax Tree nodes
based on the Graphgif.g4 grammar file.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Union
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


# Lists and collections
@dataclass
class NodeList(ASTNode):
    """List of node IDs."""
    nodes: List[str]


@dataclass
class Attribute(ASTNode):
    """Single attribute with key-value pair."""
    key: str
    operator: AttributeOperator
    value: Value


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


# Variable values union type
VarValue = Union[NodeVarRef, EdgeVarRef, AttrVarRef, NodeList, EdgeList, AttrList]


# Variable declarations
@dataclass
class VarDecl(ASTNode):
    """Variable declaration: var type name = value."""
    var_type: VarType
    name: str
    value: VarValue


# Graph structure
@dataclass
class NodeDecl(ASTNode):
    """Node declaration with optional attributes."""
    nodes: Union[NodeList, NodeVarRef]
    attributes: Optional[Union[AttrList, AttrVarRef]] = None


@dataclass
class GlobalAttrDecl(ASTNode):
    """Global attribute declaration for graph, node, or edge."""
    attr_type: GlobalAttrType
    attributes: Union[AttrList, AttrVarRef]


Statement = Union[NodeDecl, EdgeDecl]


@dataclass
class GraphDecl(ASTNode):
    """Graph declaration with direction, name, global attributes, and statements."""
    direction: GraphDirection
    name: str
    global_attributes: List[GlobalAttrDecl]
    statements: List[Statement]


# Commands
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


# Root program
@dataclass
class Program(ASTNode):
    """Root program containing variable declarations, graph declarations, and commands."""
    variable_declarations: List[VarDecl]
    graph_declarations: List[GraphDecl]
    commands: List[Command]


# Visitor pattern for AST traversal
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


# Factory functions for creating AST nodes
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


# Utility functions
def pretty_print_ast(node: ASTNode, indent: int = 0) -> str:
    """Pretty print the AST for debugging purposes."""
    indent_str = "  " * indent
    if isinstance(node, Program):
        result = f"{indent_str}Program:\n"
        result += f"{indent_str}  Variables:\n"
        for var in node.variable_declarations:
            result += pretty_print_ast(var, indent + 2)
        result += f"{indent_str}  Graphs:\n"
        for graph in node.graph_declarations:
            result += pretty_print_ast(graph, indent + 2)
        result += f"{indent_str}  Commands:\n"
        for cmd in node.commands:
            result += pretty_print_ast(cmd, indent + 2)
        return result
    elif isinstance(node, VarDecl):
        return f"{indent_str}VarDecl({node.var_type.value}, {node.name})\n"
    elif isinstance(node, GraphDecl):
        return f"{indent_str}Graph({node.direction.value}, {node.name})\n"
    elif isinstance(node, Command):
        return f"{indent_str}Command({node.graph_name})\n"
    else:
        return f"{indent_str}{type(node).__name__}\n"
