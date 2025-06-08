from typing import Dict, List, Type
from .base import GraphAlgorithm, AlgorithmResult
from .traversal import BFS, DFS
from .shortest_path import Dijkstra

class AlgorithmExecutor:
    """Manages and executes graph algorithms."""

    def __init__(self):
        self.algorithms: Dict[str, GraphAlgorithm] = {}
        self._register_default_algorithms()

    def _register_default_algorithms(self):
        """Register built-in algorithms."""
        self.register_algorithm(BFS())
        self.register_algorithm(DFS())
        self.register_algorithm(Dijkstra())

    def register_algorithm(self, algorithm: GraphAlgorithm):
        """Register a new algorithm."""
        self.algorithms[algorithm.name.lower()] = algorithm

    def get_available_algorithms(self) -> List[str]:
        """Get list of available algorithm names."""
        return list(self.algorithms.keys())

    def get_algorithm_info(self, algorithm_name: str) -> Dict:
        """Get information about an algorithm."""
        algorithm = self.algorithms.get(algorithm_name.lower())
        if not algorithm:
            return {}
        return algorithm.get_requirements()

    def validate_algorithm_for_graph(self, algorithm_name: str, graph_model) -> Dict:
        """Check if algorithm can run on graph."""
        algorithm = self.algorithms.get(algorithm_name.lower())
        if not algorithm:
            return {
                'valid': False,
                'reason': f"Algorithm '{algorithm_name}' not found"
            }

        validation = algorithm.validate_graph(graph_model)
        return {
            'valid': validation.is_valid,
            'reason': validation.reason
        }

    def execute_algorithm(self, algorithm_name: str, graph_model, **kwargs) -> AlgorithmResult:
        """Execute an algorithm on a graph."""
        algorithm = self.algorithms.get(algorithm_name.lower())
        if not algorithm:
            return AlgorithmResult(
                success=False,
                states=[],
                error_message=f"Algorithm '{algorithm_name}' not found"
            )

        return algorithm.execute(graph_model, **kwargs)

    def get_algorithms_for_graph(self, graph_model) -> Dict[str, Dict]:
        """Get all algorithms that can run on this graph."""
        results = {}
        for name, algorithm in self.algorithms.items():
            validation = algorithm.validate_graph(graph_model)
            results[name] = {
                'name': algorithm.name,
                'type': algorithm.algorithm_type.value,
                'valid': validation.is_valid,
                'reason': validation.reason if not validation.is_valid else "",
                'requirements': algorithm.get_requirements()
            }
        return results