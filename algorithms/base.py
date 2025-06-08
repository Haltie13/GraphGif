from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Union
from enum import Enum


class AlgorithmType(Enum):
    TRAVERSAL = "traversal"
    SHORTEST_PATH = "shortest_path"
    CONNECTIVITY = "connectivity"
    SPANNING_TREE = "spanning_tree"


class ValidationResult:
    def __init__(self, is_valid: bool, reason: str = ""):
        self.is_valid = is_valid
        self.reason = reason

    def __bool__(self):
        return self.is_valid


@dataclass
class GraphState:
    """Represents a state of the graph during algorithm execution."""
    step: int
    description: str
    visited_nodes: set = None
    current_node: str = None
    distances: Dict[str, float] = None
    parent: Dict[str, str] = None
    queue: List[str] = None
    stack: List[str] = None
    highlighted_edges: List[tuple] = None
    node_colors: Dict[str, str] = None
    edge_colors: Dict[tuple, str] = None
    metadata: Dict[str, Any] = None


@dataclass
class AlgorithmResult:
    """Result of algorithm execution."""
    success: bool
    states: List[GraphState]
    final_result: Any = None  # Algorithm-specific result
    execution_time: float = 0.0
    error_message: str = ""


class GraphAlgorithm(ABC):
    """Abstract base class for all graph algorithms."""

    def __init__(self, name: str, algorithm_type: AlgorithmType):
        self.name = name
        self.algorithm_type = algorithm_type
        self.requires_directed = None  # None = works with both
        self.requires_weighted = False
        self.requires_connected = False
        self.min_nodes = 1
        self.max_nodes = float('inf')

    @abstractmethod
    def validate_graph(self, graph_model) -> ValidationResult:
        """Check if algorithm can be executed on the given graph."""
        pass

    @abstractmethod
    def execute(self, graph_model, **kwargs) -> AlgorithmResult:
        """Execute the algorithm and return states."""
        pass

    def _validate_basic_requirements(self, concrete_graph) -> ValidationResult:
        """Common validation checks."""
        # Check node count
        node_count = len(concrete_graph.nodes)
        if node_count < self.min_nodes:
            return ValidationResult(False, f"Algorithm requires at least {self.min_nodes} nodes, got {node_count}")

        if node_count > self.max_nodes:
            return ValidationResult(False, f"Algorithm supports at most {self.max_nodes} nodes, got {node_count}")

        # Check directedness
        if self.requires_directed is not None:
            if self.requires_directed and not concrete_graph.is_directed:
                return ValidationResult(False, "Algorithm requires directed graph")
            if not self.requires_directed and concrete_graph.is_directed:
                return ValidationResult(False, "Algorithm requires undirected graph")

        # Check if weighted edges are required
        if self.requires_weighted:
            has_weights = any('weight' in edge_attrs for _, _, edge_attrs in concrete_graph.edges)
            if not has_weights:
                return ValidationResult(False, "Algorithm requires weighted edges")

        # Check connectivity if required
        if self.requires_connected:
            if not self._is_connected(concrete_graph):
                return ValidationResult(False, "Algorithm requires connected graph")

        return ValidationResult(True)

    def _is_connected(self, concrete_graph) -> bool:
        """Check if graph is connected."""
        if not concrete_graph.nodes:
            return True

        # Simple BFS to check connectivity
        visited = set()
        start_node = next(iter(concrete_graph.nodes.keys()))
        queue = [start_node]
        visited.add(start_node)

        # Build adjacency list
        adj_list = {node: [] for node in concrete_graph.nodes}
        for source, target, _ in concrete_graph.edges:
            adj_list[source].append(target)
            if not concrete_graph.is_directed:
                adj_list[target].append(source)

        while queue:
            current = queue.pop(0)
            for neighbor in adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == len(concrete_graph.nodes)

    def get_requirements(self) -> Dict[str, Any]:
        """Return algorithm requirements as dictionary."""
        return {
            'name': self.name,
            'type': self.algorithm_type.value,
            'requires_directed': self.requires_directed,
            'requires_weighted': self.requires_weighted,
            'requires_connected': self.requires_connected,
            'min_nodes': self.min_nodes,
            'max_nodes': self.max_nodes if self.max_nodes != float('inf') else None
        }