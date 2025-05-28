"""
Main entry point for GraphGif language processing.
This module demonstrates the complete workflow of parsing, analyzing, and working with GraphGif code.
"""

from models import *
from parsing import parse_graphgif, parse_graphgif_file
from visitors import GraphgifPrettyPrinter, GraphStatisticsVisitor


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
    
    # Command
    # run myGraph with (output="result.png");
    path = Path(["result.png"])
    arg = Argument("output", AttributeOperator.EQUALS, path)
    command = Command("myGraph", [arg])
    
    # Create program
    program = Program(
        [var_decl, attr_var_decl],
        [graph_decl],
        [command]
    )
    
    return program


def test_parsing():
    """Test parsing functionality with example code."""
    
    test_code = """
    var node myNodes = A, B, C;
    var attributes defaultAttrs = [color='red', size=10];
    
    directed graph testGraph {
        node [shape='circle'];
        A, B, C [color='blue'];
        A -> B [weight=5];
        B -> C;
    }
    
    run testGraph with (output='result.png');
    """
    
    print("Testing GraphGif Parser")
    print("=" * 50)
    
    try:
        # Parse the code
        ast = parse_graphgif(test_code)
        
        # Pretty print the result
        printer = GraphgifPrettyPrinter()
        printer.visit_program(ast)
        print("Parsed AST:")
        print("-" * 30)
        print(printer.get_output())
        
        # Show statistics
        stats_visitor = GraphStatisticsVisitor()
        stats_visitor.visit_program(ast)
        stats = stats_visitor.get_statistics()
        
        print("\nStatistics:")
        print("-" * 30)
        for key, value in stats.items():
            print(f"{key}: {value}")
            
        return ast
        
    except Exception as e:
        print(f"Error parsing code: {e}")
        return None


def test_ast_creation():
    """Test AST creation and manipulation."""
    
    print("\nTesting AST Creation")
    print("=" * 50)
    
    # Create an example AST programmatically
    program = create_example_ast()
    
    # Pretty print the AST
    printer = GraphgifPrettyPrinter()
    printer.visit_program(program)
    print("Generated AST:")
    print("-" * 30)
    print(printer.get_output())
    
    # Collect statistics
    stats_visitor = GraphStatisticsVisitor()
    stats_visitor.visit_program(program)
    stats = stats_visitor.get_statistics()
    
    print("\nProgram Statistics:")
    print("-" * 30)
    for key, value in stats.items():
        print(f"{key}: {value}")


def main():
    """Main demonstration function."""
    print("GraphGif Language Processor")
    print("=" * 60)
    
    # Test AST creation
    test_ast_creation()
    
    # Test parsing
    test_parsing()
    
    print("\nDemonstration completed successfully!")


if __name__ == "__main__":
    main()
