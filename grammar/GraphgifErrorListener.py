from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


class GraphGifErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Customize your error message
        error_msg = f"Syntax error at line {line}:{column} - {msg}"
        raise SyntaxError(error_msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass  # Handle ambiguity if needed

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass  # Handle full context attempt if needed

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass  # Handle context sensitivity if needed


class GraphGifError(Exception):
    """Base class for GraphGif interpreter errors"""
    pass


class SemanticError(GraphGifError):
    """For semantic errors in the interpreter"""
    pass