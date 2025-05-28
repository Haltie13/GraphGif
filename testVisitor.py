from antlr4 import FileStream, CommonTokenStream
from grammar.GraphgifLexer import GraphgifLexer
from grammar.GraphgifParser import GraphgifParser
from parsing.grammar.GraphgifVisitorImpl import GraphgifVisitorImpl

# Wczytaj plik jako strumień
input_stream = FileStream('./examples/example1.gg')

# Lexer i TokenStream
lexer = GraphgifLexer(input_stream)
tokens = CommonTokenStream(lexer)

# Parser
parser = GraphgifParser(tokens)
tree = parser.program()  # To jest parse tree!

# Teraz visitor z ANTLR na parse tree
visitor = GraphgifVisitorImpl()
visitor.visit(tree)
