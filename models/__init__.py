"""
GraphGif AST model package.
This package contains all the AST node types, factory methods, and utilities
for working with GraphGif language syntax trees.
"""

# Import all classes from submodules
from .values import (
    ASTNode, Value, VarRef, NodeVarRef, EdgeVarRef, AttrVarRef, Attribute,
    GraphDirection, VarType, EdgeOperator, GlobalAttrType, AttributeOperator
)

from .expressions import (
    NodeList, AttrList, EdgeDecl, EdgeList,
    NodeExpression, EdgeExpression, AttributeExpression, VarValue
)

from .statements import (
    NodeDecl, Path, Argument, Command, Statement
)

from .ast_nodes import (
    VarDecl, GlobalAttrDecl, GraphDecl, Program
)

from .factories import ASTFactory

# Export all public classes
__all__ = [
    # Base classes and values
    'ASTNode', 'Value', 'VarRef', 'NodeVarRef', 'EdgeVarRef', 'AttrVarRef', 'Attribute',
    
    # Enums
    'GraphDirection', 'VarType', 'EdgeOperator', 'GlobalAttrType', 'AttributeOperator',
    
    # Expressions
    'NodeList', 'AttrList', 'EdgeDecl', 'EdgeList',
    'NodeExpression', 'EdgeExpression', 'AttributeExpression', 'VarValue',
    
    # Statements
    'NodeDecl', 'Path', 'Argument', 'Command', 'Statement',
    
    # AST nodes
    'VarDecl', 'GlobalAttrDecl', 'GraphDecl', 'Program',
    
    # Factory
    'ASTFactory'
]
