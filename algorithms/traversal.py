from .base import GraphAlgorithm, AlgorithmResult, GraphState, ValidationResult, AlgorithmType
from typing import Dict, List, Set
import time


class BFS(GraphAlgorithm):
    """Breadth-First Search algorithm."""

    def __init__(self):
        super().__init__("bfs", AlgorithmType.TRAVERSAL)
        self.min_nodes = 1

    def validate_graph(self, concrete_graph) -> ValidationResult:
        """Validate BFS can be executed."""
        # Basic validation
        basic_result = self._validate_basic_requirements(concrete_graph)
        if not basic_result:
            return basic_result

        # BFS specific validation
        if not concrete_graph.nodes:
            return ValidationResult(False, "Graph has no nodes")

        return ValidationResult(True)

    def execute(self, concrete_graph, start_node: str = None, **kwargs) -> AlgorithmResult:
        """Execute BFS algorithm."""
        start_time = time.time()

        # Validation
        validation = self.validate_graph(concrete_graph)
        if not validation:
            return AlgorithmResult(
                success=False,
                states=[],
                error_message=validation.reason
            )

        # Determine start node
        if start_node is None:
            start_node = next(iter(concrete_graph.nodes.keys()))
        elif start_node not in concrete_graph.nodes:
            return AlgorithmResult(
                success=False,
                states=[],
                error_message=f"Start node '{start_node}' not found in graph"
            )

        # Build adjacency list
        adj_list = {node: [] for node in concrete_graph.nodes}
        for edge in concrete_graph.edges:
            adj_list[edge.source].append(edge.target)
            if not concrete_graph.is_directed:
                adj_list[edge.target].append(edge.source)

        # Execute BFS
        states = []
        visited = set()
        queue = [start_node]
        visit_order = []
        step = 0

        # Initial state
        states.append(GraphState(
            step=step,
            description=f"Initialize BFS from node {start_node}",
            visited_nodes=set(),
            current_node=start_node,
            queue=queue.copy(),
            node_colors={start_node: 'yellow'},
            metadata={'algorithm': 'BFS', 'start_node': start_node}
        ))

        while queue:
            step += 1
            current_node = queue.pop(0)

            if current_node not in visited:
                visited.add(current_node)
                visit_order.append(current_node)

                # Add neighbors to queue
                for neighbor in adj_list[current_node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)

                # Create state
                node_colors = {}
                for node in visited:
                    node_colors[node] = 'green'  # Visited
                if current_node in visited:
                    node_colors[current_node] = 'red'  # Currently processing
                for node in queue:
                    if node not in visited:
                        node_colors[node] = 'yellow'  # In queue

                states.append(GraphState(
                    step=step,
                    description=f"Visit node {current_node}, add neighbors to queue",
                    visited_nodes=visited.copy(),
                    current_node=current_node,
                    queue=queue.copy(),
                    node_colors=node_colors,
                    metadata={'visit_order': visit_order.copy()}
                ))

        # Final state
        step += 1
        states.append(GraphState(
            step=step,
            description="BFS completed",
            visited_nodes=visited.copy(),
            current_node=None,
            queue=[],
            node_colors={node: 'green' for node in visited},
            metadata={'visit_order': visit_order, 'total_visited': len(visited)}
        ))

        execution_time = time.time() - start_time

        return AlgorithmResult(
            success=True,
            states=states,
            final_result={'visit_order': visit_order, 'visited_count': len(visited)},
            execution_time=execution_time
        )


class DFS(GraphAlgorithm):
    """Depth-First Search algorithm."""

    def __init__(self):
        super().__init__("dfs", AlgorithmType.TRAVERSAL)
        self.min_nodes = 1

    def validate_graph(self, concrete_graph) -> ValidationResult:
        """Validate DFS can be executed."""
        basic_result = self._validate_basic_requirements(concrete_graph)
        if not basic_result:
            return basic_result

        if not concrete_graph.nodes:
            return ValidationResult(False, "Graph has no nodes")

        return ValidationResult(True)

    def execute(self, concrete_graph, start_node: str = None, **kwargs) -> AlgorithmResult:
        """Execute DFS algorithm."""
        start_time = time.time()

        validation = self.validate_graph(concrete_graph)
        if not validation:
            return AlgorithmResult(
                success=False,
                states=[],
                error_message=validation.reason
            )

        # Determine start node
        if start_node is None:
            start_node = next(iter(concrete_graph.nodes.keys()))
        elif start_node not in concrete_graph.nodes:
            return AlgorithmResult(
                success=False,
                states=[],
                error_message=f"Start node '{start_node}' not found in graph"
            )

        # Build adjacency list
        adj_list = {node: [] for node in concrete_graph.nodes}
        for edge in concrete_graph.edges:
            adj_list[edge.source].append(edge.target)
            if not concrete_graph.is_directed:
                adj_list[edge.target].append(edge.source)

        # Execute DFS
        states = []
        visited = set()
        stack = [start_node]
        visit_order = []
        step = 0

        # Initial state
        states.append(GraphState(
            step=step,
            description=f"Initialize DFS from node {start_node}",
            visited_nodes=set(),
            current_node=start_node,
            stack=stack.copy(),
            node_colors={start_node: 'yellow'},
            metadata={'algorithm': 'DFS', 'start_node': start_node}
        ))

        while stack:
            step += 1
            current_node = stack.pop()

            if current_node not in visited:
                visited.add(current_node)
                visit_order.append(current_node)

                # Add neighbors to stack (reverse order for consistent behavior)
                neighbors = list(adj_list[current_node])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)

                # Create state
                node_colors = {}
                for node in visited:
                    node_colors[node] = 'green'  # Visited
                if current_node in visited:
                    node_colors[current_node] = 'red'  # Currently processing
                for node in stack:
                    if node not in visited:
                        node_colors[node] = 'yellow'  # In stack

                states.append(GraphState(
                    step=step,
                    description=f"Visit node {current_node}, add neighbors to stack",
                    visited_nodes=visited.copy(),
                    current_node=current_node,
                    stack=stack.copy(),
                    node_colors=node_colors,
                    metadata={'visit_order': visit_order.copy()}
                ))

        # Final state
        step += 1
        states.append(GraphState(
            step=step,
            description="DFS completed",
            visited_nodes=visited.copy(),
            current_node=None,
            stack=[],
            node_colors={node: 'green' for node in visited},
            metadata={'visit_order': visit_order, 'total_visited': len(visited)}
        ))

        execution_time = time.time() - start_time

        return AlgorithmResult(
            success=True,
            states=states,
            final_result={'visit_order': visit_order, 'visited_count': len(visited)},
            execution_time=execution_time
        )