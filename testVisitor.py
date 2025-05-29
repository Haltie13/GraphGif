from antlr4 import FileStream, CommonTokenStream
from grammar.GraphgifLexer import GraphgifLexer
from grammar.GraphgifParser import GraphgifParser
from parsing.grammar.GraphgifVisitorImpl import GraphgifVisitorImpl

input_stream = FileStream('./examples/example1.gg')

lexer = GraphgifLexer(input_stream)
tokens = CommonTokenStream(lexer)

parser = GraphgifParser(tokens)
tree = parser.program()  # To jest parse tree!

visitor = GraphgifVisitorImpl()
visitor.visit(tree)
