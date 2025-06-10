from .base import GraphAlgorithm, AlgorithmResult, GraphState, ValidationResult, AlgorithmType
import heapq
import time


class Dijkstra(GraphAlgorithm):
    """Dijkstra's shortest path algorithm."""

    def __init__(self):
        super().__init__("Dijkstra's Algorithm", AlgorithmType.SHORTEST_PATH)
        self.requires_weighted = True
        self.min_nodes = 2

    def validate_graph(self, concrete_graph) -> ValidationResult:
        """Validate Dijkstra can be executed."""
        # Basic validation
        basic_result = self._validate_basic_requirements(concrete_graph)
        if not basic_result:
            return basic_result

        # Check for negative weights
        for edge in concrete_graph.edges:
            weight = edge.attributes.get('weight', 1)
            try:
                weight = float(weight)
                if weight < 0:
                    return ValidationResult(False, f"Negative weight found on edge {edge.source}->{edge.target}: {weight}")
            except (ValueError, TypeError):
                return ValidationResult(False, f"Invalid weight on edge {edge.source}->{edge.target}: {weight}")

        return ValidationResult(True)

    def execute(self, concrete_graph, start_node: str = None, target_node: str = None,
                **kwargs) -> AlgorithmResult:
        """Execute Dijkstra's algorithm."""
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

        # Validate target node if specified
        if target_node and target_node not in concrete_graph.nodes:
            return AlgorithmResult(
                success=False,
                states=[],
                error_message=f"Target node '{target_node}' not found in graph"
            )

        # Build adjacency list with weights
        adj_list = {node: [] for node in concrete_graph.nodes}
        for edge in concrete_graph.edges:
            weight = float(edge.attributes.get('weight', 1))
            adj_list[edge.source].append((edge.target, weight))
            if not concrete_graph.is_directed:
                adj_list[edge.target].append((edge.source, weight))

        # Execute Dijkstra
        states = []
        # Note: Dijkstra requires positive infinity for unvisited nodes
        # to correctly identify shortest paths. Negative infinity would break the algorithm.
        distances = {node: float('inf') for node in concrete_graph.nodes}
        distances[start_node] = 0
        parent = {node: None for node in concrete_graph.nodes}
        visited = set()
        priority_queue = [(0, start_node)]
        step = 0

        # Initial state
        states.append(GraphState(
            step=step,
            description=f"Initialize Dijkstra from node {start_node}",
            visited_nodes=set(),
            current_node=start_node,
            distances=distances.copy(),
            parent=parent.copy(),
            node_colors={start_node: 'yellow'},
            metadata={
                'algorithm': 'Dijkstra',
                'start_node': start_node,
                'target_node': target_node,
                'priority_queue': priority_queue.copy()
            }
        ))

        while priority_queue:
            step += 1
            current_dist, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            # If we found target, we can stop (optional optimization)
            if target_node and current_node == target_node:
                break

            # Update distances to neighbors
            updated_edges = []
            for neighbor, weight in adj_list[current_node]:
                if neighbor not in visited:
                    new_dist = distances[current_node] + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        parent[neighbor] = current_node
                        heapq.heappush(priority_queue, (new_dist, neighbor))
                        updated_edges.append((current_node, neighbor))

            # Create state
            node_colors = {}
            for node in visited:
                node_colors[node] = 'green'  # Visited
            node_colors[current_node] = 'red'  # Currently processing

            # Color nodes in priority queue
            queue_nodes = {node for _, node in priority_queue if node not in visited}
            for node in queue_nodes:
                node_colors[node] = 'yellow'  # In queue

            edge_colors = {}
            for edge in updated_edges:
                edge_colors[edge] = 'red'  # Updated edges

            states.append(GraphState(
                step=step,
                description=f"Process node {current_node} (distance: {current_dist})",
                visited_nodes=visited.copy(),
                current_node=current_node,
                distances=distances.copy(),
                parent=parent.copy(),
                node_colors=node_colors,
                edge_colors=edge_colors,
                highlighted_edges=updated_edges,
                metadata={
                    'priority_queue': [(d, n) for d, n in priority_queue if n not in visited]
                }
            ))

        # Build path if target specified
        final_path = []
        if target_node and distances[target_node] != float('inf'):
            current = target_node
            while current is not None:
                final_path.insert(0, current)
                current = parent[current]

        # Final state
        step += 1
        final_node_colors = {node: 'green' for node in visited}
        if target_node and final_path:
            for node in final_path:
                final_node_colors[node] = 'blue'  # Path nodes

        states.append(GraphState(
            step=step,
            description="Dijkstra completed",
            visited_nodes=visited.copy(),
            current_node=None,
            distances=distances.copy(),
            parent=parent.copy(),
            node_colors=final_node_colors,
            metadata={
                'shortest_path': final_path,
                'path_length': distances[target_node] if target_node else None,
                'all_distances': distances
            }
        ))

        execution_time = time.time() - start_time

        return AlgorithmResult(
            success=True,
            states=states,
            final_result={
                'distances': distances,
                'shortest_path': final_path if target_node else None,
                'path_length': distances[target_node] if target_node and target_node in distances else None
            },
            execution_time=execution_time
        )