#!/usr/bin/env python3
"""
Comprehensive test suite for the GraphGif algorithm system.
Tests algorithm compatibility, execution, and edge case handling.
"""

import os
import sys
import time
from typing import Dict, Any

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsing import parse_graphgif_file
from algorithms import AlgorithmExecutor
from algorithms.base import ValidationResult
from models.graph_model import ConcreteGraph, GraphNode, GraphEdge, GraphModel


def test_example_files():
    """Test algorithm execution on example .gg files."""
    print("=" * 60)
    print("TESTING EXAMPLE FILES")
    print("=" * 60)
    
    example_dir = '../examples'
    executor = AlgorithmExecutor()
    
    if not os.path.exists(example_dir):
        print(f"❌ Example directory not found: {example_dir}")
        return False
    
    success_count = 0
    total_count = 0
    
    for example_file in sorted(os.listdir(example_dir)):
        if not example_file.endswith('.gg'):
            continue
            
        example_path = os.path.join(example_dir, example_file)
        total_count += 1
        
        print(f"\n📁 Testing {example_file}")
        print("-" * 40)
        
        try:
            # Parse the file
            ast, graph_model = parse_graphgif_file(example_path)
            print(f"✅ Parsing successful")
            
            # Get compatible algorithms
            compatible_algorithms = executor.get_algorithms_for_graph(graph_model)
            
            if not compatible_algorithms:
                print("⚠️  No compatible algorithms found")
                continue
            
            print(f"📊 Found {len(compatible_algorithms)} algorithms:")
            
            executed_any = False
            for alg_name, info in compatible_algorithms.items():
                status = "✅" if info['valid'] else "❌"
                print(f"  {status} {info['name']} ({info['type']})")
                
                if not info['valid']:
                    print(f"     Reason: {info['reason']}")
                else:
                    # Execute the algorithm
                    try:
                        print(f"  🔄 Executing {info['name']}...")
                        start_time = time.time()
                        result = executor.execute_algorithm(alg_name, graph_model)
                        execution_time = time.time() - start_time
                        
                        if result.success:
                            print(f"     ✅ Success! Steps: {len(result.states)}, Time: {execution_time:.4f}s")
                            if result.final_result:
                                print(f"     📊 Result: {result.final_result}")
                            executed_any = True
                        else:
                            print(f"     ❌ Failed: {result.error_message}")
                    
                    except Exception as e:
                        print(f"     ❌ Exception during execution: {e}")
            
            if executed_any:
                success_count += 1
                
        except Exception as e:
            print(f"❌ Error processing {example_file}: {e}")
    
    print(f"\n📈 Summary: {success_count}/{total_count} files processed successfully")
    return success_count == total_count


def test_manual_graphs():
    """Test algorithms on manually created graphs."""
    print("\n" + "=" * 60)
    print("TESTING MANUAL GRAPH CREATION")
    print("=" * 60)
    
    executor = AlgorithmExecutor()
    
    # Test 1: Simple triangle graph
    print("\n🔺 Test 1: Simple Triangle Graph")
    print("-" * 30)
    
    triangle = ConcreteGraph(name="Triangle", directed=False)
    triangle.add_node("A")
    triangle.add_node("B") 
    triangle.add_node("C")
    triangle.add_edge("A", "B")
    triangle.add_edge("B", "C")
    triangle.add_edge("C", "A")
    
    test_algorithms_on_graph(executor, triangle)
    
    # Test 2: Weighted directed graph
    print("\n⚖️  Test 2: Weighted Directed Graph")
    print("-" * 35)
    
    weighted = ConcreteGraph(name="Weighted", directed=True)
    weighted.add_node("Start")
    weighted.add_node("Middle")
    weighted.add_node("End")
    weighted.add_edge("Start", "Middle", {"weight": 5})
    weighted.add_edge("Middle", "End", {"weight": 3})
    weighted.add_edge("End", "Start", {"weight": 8})
    
    test_algorithms_on_graph(executor, weighted)
    
    # Test 3: Disconnected graph
    print("\n🔗 Test 3: Disconnected Graph")
    print("-" * 28)
    
    disconnected = ConcreteGraph(name="Disconnected", directed=False)
    disconnected.add_node("A")
    disconnected.add_node("B")
    disconnected.add_node("C")
    disconnected.add_node("D")
    disconnected.add_edge("A", "B")
    disconnected.add_edge("C", "D")  # Separate component
    
    test_algorithms_on_graph(executor, disconnected)


def test_algorithms_on_graph(executor: AlgorithmExecutor, graph: ConcreteGraph):
    """Helper function to test all algorithms on a given graph."""
    print(f"Graph: {graph.name} ({'directed' if graph.directed else 'undirected'})")
    print(f"Nodes: {len(graph.nodes)}, Edges: {len(graph.edges)}")
    
    try:
        # Create a GraphModel to wrap the ConcreteGraph for the executor
        graph_model = GraphModel()
        graph_model.add_graph(graph)
        
        compatible_algorithms = executor.get_algorithms_for_graph(graph_model)
        
        if not compatible_algorithms:
            print("⚠️  No compatible algorithms")
            return
        
        valid_count = sum(1 for info in compatible_algorithms.values() if info['valid'])
        print(f"Compatible algorithms: {valid_count}/{len(compatible_algorithms)}")
        
        for alg_name, info in compatible_algorithms.items():
            status = "✅" if info['valid'] else "❌"
            print(f"  {status} {info['name']}")
            
            if info['valid']:
                try:
                    result = executor.execute_algorithm(alg_name, graph_model)
                    if result.success:
                        print(f"     ✅ Executed successfully ({len(result.states)} steps)")
                    else:
                        print(f"     ❌ Execution failed: {result.error_message}")
                except Exception as e:
                    print(f"     ❌ Exception: {e}")
            else:
                print(f"     Reason: {info['reason']}")
    
    except Exception as e:
        print(f"❌ Error testing graph: {e}")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n" + "=" * 60)
    print("TESTING EDGE CASES")
    print("=" * 60)
    
    executor = AlgorithmExecutor()
    
    # Test 1: Empty graph
    print("\n🕳️  Test 1: Empty Graph")
    print("-" * 20)
    
    empty = ConcreteGraph(name="Empty", directed=False)
    test_algorithms_on_graph(executor, empty)
    
    # Test 2: Single node
    print("\n🔘 Test 2: Single Node")
    print("-" * 21)
    
    single = ConcreteGraph(name="Single", directed=False)
    single.add_node("Lonely")
    test_algorithms_on_graph(executor, single)
    
    # Test 3: Self-loop
    print("\n🔄 Test 3: Self-Loop")
    print("-" * 20)
    
    self_loop = ConcreteGraph(name="SelfLoop", directed=True)
    self_loop.add_node("A")
    self_loop.add_edge("A", "A")
    test_algorithms_on_graph(executor, self_loop)
    
    # Test 4: Invalid weight
    print("\n❌ Test 4: Invalid Weight")
    print("-" * 24)
    
    invalid_weight = ConcreteGraph(name="InvalidWeight", directed=False)
    invalid_weight.add_node("A")
    invalid_weight.add_node("B")
    invalid_weight.add_edge("A", "B", {"weight": "invalid"})
    test_algorithms_on_graph(executor, invalid_weight)


def test_algorithm_validation():
    """Test individual algorithm validation logic."""
    print("\n" + "=" * 60)
    print("TESTING ALGORITHM VALIDATION")
    print("=" * 60)
    
    executor = AlgorithmExecutor()
    
    # Create test graphs
    directed_weighted = ConcreteGraph(name="DirectedWeighted", directed=True)
    directed_weighted.add_node("A")
    directed_weighted.add_node("B")
    directed_weighted.add_edge("A", "B", {"weight": 1.5})
    
    undirected_unweighted = ConcreteGraph(name="UndirectedUnweighted", directed=False)
    undirected_unweighted.add_node("X")
    undirected_unweighted.add_node("Y")
    undirected_unweighted.add_edge("X", "Y")
    
    print("\nTesting validation logic:")
    
    # Test each algorithm's validation
    for alg_name in executor.algorithms:
        algorithm = executor.algorithms[alg_name]
        
        print(f"\n🔍 Algorithm: {algorithm.name}")
        print(f"   Type: {algorithm.algorithm_type.value}")
        print(f"   Requirements: directed={algorithm.requires_directed}, weighted={algorithm.requires_weighted}")
        
        # Test on both graphs
        for graph in [directed_weighted, undirected_unweighted]:
            try:
                # Create GraphModel wrapper for proper testing
                graph_model = GraphModel()
                graph_model.add_graph(graph)
                
                # Test validation through executor (which handles GraphModel properly)
                compatible_algorithms = executor.get_algorithms_for_graph(graph_model)
                if alg_name in compatible_algorithms:
                    info = compatible_algorithms[alg_name]
                    status = "✅" if info['valid'] else "❌"
                    print(f"   {status} {graph.name}: {info['reason'] if not info['valid'] else 'Valid'}")
                else:
                    print(f"   ❌ {graph.name}: Algorithm not found in executor")
            except Exception as e:
                print(f"   ❌ {graph.name}: Exception during validation: {e}")


def main():
    """Run all tests."""
    print("🧪 GRAPHGIF ALGORITHM SYSTEM COMPREHENSIVE TESTS")
    print("=" * 60)
    
    try:
        # Test 1: Example files
        example_success = test_example_files()
        
        # Test 2: Manual graphs
        test_manual_graphs()
        
        # Test 3: Edge cases
        test_edge_cases()
        
        # Test 4: Algorithm validation
        test_algorithm_validation()
        
        print("\n" + "=" * 60)
        print("🏁 ALL TESTS COMPLETED")
        print("=" * 60)
        
        if example_success:
            print("✅ All example files processed successfully!")
        else:
            print("⚠️  Some example files had issues - check output above")
        
        print("\nTest suite finished. Check the output above for detailed results.")
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
