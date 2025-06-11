import os
import sys
import traceback

from algorithms import AlgorithmExecutor
from generators import DotGenerator

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parsing import parse_graphgif_file, parse_graphgif
from visitors import GraphGifVisitor
from errors import *


def test_dijkstra():
    _, graph_model = parse_graphgif_file('./examples/example3.gg')

    concrete_graphs = []
    if graph_model is not None:
        if graph_model.graphs is not None:
            for name, concrete_graph in graph_model.graphs.items():
                concrete_graphs.append(concrete_graph)
                print("="*50)
                print(f'Graph: {name}')
                for node_id, node in concrete_graph.nodes.items():
                    print(f'Node: {node_id}')
                    print(node)
                    print('-'*50)
                for edge in concrete_graph.edges:
                    print(f'Edge: {edge}')

    executor = AlgorithmExecutor()
    for result in executor.get_algorithms_for_graph(graph_model).values():
        print(result)
    result = executor.execute_algorithm('Dijkstra\'s Algorithm', graph_model)
    generator = DotGenerator(render_images=True)
    generator.generate(concrete_graphs[0], result, '3')
    generator.generate_animation_script('3')




if __name__ == '__main__':
    test_dijkstra()