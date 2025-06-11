"""
Test command executor functionality.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parsing.ast_builder import parse_graphgif_file
from parsing.command_executor import CommandExecutor


def test_command_execution():
    """Test automatic command execution from parsed files."""
    print("Testing command execution...")
    
    # Test with large_dijkstra.gg which has a command
    try:
        ast, graph_model, execution_results = parse_graphgif_file('./examples/large_dijkstra.gg', 'test_output')
        
        print("Parsing completed successfully")
        print(f"Found {len(graph_model.graphs)} graphs")
        print(f"Found {len(ast.commands)} commands")
        
        if execution_results:
            print("\nCommand execution results:")
            for graph_name, result in execution_results.items():
                print(f"Graph: {graph_name}")
                print(f"Algorithm: {result['algorithm']}")
                print(f"Success: {result['result'].success}")
                print(f"Steps: {len(result['result'].states)}")
                print(f"Output files: {len(result['output_files'])}")
                for output_file in result['output_files']:
                    print(f"  - {output_file}")
        else:
            print("No commands were executed")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


def test_manual_command_execution():
    """Test manual command execution."""
    print("\nTesting manual command execution...")
    
    try:
        # Parse without executing commands - import parse_graphgif instead of parse_graphgif_file
        from parsing.ast_builder import parse_graphgif
        
        # Read file content manually to avoid automatic execution
        with open('./examples/example1.gg', 'r') as f:
            content = f.read()
        
        # Parse without automatic command execution
        ast, graph_model = parse_graphgif(content)[:2]
        
        print(f"Found {len(graph_model.graphs)} graphs")
        print(f"Found {len(ast.commands)} commands")
        
        # Manually execute commands
        if ast.commands:
            executor = CommandExecutor(graph_model, "test_output")
            results = executor.execute_commands(ast.commands)
            
            print("Manual execution results:")
            for graph_name, result in results.items():
                print(f"Graph: {graph_name}")
                print(f"Algorithm: {result['algorithm']}")
                print(f"Success: {result['result'].success}")
                if result['result'].success:
                    print(f"Steps: {len(result['result'].states)}")
                else:
                    print(f"Error: {result['result'].error_message}")
        else:
            print("No commands found to execute")
                
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


def test_command_with_arguments():
    """Test command execution with specific arguments."""
    print("\nTesting command with arguments...")
    
    # Create a simple test case
    test_code = """
    directed graph TestGraph {
        A, B, C, D;
        A -> B [weight=1];
        B -> C [weight=2];
        C -> D [weight=3];
        A -> D [weight=10];
    };
    
    run TestGraph with (algorithm='dijkstra', start_node='A', target_node='D', output='test_output');
    """
    
    try:
        from parsing.ast_builder import parse_graphgif
        
        ast, graph_model, execution_results = parse_graphgif(test_code)
        
        print(f"Found {len(graph_model.graphs)} graphs")
        print(f"Found {len(ast.commands)} commands")
        
        if execution_results:
            print("Execution results:")
            for graph_name, result in execution_results.items():
                print(f"Graph: {graph_name}")
                print(f"Algorithm: {result['algorithm']}")
                print(f"Success: {result['result'].success}")
                print(f"Steps: {len(result['result'].states)}")
                if result['result'].final_result:
                    print(f"Final result: {result['result'].final_result}")
                    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    test_command_execution()
    test_manual_command_execution()
    test_command_with_arguments()
