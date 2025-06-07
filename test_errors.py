from parsing import parse_graphgif_file
from visitors import GraphgifPrettyPrinter, GraphStatisticsVisitor
import os

example_dir = './errors/examples'

for i, example_file in enumerate(os.listdir(example_dir)):
    example_path = os.path.join(example_dir, example_file)
    print('\n' + '-' * 10 + f' EXAMPLE: {example_file} ' + '-' * 10)
    ast, graph_model = parse_graphgif_file(example_path)
    print(f"AST type: {type(ast)}")
    print(f"Graph model type: {type(graph_model)}")

    printer = GraphgifPrettyPrinter()
    printer.visit_program(ast)
    print("\nAST Representation:")
    print(printer.get_output())

    print("\nConcrete Graph Model:")
    print(graph_model)

    stats_visitor = GraphStatisticsVisitor()
    stats_visitor.visit_program(ast)
    stats = stats_visitor.get_statistics()

    print("\nStatistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
