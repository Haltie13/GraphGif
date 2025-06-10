"""
Concrete graph model for GraphGif.
This module contains classes for representing actual graph structures with resolved nodes and edges.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from models.values import ASTNode


@dataclass
class GraphNode:
    """Represents a concrete node in the graph."""
    id: str
    attributes: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        if self.attributes:
            attrs = ', '.join(f"{k}={v}" for k, v in self.attributes.items())
            return f"{self.id}[{attrs}]"
        return self.id


@dataclass
class GraphEdge:
    """Represents a concrete edge in the graph."""
    source: str
    target: str
    directed: bool = True
    attributes: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        op = "->" if self.directed else "--"
        if self.attributes:
            attrs = ', '.join(f"{k}={v}" for k, v in self.attributes.items())
            return f"{self.source} {op} {self.target}[{attrs}]"
        return f"{self.source} {op} {self.target}"


@dataclass
class ConcreteGraph:
    """Represents a concrete graph with resolved nodes and edges."""
    name: str
    directed: bool
    nodes: Dict[str, GraphNode] = field(default_factory=dict)
    edges: List[GraphEdge] = field(default_factory=list)
    global_node_attributes: Dict[str, Any] = field(default_factory=dict)
    global_edge_attributes: Dict[str, Any] = field(default_factory=dict)
    global_graph_attributes: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def is_directed(self) -> bool:
        """Compatibility property for algorithms that expect is_directed."""
        return self.directed
    
    def add_node(self, node_id: str, attributes: Optional[Dict[str, Any]] = None):
        """Add a node to the graph."""
        # Merge global node attributes with specific attributes
        merged_attrs = self.global_node_attributes.copy()
        if attributes:
            merged_attrs.update(attributes)
        
        if node_id not in self.nodes:
            self.nodes[node_id] = GraphNode(node_id, merged_attrs)
        else:
            # Update existing node attributes
            self.nodes[node_id].attributes.update(merged_attrs)
    
    def add_edge(self, source: str, target: str, attributes: Optional[Dict[str, Any]] = None):
        """Add an edge to the graph."""
        # Ensure source and target nodes exist
        self.add_node(source)
        self.add_node(target)
        
        # Merge global edge attributes with specific attributes
        merged_attrs = self.global_edge_attributes.copy()
        if attributes:
            merged_attrs.update(attributes)
        
        edge = GraphEdge(source, target, self.directed, merged_attrs)
        self.edges.append(edge)
    
    def get_node_list(self) -> List[str]:
        """Get list of all node IDs."""
        return list(self.nodes.keys())
    
    def get_edge_list(self) -> List[tuple]:
        """Get list of all edges as (source, target) tuples."""
        return [(edge.source, edge.target) for edge in self.edges]
    
    def __str__(self):
        result = []
        result.append(f"{'directed' if self.directed else 'undirected'} graph {self.name} {{")
        
        # Global attributes
        if self.global_graph_attributes:
            attrs = ', '.join(f"{k}={v}" for k, v in self.global_graph_attributes.items())
            result.append(f"  graph [{attrs}]")
        if self.global_node_attributes:
            attrs = ', '.join(f"{k}={v}" for k, v in self.global_node_attributes.items())
            result.append(f"  node [{attrs}]")
        if self.global_edge_attributes:
            attrs = ', '.join(f"{k}={v}" for k, v in self.global_edge_attributes.items())
            result.append(f"  edge [{attrs}]")
        
        # Nodes
        for node in self.nodes.values():
            result.append(f"  {node}")
        
        # Edges
        for edge in self.edges:
            result.append(f"  {edge}")
        
        result.append("}")
        return "\n".join(result)


@dataclass
class GraphModel:
    """Container for multiple concrete graphs and variable symbol table."""
    graphs: Dict[str, ConcreteGraph] = field(default_factory=dict)
    variables: Dict[str, Any] = field(default_factory=dict) 
    
    def add_variable(self, name: str, var_type: str, value: Any):
        """Add a variable to the symbol table."""
        self.variables[name] = {
            'type': var_type,
            'value': value
        }
    
    def get_variable(self, name: str) -> Any:
        """Get variable value by name."""
        if name in self.variables:
            return self.variables[name]['value']
        raise ValueError(f"Variable '{name}' not found")
    
    def add_graph(self, graph: ConcreteGraph):
        """Add a graph to the model."""
        self.graphs[graph.name] = graph
    
    def get_graph(self, name: str) -> ConcreteGraph:
        """Get graph by name."""
        if name in self.graphs:
            return self.graphs[name]
        raise ValueError(f"Graph '{name}' not found")
    
    def __str__(self):
        result = []
        result.append("=== Graph Model ===")
        
        if self.variables:
            result.append("\nVariables:")
            for name, var_info in self.variables.items():
                result.append(f"  {var_info['type']} {name} = {var_info['value']}")
        
        if self.graphs:
            result.append("\nGraphs:")
            for graph in self.graphs.values():
                result.append(str(graph))
                result.append("")
        
        return "\n".join(result)
