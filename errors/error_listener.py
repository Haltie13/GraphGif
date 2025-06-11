from antlr4 import Lexer
from antlr4.error.ErrorListener import ErrorListener
from .exceptions import LexerError, ParserError


class GraphGifErrorListener(ErrorListener):
    """Enhanced error listener with error collection and pretty printing."""

    def __init__(self, source_name: str = "input"):
        super().__init__()
        self.source_name = source_name
        self._input_cache = None
        self.errors = []  # Stores all encountered errors

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        context_line, marker = self._get_error_context(recognizer, line, column, offending_symbol)
        full_context = f"{context_line}\n{marker}" if context_line else None

        # Create error dictionary
        error = {
            'type': 'lexer' if isinstance(recognizer, Lexer) else 'parser',
            'message': msg,
            'line': line,
            'column': column,
            'context': full_context,
            'offending_symbol': offending_symbol.text if offending_symbol else None
        }
        self.errors.append(error)

        # Still raise exceptions for immediate failure
        # if isinstance(recognizer, Lexer):
        #     raise LexerError(msg, line, column, full_context)
        # else:
        #     expected = self._get_expected_tokens(recognizer)
        #     enhanced_msg = f"{msg} (expected: {expected})" if expected else msg
        #     raise ParserError(enhanced_msg, line, column, full_context)

    def print_errors(self):
        """Prints all collected errors in a user-friendly format."""
        if not self.errors:
            print("No errors found")
            return

        print(f"\nFound {len(self.errors)} errors in {self.source_name}:")
        for i, error in enumerate(self.errors, 1):
            print(f"\nError {i}: {error['type'].upper()} error")
            print(f"Line {error['line']}:{error['column']} - {error['message']}")
            if error['context']:
                print(error['context'])

    def has_errors(self):
        """Returns True if any errors were collected."""
        return len(self.errors) > 0

    def get_errors(self):
        """Returns the list of all error dictionaries."""
        return self.errors.copy()

    def _get_input_lines(self, input_stream):
        """Cache and return the input lines"""
        if self._input_cache is None:
            if hasattr(input_stream, 'strdata'):
                self._input_cache = input_stream.strdata.split('\n')
            elif hasattr(input_stream, 'tokenSource'):
                src = input_stream.tokenSource.inputStream
                if hasattr(src, 'strdata'):
                    self._input_cache = src.strdata.split('\n')
            else:
                self._input_cache = []
        return self._input_cache

    def _get_error_context(self, recognizer, line, column, offending_symbol):
        """Extract the error line and generate marker"""
        input_stream = recognizer.getInputStream()
        lines = self._get_input_lines(input_stream)

        context_line = lines[line - 1] if 0 < line <= len(lines) else ""

        if offending_symbol:
            start = offending_symbol.start
            stop = offending_symbol.stop
            if start >= 0 and stop >= start:
                marker = ' ' * (column) + '^' * (stop - start + 1)
            else:
                marker = ' ' * column + '^'
        else:
            marker = ' ' * column + '^'

        return context_line, marker

    def _get_expected_tokens(self, recognizer):
        """Get expected tokens for parser errors"""
        if hasattr(recognizer, 'getExpectedTokens'):
            expected = recognizer.getExpectedTokens()
            if expected:
                return ", ".join(str(t) for t in expected)
        return None

    # Other ANTLR listener methods remain unchanged
    def reportAmbiguity(self, *args):
        pass

    def reportAttemptingFullContext(self, *args):
        pass

    def reportContextSensitivity(self, *args):
        pass
    
    def report_graph_direction_error(self, line, column, message, context_line=None):
        """Report a semantic error related to graph direction."""
        error = {
            'type': 'semantic',
            'message': message,
            'line': line,
            'column': column,
            'context': context_line,
            'offending_symbol': None
        }
        self.errors.append(error)