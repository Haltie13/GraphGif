"""
Example usage of the Graphgif AST model.
This file demonstrates how to construct and work with the AST nodes.
"""

from graphgif_model import *


def create_example_ast() -> Program:
    """Create an example AST representing a simple Graphgif program."""
    
    # Variable declarations
    # var node myNodes = A, B, C;
    node_list = NodeList(["A", "B", "C"])
    var_decl = ASTFactory.create_var_decl("node", "myNodes", node_list)
    
    # var attributes defaultAttrs = [color="red", size=10];
    color_attr = ASTFactory.create_attribute("color", "=", ASTFactory.create_value("red", "STRING"))
    size_attr = ASTFactory.create_attribute("size", "=", ASTFactory.create_value(10, "NUMBER"))
    attr_list = AttrList([color_attr, size_attr])
    attr_var_decl = ASTFactory.create_var_decl("attributes", "defaultAttrs", attr_list)
    
    # Graph declaration
    # directed graph myGraph {
    #     node [shape="circle"];
    #     A, B, C [color="blue"];
    #     A -> B [weight=5];
    #     B -> C;
    # }
    
    # Global attribute: node [shape="circle"]
    shape_attr = ASTFactory.create_attribute("shape", "=", ASTFactory.create_value("circle", "STRING"))
    global_node_attrs = AttrList([shape_attr])
    global_attr_decl = GlobalAttrDecl(GlobalAttrType.NODE, global_node_attrs)
    
    # Node declaration: A, B, C [color="blue"]
    nodes = NodeList(["A", "B", "C"])
    blue_attr = ASTFactory.create_attribute("color", "=", ASTFactory.create_value("blue", "STRING"))
    node_attrs = AttrList([blue_attr])
    node_decl = NodeDecl(nodes, node_attrs)
    
    # Edge declarations
    weight_attr = ASTFactory.create_attribute("weight", "=", ASTFactory.create_value(5, "NUMBER"))
    edge_attrs = AttrList([weight_attr])
    edge1 = ASTFactory.create_edge_decl("A", "->", "B", edge_attrs)
    edge2 = ASTFactory.create_edge_decl("B", "->", "C")
    
    # Create graph
    graph_decl = ASTFactory.create_graph_decl(
        "directed", 
        "myGraph", 
        [global_attr_decl],
        [node_decl, edge1, edge2]
    )
    
    # Command: run myGraph with (output="result.png");
    output_path = Path(["result.png"])
    output_arg = Argument("output", AttributeOperator.EQUALS, output_path)
    command = Command("myGraph", [output_arg])
    
    # Create program
    program = Program(
        variable_declarations=[var_decl, attr_var_decl],
        graph_declarations=[graph_decl],
        commands=[command]
    )
    
    return program


class GraphgifPrettyPrinter(BaseASTVisitor):
    """A visitor that generates a readable representation of the AST."""
    
    def __init__(self):
        self.output = []
        self.indent_level = 0
    
    def indent(self):
        return "  " * self.indent_level
    
    def visit_program(self, node: Program) -> None:
        self.output.append("=== GRAPHGIF PROGRAM ===\n")
        
        if node.variable_declarations:
            self.output.append("Variables:\n")
            self.indent_level += 1
            for var_decl in node.variable_declarations:
                self.visit_var_decl(var_decl)
            self.indent_level -= 1
            self.output.append("\n")
        
        if node.graph_declarations:
            self.output.append("Graphs:\n")
            self.indent_level += 1
            for graph_decl in node.graph_declarations:
                self.visit_graph_decl(graph_decl)
            self.indent_level -= 1
            self.output.append("\n")
        
        if node.commands:
            self.output.append("Commands:\n")
            self.indent_level += 1
            for command in node.commands:
                self.visit_command(command)
            self.indent_level -= 1
    
    def visit_var_decl(self, node: VarDecl) -> None:
        self.output.append(f"{self.indent()}{node.var_type.value} {node.name} = ")
        if isinstance(node.value, NodeList):
            self.output.append(f"[{', '.join(node.value.nodes)}]\n")
        elif isinstance(node.value, AttrList):
            self.visit_attr_list(node.value)
            self.output.append("\n")
        elif isinstance(node.value, EdgeList):
            self.output.append("edge_list\n")
        else:
            self.output.append(f"${node.value.name}\n")
    
    def visit_graph_decl(self, node: GraphDecl) -> None:
        self.output.append(f"{self.indent()}{node.direction.value} graph {node.name} {{\n")
        self.indent_level += 1
        
        for global_attr in node.global_attributes:
            self.output.append(f"{self.indent()}{global_attr.attr_type.value} ")
            if isinstance(global_attr.attributes, AttrList):
                self.visit_attr_list(global_attr.attributes)
            else:
                self.output.append(f"${global_attr.attributes.name}")
            self.output.append("\n")
        
        for statement in node.statements:
            if isinstance(statement, NodeDecl):
                self.visit_node_decl(statement)
            elif isinstance(statement, EdgeDecl):
                self.visit_edge_decl(statement)
        
        self.indent_level -= 1
        self.output.append(f"{self.indent()}}}\n")
    
    def visit_node_decl(self, node: NodeDecl) -> None:
        self.output.append(f"{self.indent()}")
        if isinstance(node.nodes, NodeList):
            self.output.append(f"{', '.join(node.nodes.nodes)}")
        else:
            self.output.append(f"${node.nodes.name}")
        
        if node.attributes:
            self.output.append(" ")
            if isinstance(node.attributes, AttrList):
                self.visit_attr_list(node.attributes)
            else:
                self.output.append(f"${node.attributes.name}")
        self.output.append("\n")
    
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        self.output.append(f"{self.indent()}{node.source} {node.operator.value} {node.target}")
        if node.attributes:
            self.output.append(" ")
            if isinstance(node.attributes, AttrList):
                self.visit_attr_list(node.attributes)
            else:
                self.output.append(f"${node.attributes.name}")
        self.output.append("\n")
    
    def visit_command(self, node: Command) -> None:
        self.output.append(f"{self.indent()}run {node.graph_name} with (")
        for i, arg in enumerate(node.arguments):
            if i > 0:
                self.output.append(", ")
            self.output.append(f"{arg.name}{arg.operator.value}{'.'.join(arg.path.components)}")
        self.output.append(")\n")
    
    def visit_attr_list(self, node: AttrList) -> None:
        self.output.append("[")
        for i, attr in enumerate(node.attributes):
            if i > 0:
                self.output.append(", ")
            value_str = f'"{attr.value.value}"' if attr.value.value_type == "STRING" else str(attr.value.value)
            self.output.append(f"{attr.key}{attr.operator.value}{value_str}")
        self.output.append("]")
    
    def visit_node_list(self, node: NodeList) -> None:
        pass  # Handled in parent methods
    
    def get_output(self) -> str:
        return "".join(self.output)


class GraphStatisticsVisitor(BaseASTVisitor):
    """A visitor that collects statistics about the graph structure."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.node_count = 0
        self.edge_count = 0
        self.graph_count = 0
        self.variable_count = 0
        self.command_count = 0
        self.nodes = set()
        self.edges = []
    
    def visit_program(self, node: Program) -> None:
        self.reset()
        super().visit_program(node)
    
    def visit_var_decl(self, node: VarDecl) -> None:
        self.variable_count += 1
        super().visit_var_decl(node)
    
    def visit_graph_decl(self, node: GraphDecl) -> None:
        self.graph_count += 1
        super().visit_graph_decl(node)
    
    def visit_node_decl(self, node: NodeDecl) -> None:
        if isinstance(node.nodes, NodeList):
            self.nodes.update(node.nodes.nodes)
        super().visit_node_decl(node)
    
    def visit_edge_decl(self, node: EdgeDecl) -> None:
        self.edge_count += 1
        self.edges.append((node.source, node.target))
        self.nodes.add(node.source)
        self.nodes.add(node.target)
        super().visit_edge_decl(node)
    
    def visit_command(self, node: Command) -> None:
        self.command_count += 1
        super().visit_command(node)
    
    def visit_node_list(self, node: NodeList) -> None:
        self.nodes.update(node.nodes)
    
    def get_statistics(self) -> dict:
        return {
            "total_nodes": len(self.nodes),
            "total_edges": self.edge_count,
            "total_graphs": self.graph_count,
            "total_variables": self.variable_count,
            "total_commands": self.command_count,
            "node_list": sorted(list(self.nodes)),
            "edge_list": self.edges
        }


def main():
    """Example usage of the Graphgif AST model."""
    
    # Create an example AST
    program = create_example_ast()
    
    # Pretty print the AST
    printer = GraphgifPrettyPrinter()
    printer.visit_program(program)
    print("Generated Graphgif Code:")
    print("=" * 50)
    print(printer.get_output())
    
    # Collect statistics
    stats_visitor = GraphStatisticsVisitor()
    stats_visitor.visit_program(program)
    stats = stats_visitor.get_statistics()
    
    print("\nProgram Statistics:")
    print("=" * 50)
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
