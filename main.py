"""
Main entry point for GraphGif language processing.
This module demonstrates the complete workflow of parsing, analyzing, and working with GraphGif code.
"""


from parsing import parse_graphgif, parse_graphgif_file
from visitors import GraphgifPrettyPrinter, GraphStatisticsVisitor
import argparse
import pathlib
import sys

def main():
    parser = argparse.ArgumentParser(
        description='GraphGif - Translator of graph language to Graphviz animation'
    )
    parser.add_argument('input_file',
                        help='Input file with graph language code')
    parser.add_argument('-o', '--output',
                        help='Output directory for generated files',
                        default='output')


    args = parser.parse_args()

    if not pathlib.Path(args.input_file).exists():
        print(f"Błąd: Plik {args.input_file} nie istnieje")
        sys.exit(1)

    print(f"Przetwarzam: {args.input_file}")
    print(f"Wynik zostanie zapisany w: {args.output}")

    ast_tree, graph_model = parse_graphgif_file(args.input_file)


if __name__ == "__main__":
    main()
