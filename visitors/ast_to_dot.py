from models.ast_nodes import Program, GraphDecl
from models.statements import NodeDecl
from models.expressions import EdgeDecl, AttrList
from models.values import GraphDirection, Attribute, AttributeOperator
from typing import Dict


def ast_to_dot(ast: Program) -> Dict[str, str]:
   
    result = {}

    for graph in ast.graph_declarations:
        is_directed = graph.direction == GraphDirection.DIRECTED
        edge_op = '->' if is_directed else '--'

        lines = [f"{'digraph' if is_directed else 'graph'} {graph.name} {{"]
        
        for global_attr in graph.global_attributes:
            if isinstance(global_attr.attributes, AttrList):
                attr_str = _format_attributes(global_attr.attributes.attributes)
                lines.append(f"  {global_attr.attr_type.value} [{attr_str}];")
        
        for stmt in graph.statements:
            if isinstance(stmt, NodeDecl):
                node_ids = _get_node_ids(stmt.nodes)
                attr_str = ""
                if isinstance(stmt.attributes, AttrList):
                    attr_str = f" [{_format_attributes(stmt.attributes.attributes)}]"
                lines.append(f"  {', '.join(node_ids)}{attr_str};")
            elif isinstance(stmt, EdgeDecl):
                attr_str = ""
                if isinstance(stmt.attributes, AttrList):
                    attr_str = f" [{_format_attributes(stmt.attributes.attributes)}]"
                lines.append(f"  {stmt.source} {edge_op} {stmt.target}{attr_str};")
        
        lines.append("}")
        result[graph.name] = "\n".join(lines)

    return result


def _format_attributes(attributes: list[Attribute]) -> str:
    return ", ".join(
        f'{attr.key}="{attr.value.value}"'
        for attr in attributes
        if hasattr(attr.value, 'value')
    )


def _get_node_ids(nodes_expr) -> list[str]:
    if hasattr(nodes_expr, "nodes"):
        return nodes_expr.nodes 
    elif hasattr(nodes_expr, "name"):
        return [f"${nodes_expr.name}"]  
    return []
