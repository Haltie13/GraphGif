class GraphgifError(Exception):
    """Base exception for all Graphgif errors."""

    def __init__(self, message: str, line: int = None, column: int = None, context: str = None):
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column
        self.context = context

    def __str__(self):
        location = ""
        if self.line is not None:
            location = f" at line {self.line}"
            if self.column is not None:
                location += f":{self.column}"

        context_info = ""
        if self.context:
            context_info = f"\nContext: {self.context}"

        return f"{self.__class__.__name__}{location}: {self.message}{context_info}"


class SyntaxError(GraphgifError):
    """Syntax errors from parser."""
    pass


class LexerError(SyntaxError):
    """Lexical analysis errors."""
    pass


class ParserError(SyntaxError):
    """Grammar/syntax parsing errors."""
    pass


class SemanticError(GraphgifError):
    """Semantic errors (undefined variables, type mismatches, etc.)."""
    pass


class ValidationError(GraphgifError):
    """Validation errors (graph structure issues, etc.)."""
    pass


class RuntimeError(GraphgifError):
    """Runtime errors during graph generation."""
    pass


class UndefinedVariableError(SemanticError):
    """Variable reference to undefined variable."""

    def __init__(self, var_name: str, line: int = None, column: int = None, context: str = None):
        super().__init__(f"Undefined variable: '{var_name}'", line, column, context)
        self.var_name = var_name


class TypeMismatchError(SemanticError):
    """Type mismatch error."""

    def __init__(self, expected_type: str, actual_type: str, var_name: str = None,
                 line: int = None, column: int = None, context: str = None):
        var_info = f" for variable '{var_name}'" if var_name else ""
        super().__init__(
            f"Type mismatch{var_info}: expected {expected_type}, got {actual_type}",
            line, column, context
        )
        self.expected_type = expected_type
        self.actual_type = actual_type
        self.var_name = var_name


class DuplicateDeclarationError(SemanticError):
    """Duplicate variable or graph declaration."""

    def __init__(self, name: str, declaration_type: str = "variable",
                 line: int = None, column: int = None, context: str = None):
        super().__init__(f"Duplicate {declaration_type} declaration: '{name}'", line, column, context)
        self.name = name
        self.declaration_type = declaration_type