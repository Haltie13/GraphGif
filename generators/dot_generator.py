from models.graph_model import GraphModel, ConcreteGraph, GraphNode, GraphEdge

class DOTGenerator:
    def __init__(self):
        self.output = []

    def generate_dot(self, graph_model: GraphModel) -> dict[str, str]:
        result = {}
        for graph in graph_model.graphs.values():
            self.output = []
            self.generate_graph_dot(graph)
            result[graph.name] = "\n".join(self.output)
        return result


    def generate_graph_dot(self, concrete_graph: ConcreteGraph) -> None:
        lines = []
        graph_type = "digraph" if concrete_graph.directed else "graph"
        edge_op = "->" if concrete_graph.directed else "--"

        lines.append(f"{graph_type} {concrete_graph.name} {{")

        if concrete_graph.global_graph_attributes:
            lines.append(f"  graph [{self._format_attributes(concrete_graph.global_graph_attributes)}];")
        if concrete_graph.global_node_attributes:
            lines.append(f"  node [{self._format_attributes(concrete_graph.global_node_attributes)}];")
        if concrete_graph.global_edge_attributes:
            lines.append(f"  edge [{self._format_attributes(concrete_graph.global_edge_attributes)}];")

        for node in concrete_graph.nodes.values():
            attr_str = self._format_attributes(node.attributes)
            lines.append(f"  {self._escape(node.id)}{attr_str};")

        for edge in concrete_graph.edges:
            attr_str = self._format_attributes(edge.attributes)
            lines.append(f"  {self._escape(edge.source)} {edge_op} {self._escape(edge.target)}{attr_str};")

        lines.append("}")
        self.output.append("\n".join(lines))

    def _format_attributes(self, attributes: dict) -> str:
        if not attributes:
            return ""
        parts = []
        for key, value in attributes.items():
            if isinstance(value, str):
                escaped_value = value.replace('"', '\\"')
                parts.append(f'{key}="{escaped_value}"')
            else:
                parts.append(f'{key}={value}')
        return " [" + ", ".join(parts) + "]"

    def _escape(self, identifier: str) -> str:
        if not identifier.replace('_', '').isalnum():
            return f'"{identifier}"'
        return identifier
