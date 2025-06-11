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
    parser.add_argument('--verbose', '-v',
                        action='store_true',
                        help='Verbose output - show detailed information')
    parser.add_argument('--no-validation',
                        action='store_true',
                        help='Skip semantic validation (faster but risky)')
    parser.add_argument('--format',
                        choices=['png', 'svg', 'pdf', 'gif'],
                        default='png',
                        help='Output format for generated images')
    parser.add_argument('--render-images',
                        action='store_true',
                        default=True,
                        help='Generate image files from DOT files')
    parser.add_argument('--no-render',
                        action='store_true',
                        help='Only generate DOT files, skip image rendering')
    parser.add_argument('--dry-run',
                        action='store_true',
                        help='Parse and validate only, do not execute commands')
    parser.add_argument('--list-algorithms',
                        action='store_true',
                        help='List available algorithms and exit')


    args = parser.parse_args()

    if not pathlib.Path(args.input_file).exists():
        print(f"Błąd: Plik {args.input_file} nie istnieje")
        sys.exit(1)

    print(f"Przetwarzam: {args.input_file}")
    print(f"Wynik zostanie zapisany w: {args.output}")

    try:
        if args.verbose:
            print("Parsowanie pliku...")
        ast_tree, graph_model, execution_results = parse_graphgif_file(args.input_file)

    except Exception as e:
        print(f"Błąd podczas przetwarzania: {str(e)}")
        import traceback
        if args.verbose:  # Tryb gadatliwy - pokaż pełny traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
