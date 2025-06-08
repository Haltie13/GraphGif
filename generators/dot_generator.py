import os
from parsing.ast_builder import parse_graphgif_file
from models.graph_model import GraphModel, ConcreteGraph

class DOTGenerator:
    def __init__(self):
        self.output_dir = "dot_output"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_dot(self, graphgif_file_path: str) -> None:
        try:
            filename_hint = os.path.splitext(os.path.basename(graphgif_file_path))[0]
            _, graph_model = parse_graphgif_file(graphgif_file_path)
        except Exception as e:
            print(f"Błąd podczas parsowania pliku '{graphgif_file_path}': {e}")
            return

        for graph in graph_model.graphs.values():
            try:
                dot_text = self._generate_graph_dot(graph)
                output_path = os.path.join(self.output_dir, f"{filename_hint}.dot")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(dot_text)
                print(f"Zapisano poprawnie: {output_path}")
            except ValueError as ve:
                print(f"błąd walidacji w grafie '{graph.name}': {ve}")
            except Exception as e:
                print(f"błąd wewnętrzny w grafie '{graph.name}': {e}")

    def _generate_graph_dot(self, concrete_graph: ConcreteGraph) -> str:
        if not concrete_graph.nodes and not concrete_graph.edges:
            raise ValueError(f"Graph '{concrete_graph.name}' is empty and cannot be exported to DOT")

        graph_type = "digraph" if concrete_graph.directed else "graph"
        edge_op = "->" if concrete_graph.directed else "--"

        lines = [f"{graph_type} {concrete_graph.name} {{"]

        if concrete_graph.global_graph_attributes:
            lines.append(f"  graph {self._format_attributes(concrete_graph.global_graph_attributes)};")
        if concrete_graph.global_node_attributes:
            lines.append(f"  node {self._format_attributes(concrete_graph.global_node_attributes)};")
        if concrete_graph.global_edge_attributes:
            lines.append(f"  edge {self._format_attributes(concrete_graph.global_edge_attributes)};")

        for node in concrete_graph.nodes.values():
            merged_attrs = {**concrete_graph.global_node_attributes, **node.attributes}
            attr_str = self._format_attributes(merged_attrs)
            lines.append(f"  {self._escape(node.id)}{attr_str};")

        for edge in concrete_graph.edges:
            if edge.source not in concrete_graph.nodes:
                raise ValueError(f"nieznany węzeł źródłowy '{edge.source}'")
            if edge.target not in concrete_graph.nodes:
                raise ValueError(f"nieznany węzeł docelowy '{edge.target}'")
            merged_attrs = {**concrete_graph.global_edge_attributes, **edge.attributes}
            attr_str = self._format_attributes(merged_attrs)
            lines.append(f"  {self._escape(edge.source)} {edge_op} {self._escape(edge.target)}{attr_str};")

        lines.append("}")
        return "\n".join(lines)

    def _format_attributes(self, attributes: dict) -> str:
        if not attributes:
            return ""
        parts = []
        for key, value in attributes.items():
            try:
                if isinstance(value, str):
                    if value.lower() == "nan":
                        raise ValueError(f"Atrybut '{key}' ma niedozwoloną wartość: {value}")
                    escaped_value = value.replace('"', '\\"')
                    parts.append(f'{key}="{escaped_value}"')
                else:
                    parts.append(f'{key}={value}')
            except Exception as e:
                raise ValueError(f"Błąd formatowania atrybutu '{key}': {e}")
        return " [" + ", ".join(parts) + "]"


    def _escape(self, identifier: str) -> str:
        if not identifier.replace('_', '').isalnum():
            return f'"{identifier}"'
        return identifier
