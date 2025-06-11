"""
Semantic validation for the Graphgif AST.
This module provides validation rules and error checking for the AST.
"""

from typing import List, Dict, Set, Optional, Union
from models import *
from visitors import *

class ValidationError(Exception):
    """Exception raised for validation errors."""
    def __init__(self, message: str, node: Optional[ASTNode] = None):
        self.message = message
        self.node = node
        super().__init__(message)


class SemanticValidator(BaseASTVisitor):
    """Validator that checks semantic correctness of the AST."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.variables = {}  # name -> (type, node)
        self.graphs = {}     # name -> GraphDecl
        self.current_graph_nodes = set()
        self.current_graph_name = None
    
    def add_error(self, message: str, node: Optional[ASTNode] = None):
        """Add a validation error."""
        self.errors.append(ValidationError(message, node))
    
    def add_warning(self, message: str, node: Optional[ASTNode] = None):
        """Add a validation warning."""
        self.warnings.append(ValidationError(message, node))
    
    def visit_program(self, node: Program) -> None:
        """Validate the entire program."""
        self.errors.clear()
        self.warnings.clear()
        self.variables.clear()
        self.graphs.clear()
        
        # First pass: collect variable and graph declarations
        for var_decl in node.variable_declarations:
            self.visit_var_decl(var_decl)
        
        for graph_decl in node.graph_declarations:
            if graph_decl.name in self.graphs:
                self.add_error(f"Duplicate graph name: {graph_decl.name}", graph_decl)
            else:
                self.graphs[graph_decl.name] = graph_decl
        
        # Second pass: validate graph contents
        for graph_decl in node.graph_declarations:
            self.visit_graph_decl(graph_decl)
        
        # Third pass: validate commands
        for command in node.commands:
            self.visit_command(command)
    
    def visit_var_decl(self, node: VarDecl) -> None:
        """Validate variable declaration."""
        if node.name in self.variables:
            self.add_error(f"Duplicate variable name: {node.name}", node)
        else:
            self.variables[node.name] = (node.var_type, node)
        
        # Validate variable value type matches declaration
        self._validate_var_value_type(node.var_type, node.value, node)
    
    def _validate_var_value_type(self, declared_type: VarType, value: VarValue, node: VarDecl):
        """Validate that variable value matches declared type."""
        if declared_type == VarType.NODE:
            if not isinstance(value, (NodeList, NodeVarRef)):
                self.add_error(f"Variable {node.name} declared as 'node' but assigned {type(value).__name__}", node)
        elif declared_type == VarType.EDGE:
            if not isinstance(value, (EdgeList, EdgeVarRef)):
                self.add_error(f"Variable {node.name} declared as 'edge' but assigned {type(value).__name__}", node)
        elif declared_type == VarType.ATTRIBUTES:
            if not isinstance(value, (AttrList, AttrVarRef)):
                self.add_error(f"Variable {node.name} declared as 'attributes' but assigned {type(value).__name__}", node)
    
    def visit_graph_decl(self, node: GraphDecl) -> None:
        """Validate graph declaration."""
        self.current_graph_name = node.name
        self.current_graph_nodes = set()
        
        # Validate global attributes
        for global_attr in node.global_attributes:
            self._validate_attribute_reference(global_attr.attributes, node)
        
        # Collect all nodes declared in this graph
        for statement in node.statements:
            if isinstance(statement, NodeDecl):
                if isinstance(statement.nodes, NodeList):
                    self.current_graph_nodes.update(statement.nodes.nodes)
                elif isinstance(statement.nodes, NodeVarRef):
                    self._validate_node_var_ref(statement.nodes, node)
        
        # Validate statements
        super().visit_graph_decl(node)
        
        self.current_graph_name = None
        self.current_graph_nodes = set()
    
    def visit_node_decl(self, node: NodeDecl) -> None:
        """Validate node declaration."""
        if isinstance(node.nodes, NodeVarRef):
            self._validate_node_var_ref(node.nodes, node)
        
        if node.attributes:
            self._validate_attribute_reference(node.attributes, node)
    
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        """Validate edge declaration."""
        # Check if nodes exist in current graph or are declared elsewhere
        if node.source not in self.current_graph_nodes:
            self.add_warning(f"Edge source '{node.source}' not declared in current graph", node)
        
        if node.target not in self.current_graph_nodes:
            self.add_warning(f"Edge target '{node.target}' not declared in current graph", node)
        
        if node.attributes:
            self._validate_attribute_reference(node.attributes, node)
    
    def visit_command(self, node: Command) -> None:
        """Validate command."""
        if node.graph_name not in self.graphs:
            self.add_error(f"Unknown graph '{node.graph_name}' in command", node)
        
        # Validate argument paths (basic validation)
        for arg in node.arguments:
            if not arg.path.components:
                self.add_error(f"Empty path in argument '{arg.name}'", node)
    
    def _validate_node_var_ref(self, var_ref: NodeVarRef, context_node: ASTNode):
        """Validate node variable reference."""
        if var_ref.name not in self.variables:
            self.add_error(f"Unknown variable '{var_ref.name}'", context_node)
        else:
            var_type, _ = self.variables[var_ref.name]
            if var_type != VarType.NODE:
                self.add_error(f"Variable '{var_ref.name}' is not of type 'node'", context_node)
    
    def _validate_edge_var_ref(self, var_ref: EdgeVarRef, context_node: ASTNode):
        """Validate edge variable reference."""
        if var_ref.name not in self.variables:
            self.add_error(f"Unknown variable '{var_ref.name}'", context_node)
        else:
            var_type, _ = self.variables[var_ref.name]
            if var_type != VarType.EDGE:
                self.add_error(f"Variable '{var_ref.name}' is not of type 'edge'", context_node)
    
    def _validate_attr_var_ref(self, var_ref: AttrVarRef, context_node: ASTNode):
        """Validate attribute variable reference."""
        if var_ref.name not in self.variables:
            self.add_error(f"Unknown variable '{var_ref.name}'", context_node)
        else:
            var_type, _ = self.variables[var_ref.name]
            if var_type != VarType.ATTRIBUTES:
                self.add_error(f"Variable '{var_ref.name}' is not of type 'attributes'", context_node)
    
    def _validate_attribute_reference(self, attr_ref: Union[AttrList, AttrVarRef], context_node: ASTNode):
        """Validate attribute reference."""
        if isinstance(attr_ref, AttrVarRef):
            self._validate_attr_var_ref(attr_ref, context_node)
        elif isinstance(attr_ref, AttrList):
            # Validate individual attributes
            attr_names = set()
            for attr in attr_ref.attributes:
                if attr.key in attr_names:
                    self.add_warning(f"Duplicate attribute '{attr.key}'", context_node)
                attr_names.add(attr.key)
    
    def is_valid(self) -> bool:
        """Check if the AST is valid (no errors)."""
        return len(self.errors) == 0
    
    def get_error_summary(self) -> str:
        """Get a summary of all errors and warnings."""
        summary = []
        
        if self.errors:
            summary.append(f"ERRORS ({len(self.errors)}):")
            for error in self.errors:
                summary.append(f"  - {error.message}")
        
        if self.warnings:
            summary.append(f"WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                summary.append(f"  - {warning.message}")
        
        if not self.errors and not self.warnings:
            summary.append("No errors or warnings found.")
        
        return "\n".join(summary)


class GraphAnalyzer(BaseASTVisitor):
    """Analyzer that extracts graph structure information."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.graphs = {}
        self.current_graph = None
    
    def visit_program(self, node: Program) -> None:
        """Analyze all graphs in the program."""
        self.reset()
        super().visit_program(node)
    
    def visit_graph_decl(self, node: GraphDecl) -> None:
        """Analyze graph declaration."""
        self.current_graph = {
            'name': node.name,
            'direction': node.direction,
            'nodes': set(),
            'edges': [],
            'global_attributes': {},
            'node_attributes': {},
            'edge_attributes': {}
        }
        
        # Process global attributes
        for global_attr in node.global_attributes:
            if isinstance(global_attr.attributes, AttrList):
                attrs = {attr.key: attr.value.value for attr in global_attr.attributes.attributes}
                self.current_graph['global_attributes'][global_attr.attr_type.value] = attrs
        
        super().visit_graph_decl(node)
        
        self.graphs[node.name] = self.current_graph
        self.current_graph = None
    
    def visit_node_decl(self, node: NodeDecl) -> None:
        """Analyze node declaration."""
        if isinstance(node.nodes, NodeList):
            nodes = node.nodes.nodes
            self.current_graph['nodes'].update(nodes)
            
            if node.attributes and isinstance(node.attributes, AttrList):
                attrs = {attr.key: attr.value.value for attr in node.attributes.attributes}
                for node_name in nodes:
                    self.current_graph['node_attributes'][node_name] = attrs
    
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        """Analyze edge declaration."""
        edge_info = {
            'source': node.source,
            'target': node.target,
            'operator': node.operator.value,
            'attributes': {}
        }
        
        if node.attributes and isinstance(node.attributes, AttrList):
            edge_info['attributes'] = {attr.key: attr.value.value for attr in node.attributes.attributes}
        
        self.current_graph['edges'].append(edge_info)
        self.current_graph['nodes'].add(node.source)
        self.current_graph['nodes'].add(node.target)
    
    def get_graph_info(self, graph_name: str) -> Optional[dict]:
        """Get information about a specific graph."""
        return self.graphs.get(graph_name)
    
    def get_all_graphs(self) -> Dict[str, dict]:
        """Get information about all graphs."""
        return self.graphs.copy()
    
    def is_connected(self, graph_name: str) -> bool:
        """Check if a graph is connected (simplified check)."""
        graph = self.get_graph_info(graph_name)
        if not graph:
            return False
        
        nodes = graph['nodes']
        edges = graph['edges']
        
        if len(nodes) <= 1:
            return True
        
        # Build adjacency list
        adj = {node: set() for node in nodes}
        for edge in edges:
            adj[edge['source']].add(edge['target'])
            if graph['direction'] == GraphDirection.UNDIRECTED or edge['operator'] == '--':
                adj[edge['target']].add(edge['source'])
        
        # BFS to check connectivity
        if not nodes:
            return True
        
        start_node = next(iter(nodes))
        visited = set()
        queue = [start_node]
        visited.add(start_node)
        
        while queue:
            node = queue.pop(0)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == len(nodes)


def validate_ast(ast: Program) -> SemanticValidator:
    """Validate an AST and return the validator with results."""
    validator = SemanticValidator()
    validator.visit_program(ast)
    return validator


def analyze_graphs(ast: Program) -> GraphAnalyzer:
    """Analyze graph structure in an AST."""
    analyzer = GraphAnalyzer()
    analyzer.visit_program(ast)
    return analyzer


# Example usage
if __name__ == "__main__":
    from example_usage import create_example_ast
    
    # Create and validate example AST
    ast = create_example_ast()
    
    # Validate
    validator = validate_ast(ast)
    print("Validation Results:")
    print("=" * 50)
    print(validator.get_error_summary())
    
    # Analyze
    analyzer = analyze_graphs(ast)
    print("\nGraph Analysis:")
    print("=" * 50)
    for graph_name, graph_info in analyzer.get_all_graphs().items():
        print(f"Graph '{graph_name}':")
        print(f"  Direction: {graph_info['direction'].value}")
        print(f"  Nodes: {sorted(graph_info['nodes'])}")
        print(f"  Edges: {len(graph_info['edges'])}")
        print(f"  Connected: {analyzer.is_connected(graph_name)}")
        if graph_info['global_attributes']:
            print(f"  Global attributes: {graph_info['global_attributes']}")
        print()
