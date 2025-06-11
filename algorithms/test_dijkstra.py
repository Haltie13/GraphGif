#!/usr/bin/env python3
"""
Specialized test suite for Dijkstra's algorithm with large graph testing.
Creates comprehensive test cases including performance testing on large graphs.
"""

import os
import sys
import time
import random
from typing import Dict, Any, List, Tuple

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsing import parse_graphgif_file
from algorithms import AlgorithmExecutor
from algorithms.shortest_path import Dijkstra
from models.graph_model import ConcreteGraph, GraphNode, GraphEdge, GraphModel


def create_large_dijkstra_graph(size: int = 100, connectivity: float = 0.3, seed: int = 42) -> ConcreteGraph:
    """
    Create a large weighted directed graph for Dijkstra testing.
    
    Args:
        size: Number of nodes in the graph
        connectivity: Probability of edge existence between any two nodes (0.0 to 1.0)
        seed: Random seed for reproducible graphs
    
    Returns:
        ConcreteGraph: A large weighted directed graph
    """
    random.seed(seed)
    
    graph = ConcreteGraph(name=f"LargeDijkstraGraph_{size}", directed=True)
    
    # Add nodes
    for i in range(size):
        node_id = f"N{i:03d}"
        graph.add_node(node_id)
    
    # Add edges with random weights
    nodes = list(graph.nodes.keys())
    edge_count = 0
    
    for i, source in enumerate(nodes):
        for j, target in enumerate(nodes):
            if i != j and random.random() < connectivity:
                # Generate positive weight between 1 and 20
                weight = random.randint(1, 20)
                graph.add_edge(source, target, {"weight": weight})
                edge_count += 1
    
    # Ensure graph is connected by creating a path through all nodes
    # This guarantees that Dijkstra can reach all nodes from any starting point
    for i in range(size - 1):
        source = f"N{i:03d}"
        target = f"N{(i+1):03d}"
        
        # Check if edge already exists, if not add it
        edge_exists = any(
            edge.source == source and edge.target == target 
            for edge in graph.edges
        )
        
        if not edge_exists:
            weight = random.randint(1, 10)
            graph.add_edge(source, target, {"weight": weight})
            edge_count += 1
    
    print(f"Created large graph with {len(graph.nodes)} nodes and {edge_count} edges")
    print(f"Average degree: {2 * edge_count / len(graph.nodes):.2f}")
    
    return graph


def create_city_network_graph() -> ConcreteGraph:
    """
    Create a realistic city network graph for Dijkstra testing.
    Models a transportation network between cities.
    
    Returns:
        ConcreteGraph: A city network graph with realistic distances
    """
    graph = ConcreteGraph(name="CityNetwork", directed=True)
    
    # Major cities with realistic distances (simplified network)
    cities_and_connections = {
        "NewYork": [("Boston", 215), ("Philadelphia", 95), ("Washington", 225), ("Chicago", 790)],
        "Boston": [("NewYork", 215), ("Montreal", 320), ("Portland", 105)],
        "Philadelphia": [("NewYork", 95), ("Washington", 140), ("Pittsburgh", 305)],
        "Washington": [("NewYork", 225), ("Philadelphia", 140), ("Richmond", 110), ("Atlanta", 440)],
        "Chicago": [("NewYork", 790), ("Detroit", 280), ("Milwaukee", 90), ("StLouis", 300), ("Indianapolis", 185)],
        "Detroit": [("Chicago", 280), ("Toronto", 375), ("Cleveland", 170)],
        "Atlanta": [("Washington", 440), ("Charlotte", 245), ("Nashville", 250), ("Jacksonville", 345)],
        "Miami": [("Jacksonville", 345), ("Tampa", 280), ("Atlanta", 660)],
        "LosAngeles": [("SanDiego", 120), ("LasVegas", 270), ("SanFrancisco", 380), ("Phoenix", 370)],
        "SanFrancisco": [("LosAngeles", 380), ("Portland", 635), ("Sacramento", 90), ("LasVegas", 570)],
        "Seattle": [("Portland", 173), ("Vancouver", 230), ("Spokane", 280)],
        "Denver": [("SaltLakeCity", 525), ("Phoenix", 600), ("KansasCity", 600), ("Chicago", 920)],
        "Dallas": [("Houston", 240), ("Austin", 195), ("OklahomaCity", 205), ("NewOrleans", 345)],
        "Houston": [("Dallas", 240), ("Austin", 165), ("NewOrleans", 350), ("SanAntonio", 200)]
    }
    
    # Add all cities as nodes
    all_cities = set(cities_and_connections.keys())
    for connections in cities_and_connections.values():
        for city, _ in connections:
            all_cities.add(city)
    
    for city in all_cities:
        graph.add_node(city)
    
    # Add connections as weighted edges
    added_edges = set()
    for source_city, connections in cities_and_connections.items():
        for target_city, distance in connections:
            # Avoid duplicate edges
            edge_key = tuple(sorted([source_city, target_city]))
            if edge_key not in added_edges:
                graph.add_edge(source_city, target_city, {"weight": distance})
                graph.add_edge(target_city, source_city, {"weight": distance})  # Bidirectional
                added_edges.add(edge_key)
    
    print(f"Created city network with {len(graph.nodes)} cities and {len(graph.edges)} connections")
    return graph


def test_dijkstra_correctness():
    """Test Dijkstra algorithm correctness on known graphs."""
    print("\n" + "=" * 60)
    print("TESTING DIJKSTRA CORRECTNESS")
    print("=" * 60)
    
    executor = AlgorithmExecutor()
    
    # Test 1: Simple triangle with known shortest path
    print("\n🔺 Test 1: Simple Weighted Triangle")
    print("-" * 40)
    
    triangle = ConcreteGraph(name="WeightedTriangle", directed=True)
    triangle.add_node("A")
    triangle.add_node("B")
    triangle.add_node("C")
    triangle.add_edge("A", "B", {"weight": 4})
    triangle.add_edge("A", "C", {"weight": 2})
    triangle.add_edge("C", "B", {"weight": 1})  # Shorter path A->C->B (cost 3)
    
    # Expected: A->B direct cost 4, A->C->B cost 3
    result = executor.execute_algorithm("dijkstra's algorithm", triangle, start_node="A", target_node="B")
    
    if result.success:
        shortest_path = result.final_result.get("shortest_path", [])
        path_length = result.final_result.get("path_length", None)
        print(f"✅ Path found: {' -> '.join(shortest_path)}")
        print(f"✅ Path length: {path_length}")
        
        # Verify correctness
        expected_path = ["A", "C", "B"]
        expected_length = 3
        
        if shortest_path == expected_path and path_length == expected_length:
            print("✅ CORRECT: Found optimal path A -> C -> B with cost 3")
        else:
            print(f"❌ INCORRECT: Expected path {expected_path} with cost {expected_length}")
    else:
        print(f"❌ Algorithm failed: {result.error_message}")
    
    # Test 2: Disconnected graph
    print("\n🔗 Test 2: Disconnected Graph")
    print("-" * 35)
    
    disconnected = ConcreteGraph(name="Disconnected", directed=True)
    disconnected.add_node("A")
    disconnected.add_node("B")
    disconnected.add_node("C")
    disconnected.add_edge("A", "B", {"weight": 5})
    # C is disconnected
    
    result = executor.execute_algorithm("dijkstra's algorithm", disconnected, start_node="A", target_node="C")
    
    if result.success:
        path_length = result.final_result.get("path_length", None)
        if path_length == float('inf'):
            print("✅ CORRECT: No path to disconnected node (infinite distance)")
        else:
            print(f"❌ INCORRECT: Expected infinite distance, got {path_length}")
    else:
        print(f"❌ Algorithm failed: {result.error_message}")


def test_dijkstra_performance():
    """Test Dijkstra performance on large graphs."""
    print("\n" + "=" * 60)
    print("TESTING DIJKSTRA PERFORMANCE")
    print("=" * 60)
    
    executor = AlgorithmExecutor()
    
    # Test different graph sizes
    test_sizes = [50, 100, 200]
    connectivity_levels = [0.1, 0.3, 0.5]
    
    for size in test_sizes:
        for connectivity in connectivity_levels:
            print(f"\n📊 Testing {size} nodes, {connectivity:.1f} connectivity")
            print("-" * 50)
            
            # Create large graph
            large_graph = create_large_dijkstra_graph(size, connectivity)
            
            # Test execution time
            start_time = time.time()
            result = executor.execute_algorithm("dijkstra's algorithm", large_graph, start_node="N000")
            execution_time = time.time() - start_time
            
            if result.success:
                print(f"✅ Execution time: {execution_time:.4f} seconds")
                print(f"✅ Algorithm steps: {len(result.states)}")
                print(f"✅ Nodes reached: {len([d for d in result.final_result['distances'].values() if d != float('inf')])}")
                
                # Memory usage approximation
                total_states = len(result.states)
                avg_state_size = sum(len(state.visited_nodes) for state in result.states) / total_states if total_states > 0 else 0
                print(f"📊 Avg nodes per state: {avg_state_size:.1f}")
                
                # Performance benchmark
                if execution_time < 1.0:
                    print("🚀 EXCELLENT performance")
                elif execution_time < 5.0:
                    print("✅ GOOD performance")
                else:
                    print("⚠️  SLOW performance")
            else:
                print(f"❌ Algorithm failed: {result.error_message}")


def test_dijkstra_realistic_scenarios():
    """Test Dijkstra on realistic scenarios like city networks."""
    print("\n" + "=" * 60)
    print("TESTING DIJKSTRA REALISTIC SCENARIOS")
    print("=" * 60)
    
    executor = AlgorithmExecutor()
    
    # Test on city network
    print("\n🏙️  City Network Test")
    print("-" * 25)
    
    city_graph = create_city_network_graph()
    
    # Test shortest path from New York to Los Angeles
    print("Finding shortest route: New York → Los Angeles")
    start_time = time.time()
    result = executor.execute_algorithm("dijkstra's algorithm", city_graph, start_node="NewYork", target_node="LosAngeles")
    execution_time = time.time() - start_time
    
    if result.success:
        shortest_path = result.final_result.get("shortest_path", [])
        path_length = result.final_result.get("path_length", None)
        
        print(f"✅ Route found: {' → '.join(shortest_path)}")
        print(f"✅ Total distance: {path_length} miles")
        print(f"✅ Execution time: {execution_time:.4f} seconds")
        print(f"✅ Cities in route: {len(shortest_path)}")
        
        # Test multiple routes
        test_routes = [
            ("Seattle", "Miami"),
            ("SanFrancisco", "NewYork"),
            ("Chicago", "LosAngeles"),
            ("Boston", "Houston")
        ]
        
        print("\n🗺️  Additional Route Tests:")
        for start, end in test_routes:
            route_result = executor.execute_algorithm("dijkstra's algorithm", city_graph, start_node=start, target_node=end)
            if route_result.success:
                route_path = route_result.final_result.get("shortest_path", [])
                route_distance = route_result.final_result.get("path_length", None)
                print(f"  {start} → {end}: {route_distance} miles ({len(route_path)} cities)")
            else:
                print(f"  {start} → {end}: ❌ No route found")
    else:
        print(f"❌ Algorithm failed: {result.error_message}")


def test_dijkstra_edge_cases():
    """Test Dijkstra on edge cases and error conditions."""
    print("\n" + "=" * 60)
    print("TESTING DIJKSTRA EDGE CASES")
    print("=" * 60)
    
    executor = AlgorithmExecutor()
    
    # Test 1: Single node
    print("\n🔵 Test 1: Single Node Graph")
    print("-" * 30)
    
    single = ConcreteGraph(name="SingleNode", directed=True)
    single.add_node("Alone")
    
    result = executor.execute_algorithm("dijkstra's algorithm", single, start_node="Alone", target_node="Alone")
    if result.success:
        path_length = result.final_result.get("path_length", None)
        print(f"✅ Distance to self: {path_length}")
    else:
        print(f"❌ Failed: {result.error_message}")
    
    # Test 2: Negative weights (should fail validation)
    print("\n⚖️  Test 2: Negative Weights")
    print("-" * 30)
    
    negative = ConcreteGraph(name="NegativeWeights", directed=True)
    negative.add_node("A")
    negative.add_node("B")
    negative.add_edge("A", "B", {"weight": -5})
    
    result = executor.execute_algorithm("dijkstra's algorithm", negative, start_node="A")
    if not result.success:
        print(f"✅ Correctly rejected negative weights: {result.error_message}")
    else:
        print("❌ Should have rejected negative weights")
    
    # Test 3: Zero weights
    print("\n0️⃣  Test 3: Zero Weights")
    print("-" * 25)
    
    zero = ConcreteGraph(name="ZeroWeights", directed=True)
    zero.add_node("A")
    zero.add_node("B")
    zero.add_edge("A", "B", {"weight": 0})
    
    result = executor.execute_algorithm("dijkstra's algorithm", zero, start_node="A", target_node="B")
    if result.success:
        path_length = result.final_result.get("path_length", None)
        print(f"✅ Zero weight path length: {path_length}")
    else:
        print(f"❌ Failed with zero weights: {result.error_message}")


def test_dijkstra():
    """Main test function for Dijkstra's algorithm."""
    print("🔍 DIJKSTRA'S ALGORITHM COMPREHENSIVE TESTING")
    print("=" * 60)
    
    try:
        # Test correctness
        test_dijkstra_correctness()
        
        # Test performance
        test_dijkstra_performance()
        
        # Test realistic scenarios
        test_dijkstra_realistic_scenarios()
        
        # Test edge cases
        test_dijkstra_edge_cases()
        
        print("\n" + "=" * 60)
        print("🏁 DIJKSTRA TESTING COMPLETED")
        print("=" * 60)
        print("✅ All Dijkstra tests finished successfully!")
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR during Dijkstra testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_dijkstra()
