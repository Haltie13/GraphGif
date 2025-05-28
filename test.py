from ast_builder import *
from example_usage import GraphgifPrettyPrinter, GraphStatisticsVisitor
from grammar.GraphgifVisitorImpl import GraphgifVisitorImpl


ast = parse_graphgif_file('./examples/example1.gg')
print(type(ast))
printer = GraphgifPrettyPrinter()
printer.visit_program(ast)
print(printer.get_output())

stats_visitor = GraphStatisticsVisitor()
stats_visitor.visit_program(ast)
stats = stats_visitor.get_statistics()
        
print("\nStatistics:")
print("=" * 50)
for key, value in stats.items():
    print(f"{key}: {value}")
