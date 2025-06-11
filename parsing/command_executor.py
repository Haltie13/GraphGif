"""
Command executor for processing parsed GraphGi        # Generate output if requested
        output_files = []
        if 'output' in args and algorithm_result.success:
            output_files = self._generate_output(
                target_graph, algorithm_result, args
            )
        elif not algorithm_result.success:
            print(f"Warning: Algorithm failed, skipping output generation: {algorithm_result.error_message}")
        
        return {
            'algorithm': algorithm,
            'result': algorithm_result,
            'output_files': output_files,
            'graph': command.graph_name
        }his module executes commands from parsed GraphGif programs.
"""

import os
from typing import Dict, Any, Optional, List
from models.statements import Command, Path
from models.values import Value
from models.graph_model import GraphModel
from algorithms.executor import AlgorithmExecutor
from generators.dot_generator import DotGenerator


class CommandExecutor:
    """Executes commands from parsed GraphGif programs."""
    
    def __init__(self, graph_model: GraphModel, base_output_dir: str = "output"):
        self.graph_model = graph_model
        self.algorithm_executor = AlgorithmExecutor()
        self.base_output_dir = base_output_dir
        self.results = {}
    
    def execute_commands(self, commands: List[Command]) -> Dict[str, Any]:
        """Execute all commands and return results."""
        for command in commands:
            result = self.execute_command(command)
            self.results[command.graph_name] = result
        return self.results
    
    def execute_command(self, command: Command) -> Dict[str, Any]:
        """Execute a single command."""
        # Get the target graph
        if command.graph_name not in self.graph_model.graphs:
            raise ValueError(f"Graph '{command.graph_name}' not found")
        
        target_graph = self.graph_model.graphs[command.graph_name]

        args = self._parse_arguments(command.arguments)

        algorithm = args.get('algorithm', self._infer_algorithm(args))
        if not algorithm:
            raise ValueError("No algorithm specified or inferred")

        algorithm_result = self.algorithm_executor.execute_algorithm(
            algorithm, self.graph_model, **args
        )
        
        # Generate output if requested
        output_files = []
        if 'output' in args or args.get('generate_output', True):
            output_files = self._generate_output(
                target_graph, algorithm_result, args, command.graph_name, algorithm
            )
        
        return {
            'algorithm': algorithm,
            'result': algorithm_result,
            'output_files': output_files,
            'graph': command.graph_name
        }
    
    def _parse_arguments(self, arguments: List) -> Dict[str, Any]:
        """Parse command arguments into a dictionary."""
        args = {}
        for arg in arguments:
            if isinstance(arg.argument_value, Value):
                args[arg.name] = arg.argument_value.value
            elif isinstance(arg.argument_value, Path):
                args[arg.name] = '.'.join(arg.argument_value.components)
            else:
                args[arg.name] = str(arg.argument_value)
        return args
    
    def _infer_algorithm(self, args: Dict[str, Any]) -> Optional[str]:
        """Infer algorithm from arguments or graph structure."""
        # Check for algorithm-specific parameters
        if 'start_node' in args or 'source' in args:
            if 'target_node' in args or 'destination' in args:
                return "dijkstra"  # Shortest path
            else:
                return "bfs"  # Single source traversal
        
        # Default to BFS for simple traversal
        return "bfs"
    
    def _generate_output(self, graph, algorithm_result, args: Dict[str, Any], graph_name: str, algorithm_name: str) -> List[str]:
        """Generate output files based on arguments."""
        output_files = []
        
        # Determine output format and settings
        output_path = args.get('output', self.base_output_dir)
        render_images = args.get('render_images', True)
        image_format = args.get('format', 'png')
        
        # Create filename pattern: (graph_name)_(algorithm)_...
        base_filename = f"{graph_name}_{algorithm_name}"
        
        # Handle output path
        if '.' in output_path and os.path.dirname(output_path):
            # Full path with extension provided
            output_dir = os.path.dirname(output_path)
            custom_basename = os.path.splitext(os.path.basename(output_path))[0]
            base_filename = f"{custom_basename}_{base_filename}"
        elif os.path.isdir(output_path) or not os.path.dirname(output_path):
            # Directory path provided
            output_dir = output_path
        else:
            # Custom base name without directory
            output_dir = self.base_output_dir
            base_filename = f"{output_path}_{base_filename}"
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate visualization
        generator = DotGenerator(
            output_dir=output_dir,
            render_images=render_images,
            image_format=image_format
        )
        
        generated_files = generator.generate(graph, algorithm_result, base_filename)
        output_files.extend(generated_files)
        
        # Generate animation script if requested
        if args.get('animate', True):
            script_path = generator.generate_animation_script(base_filename)
            output_files.append(script_path)
        
        return output_files
