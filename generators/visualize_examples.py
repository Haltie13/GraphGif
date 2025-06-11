#!/usr/bin/env python3
"""
Practical example: Generate DOT visualizations for GraphGif example files.
This script parses .gg files and creates algorithm visualizations.
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsing import parse_graphgif_file
from algorithms import AlgorithmExecutor
from generators import DotGenerator


def process_example_file(example_path: str, output_base_dir: str = "visualizations"):
    """Process a single .gg file and generate visualizations."""
    print(f"\n📁 Processing {os.path.basename(example_path)}")
    print("-" * 50)
    
    try:
        # Parse the file
        ast, graph_model = parse_graphgif_file(example_path)
        print("✅ Parsing successful")
        
        # Get the first graph (assuming single graph per file for demo)
        if not graph_model.graphs:
            print("⚠️  No graphs found in file")
            return
        
        graph_name = list(graph_model.graphs.keys())[0]
        concrete_graph = graph_model.graphs[graph_name]
        
        print(f"📊 Graph: {concrete_graph.name}")
        print(f"   Nodes: {len(concrete_graph.nodes)}")
        print(f"   Edges: {len(concrete_graph.edges)}")
        print(f"   Type: {'Directed' if concrete_graph.is_directed else 'Undirected'}")
        
        # Setup output directory
        file_base = os.path.splitext(os.path.basename(example_path))[0]
        output_dir = os.path.join(output_base_dir, file_base)
        
        # Execute compatible algorithms and generate visualizations
        executor = AlgorithmExecutor()
        compatible_algorithms = executor.get_algorithms_for_graph(graph_model)
        
        generated_files = []
        
        for alg_name, info in compatible_algorithms.items():
            if not info['valid']:
                print(f"⏭️  Skipping {info['name']}: {info['reason']}")
                continue
                
            print(f"\n🔄 Executing {info['name']}...")
            
            try:
                # Execute algorithm
                result = executor.execute_algorithm(alg_name, concrete_graph)
                
                if not result.success:
                    print(f"   ❌ Failed: {result.error_message}")
                    continue
                
                print(f"   ✅ Success! ({len(result.states)} states)")
                
                # Generate DOT files
                alg_output_dir = os.path.join(output_dir, alg_name.replace(" ", "_").lower())
                generator = DotGenerator(output_dir=alg_output_dir, 
                                       render_images=True, 
                                       image_format="png")
                
                files = generator.generate(concrete_graph, result, 
                                         f"{file_base}_{alg_name.replace(' ', '_').lower()}")
                generated_files.extend(files)
                
                print(f"   📁 Generated {len(files)} files in {alg_output_dir}")
                
                # Generate animation script
                script_path = generator.generate_animation_script(
                    f"{file_base}_{alg_name.replace(' ', '_').lower()}", result)
                generated_files.append(script_path)
                
            except Exception as e:
                print(f"   ❌ Error: {e}")
        
        if generated_files:
            print(f"\n📊 Total generated files: {len(generated_files)}")
            print("💡 To create animations, run the generated shell scripts")
        else:
            print("\n⚠️  No visualizations generated")
            
    except Exception as e:
        print(f"❌ Error processing {example_path}: {e}")


def main():
    """Process all example files and generate visualizations."""
    print("🎨 GRAPHGIF VISUALIZATION GENERATOR")
    print("=" * 60)
    print("Generating DOT files and images for algorithm visualizations...")
    
    # Find example files
    examples_dir = "examples"
    if not os.path.exists(examples_dir):
        print(f"❌ Examples directory not found: {examples_dir}")
        return
    
    example_files = [f for f in os.listdir(examples_dir) if f.endswith('.gg')]
    
    if not example_files:
        print(f"❌ No .gg files found in {examples_dir}")
        return
    
    print(f"📁 Found {len(example_files)} example files")
    
    # Process each file
    for example_file in sorted(example_files):
        example_path = os.path.join(examples_dir, example_file)
        process_example_file(example_path)
    
    print("\n" + "=" * 60)
    print("🏁 VISUALIZATION GENERATION COMPLETED")
    print("=" * 60)
    
    print("\n📂 Output structure:")
    print("visualizations/")
    print("├── example1/")
    print("│   ├── breadth_first_search/")
    print("│   │   ├── *.dot files")
    print("│   │   ├── *.png files (if Graphviz installed)")
    print("│   │   └── *_animate.sh")
    print("│   └── depth_first_search/")
    print("└── example2/")
    print("    └── ...")
    
    print("\n💡 To view results:")
    print("1. Install Graphviz: brew install graphviz (macOS)")
    print("2. Install ImageMagick: brew install imagemagick (for animations)")
    print("3. Open .dot files in any text editor")
    print("4. View .png files in any image viewer")
    print("5. Run .sh scripts to create animated GIFs")


if __name__ == "__main__":
    main()
