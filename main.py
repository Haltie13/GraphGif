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

    try:
        print("Parsowanie pliku...")
        ast_tree, graph_model, execution_results = parse_graphgif_file(args.input_file, args.output)
        
        if execution_results:
            print(f"Wykonano {len(execution_results)} komend")
            for graph_name, result in execution_results.items():
                print(f"  Graf: {graph_name}")
                print(f"  Algorytm: {result['algorithm']}")
                if result['output_files']:
                    print(f"  Pliki wyjściowe: {', '.join(result['output_files'])}")
        else:
            print("Brak komend do wykonania")
            
    except Exception as e:
        print(f"Błąd podczas przetwarzania: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
