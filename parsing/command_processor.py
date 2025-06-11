"""
Command processor for executing algorithms on graphs in GraphGIF.
This module handles the execution of run commands with proper error handling.
"""

from typing import Dict, Any, Optional, List
from algorithms.executor import AlgorithmExecutor
from algorithms.base import AlgorithmResult
from models.graph_model import ConcreteGraph
from errors.exceptions import GraphgifError


class CommandProcessor:
    """Processes and executes GraphGIF commands."""
    
    def __init__(self):
        self.algorithm_executor = AlgorithmExecutor()
        # Map command names to algorithm names
        self.algorithm_name_mapping = {
            'bfs': 'breadth-first search',
            'breadth-first': 'breadth-first search',
            'breadth-first-search': 'breadth-first search',
            'dfs': 'depth-first search', 
            'depth-first': 'depth-first search',
            'depth-first-search': 'depth-first search',
            'dijkstra': "dijkstra's algorithm",
            'dijkstras': "dijkstra's algorithm",
            'dijkstra-algorithm': "dijkstra's algorithm",
            'shortest-path': "dijkstra's algorithm"
        }
    
    def execute_command(self, command_name: str, graph: ConcreteGraph, 
                       arguments: Dict[str, Any]) -> AlgorithmResult:
        """
        Execute a command on a graph with given arguments.
        
        Args:
            command_name: Name of the algorithm/command to execute
            graph: The concrete graph to operate on
            arguments: Command arguments (start_node, target_node, etc.)
            
        Returns:
            AlgorithmResult with execution results or error information
        """
        try:
            # Normalize command name
            normalized_name = command_name.lower().replace('_', '-')
            algorithm_name = self.algorithm_name_mapping.get(normalized_name, normalized_name)
            
            # Validate algorithm exists
            available_algorithms = self.algorithm_executor.get_available_algorithms()
            if algorithm_name not in available_algorithms:
                return AlgorithmResult(
                    success=False,
                    states=[],
                    error_message=f"Unknown algorithm '{command_name}'. Available algorithms: {', '.join(available_algorithms)}"
                )
            
            # Validate algorithm can run on this graph
            validation = self.algorithm_executor.validate_algorithm_for_graph(algorithm_name, graph)
            if not validation['valid']:
                return AlgorithmResult(
                    success=False,
                    states=[],
                    error_message=f"Algorithm '{command_name}' cannot run on this graph: {validation['reason']}"
                )
            
            # Process algorithm-specific arguments
            processed_args = self._process_algorithm_arguments(algorithm_name, arguments, graph)
            
            # Execute the algorithm
            result = self.algorithm_executor.execute_algorithm(algorithm_name, graph, **processed_args)
            
            return result
            
        except Exception as e:
            return AlgorithmResult(
                success=False,
                states=[],
                error_message=f"Error executing command '{command_name}': {str(e)}"
            )
    
    def _process_algorithm_arguments(self, algorithm_name: str, arguments: Dict[str, Any], 
                                   graph: ConcreteGraph) -> Dict[str, Any]:
        """
        Process and validate algorithm-specific arguments.
        
        Args:
            algorithm_name: Name of the algorithm
            arguments: Raw command arguments
            graph: The graph being operated on
            
        Returns:
            Processed arguments ready for algorithm execution
        """
        processed = {}
        
        # Common argument processing
        if 'start' in arguments or 'from' in arguments:
            start_node = arguments.get('start') or arguments.get('from')
            if start_node not in graph.nodes:
                raise GraphgifError(f"Start node '{start_node}' not found in graph")
            processed['start_node'] = start_node
        
        if 'target' in arguments or 'to' in arguments:
            target_node = arguments.get('target') or arguments.get('to')
            if target_node not in graph.nodes:
                raise GraphgifError(f"Target node '{target_node}' not found in graph")
            processed['target_node'] = target_node
        
        # Algorithm-specific argument processing
        if algorithm_name == "dijkstra's algorithm":
            # Dijkstra requires start_node, optionally target_node
            if 'start_node' not in processed:
                # Use first node as default start
                processed['start_node'] = next(iter(graph.nodes.keys()))
        
        elif algorithm_name in ['breadth-first search', 'depth-first search']:
            # Traversal algorithms require start_node
            if 'start_node' not in processed:
                # Use first node as default start
                processed['start_node'] = next(iter(graph.nodes.keys()))
        
        # Copy other arguments as-is
        for key, value in arguments.items():
            if key not in ['start', 'from', 'target', 'to']:
                processed[key] = value
        
        return processed
    
    def get_available_algorithms(self) -> List[str]:
        """Get list of available algorithm names."""
        return list(self.algorithm_name_mapping.keys()) + self.algorithm_executor.get_available_algorithms()
    
    def get_algorithm_info(self, command_name: str) -> Dict[str, Any]:
        """Get information about an algorithm."""
        normalized_name = command_name.lower().replace('_', '-')
        algorithm_name = self.algorithm_name_mapping.get(normalized_name, normalized_name)
        return self.algorithm_executor.get_algorithm_info(algorithm_name)
