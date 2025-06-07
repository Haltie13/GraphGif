# Core error classes
from .exceptions import (
    GraphgifError,
    SyntaxError,
    LexerError,
    ParserError,
    SemanticError,
    ValidationError,
    RuntimeError,
    UndefinedVariableError,
    TypeMismatchError,
    DuplicateDeclarationError
)

# Error listener implementation
from .error_listener import GraphGifErrorListener

__all__ = [
    # Base exceptions
    'GraphgifError',

    # Syntax errors
    'SyntaxError',
    'LexerError',
    'ParserError',

    # Semantic errors
    'SemanticError',
    'ValidationError',
    'RuntimeError',
    'UndefinedVariableError',
    'TypeMismatchError',
    'DuplicateDeclarationError',

    # Listener
    'GraphGifErrorListener',

]

# Optional: Default error listener instance
default_error_listener = GraphGifErrorListener()