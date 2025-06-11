#!/usr/bin/env python3
"""
Test script for the DOT generator.
Demonstrates generating DOT files from algorithm execution states.
"""

import os
import sys
import shutil

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators import DotGenerator
from algorithms import AlgorithmExecutor
from models.graph_model import ConcreteGraph


def create_sample_graph() -> ConcreteGraph:
    """Create a sample graph for testing."""
    graph = ConcreteGraph(name="SampleGraph", directed=False)
    
    # Add nodes
    graph.add_node("A", {"label": "Start"})
    graph.add_node("B", {"label": "Middle"})
    graph.add_node("C", {"label": "End"})
    graph.add_node("D", {"label": "Branch"})
    
    # Add edges
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")
    graph.add_edge("A", "D")
    
    return graph


def create_weighted_graph() -> ConcreteGraph:
    """Create a weighted graph for Dijkstra testing."""
    graph = ConcreteGraph(name="WeightedGraph", directed=True)
    
    # Add nodes
    graph.add_node("S", {"label": "Start"})
    graph.add_node("A", {"label": "Node A"})
    graph.add_node("B", {"label": "Node B"})
    graph.add_node("T", {"label": "Target"})
    
    # Add weighted edges
    graph.add_edge("S", "A", {"weight": 2})
    graph.add_edge("S", "B", {"weight": 4})
    graph.add_edge("A", "B", {"weight": 1})
    graph.add_edge("A", "T", {"weight": 7})
    graph.add_edge("B", "T", {"weight": 3})
    
    return graph


def test_bfs_generation():
    """Test DOT generation for BFS algorithm."""
    print("🔍 Testing BFS DOT Generation")
    print("-" * 40)
    
    # Create graph and executor
    graph = create_sample_graph()
    executor = AlgorithmExecutor()
    
    # Execute BFS
    result = executor.execute_algorithm("breadth-first search", graph, start_node="A")
    
    if not result.success:
        print(f"❌ BFS execution failed: {result.error_message}")
        return
    
    print(f"✅ BFS executed successfully ({len(result.states)} states)")
    
    # Generate DOT files
    generator = DotGenerator(output_dir="output/bfs", render_images=True)
    generated_files = generator.generate(graph, result, "bfs_sample")
    
    print(f"📁 Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"   - {file}")
    
    # Generate animation script
    script_path = generator.generate_animation_script("bfs_sample", result)
    print(f"🎬 Animation script: {script_path}")


def test_dfs_generation():
    """Test DOT generation for DFS algorithm."""
    print("\n🌲 Testing DFS DOT Generation")
    print("-" * 40)
    
    # Create graph and executor
    graph = create_sample_graph()
    executor = AlgorithmExecutor()
    
    # Execute DFS
    result = executor.execute_algorithm("depth-first search", graph, start_node="A")
    
    if not result.success:
        print(f"❌ DFS execution failed: {result.error_message}")
        return
    
    print(f"✅ DFS executed successfully ({len(result.states)} states)")
    
    # Generate DOT files
    generator = DotGenerator(output_dir="output/dfs", render_images=True)
    generated_files = generator.generate(graph, result, "dfs_sample")
    
    print(f"📁 Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"   - {file}")


def test_dijkstra_generation():
    """Test DOT generation for Dijkstra's algorithm."""
    print("\n⚖️  Testing Dijkstra DOT Generation")
    print("-" * 40)
    
    # Create weighted graph and executor
    graph = create_weighted_graph()
    executor = AlgorithmExecutor()
    
    # Execute Dijkstra
    result = executor.execute_algorithm("dijkstra's algorithm", graph, 
                                      start_node="S", target_node="T")
    
    if not result.success:
        print(f"❌ Dijkstra execution failed: {result.error_message}")
        return
    
    print(f"✅ Dijkstra executed successfully ({len(result.states)} states)")
    print(f"📊 Final result: {result.final_result}")
    
    # Generate DOT files
    generator = DotGenerator(output_dir="output/dijkstra", render_images=True)
    generated_files = generator.generate(graph, result, "dijkstra_sample")
    
    print(f"📁 Generated {len(generated_files)} files:")
    for file in generated_files:
        print(f"   - {file}")


def test_single_state_generation():
    """Test generating a single state DOT file."""
    print("\n🎯 Testing Single State Generation")
    print("-" * 40)
    
    # Create graph and execute algorithm
    graph = create_sample_graph()
    executor = AlgorithmExecutor()
    result = executor.execute_algorithm("breadth-first search", graph, start_node="A")
    
    if not result.success:
        print(f"❌ Algorithm execution failed: {result.error_message}")
        return
    
    # Generate single state (middle step)
    generator = DotGenerator(output_dir="output/single")
    middle_state = result.states[len(result.states) // 2]
    
    filepath = generator.generate_single_state(graph, middle_state, "single_state.dot")
    print(f"📄 Generated single state file: {filepath}")
    
    # Read and display content
    with open(filepath, 'r') as f:
        content = f.read()
    
    print("\n📝 Generated DOT content:")
    print(content)


def cleanup_output():
    """Clean up output directories."""
    output_dir = "output"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        print(f"🧹 Cleaned up {output_dir} directory")


def main():
    """Run all DOT generator tests."""
    print("🧪 GRAPHGIF DOT GENERATOR TESTS")
    print("=" * 60)
    
    try:
        # Clean up previous output
        cleanup_output()
        
        # Run tests
        test_bfs_generation()
        test_dfs_generation()
        test_dijkstra_generation()
        test_single_state_generation()
        
        print("\n" + "=" * 60)
        print("🏁 ALL DOT GENERATOR TESTS COMPLETED")
        print("=" * 60)
        
        print("\n💡 Tips:")
        print("- Install Graphviz (brew install graphviz) to render images")
        print("- Install ImageMagick (brew install imagemagick) to create animations")
        print("- Run the generated shell scripts to create animated GIFs")
        print("- Check the output/ directory for generated files")
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
