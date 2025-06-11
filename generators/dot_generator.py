"""
DOT generator for GraphGif algorithm visualization.
Creates Graphviz DOT files for each state of algorithm execution.
"""

import os
import sys
from typing import List, Dict, Any, Optional

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .base_generator import BaseGenerator
from algorithms.base import AlgorithmResult, GraphState
from models.graph_model import ConcreteGraph, GraphEdge


class DotGenerator(BaseGenerator):
    """Generates DOT files for algorithm state visualization."""
    
    def __init__(self, output_dir: str = "output", 
                 render_images: bool = False,
                 image_format: str = "png"):
        """
        Initialize DOT generator.
        
        Args:
            output_dir: Directory for output files
            render_images: Whether to render DOT files to images (requires Graphviz)
            image_format: Image format for rendering (png, svg, pdf, etc.)
        """
        super().__init__(output_dir)
        self.render_images = render_images
        self.image_format = image_format
        
        # Default styling
        self.default_node_style = {
            'shape': 'circle',
            'style': 'filled',
            'fillcolor': 'lightgray',
            'fontname': 'Arial',
            'fontsize': '12'
        }
        
        self.default_edge_style = {
            'fontname': 'Arial',
            'fontsize': '10'
        }
        
        self.algorithm_colors = {
            'visited': 'lightgreen',
            'current': 'red',
            'queued': 'yellow',
            'path': 'lightblue',
            'unvisited': 'lightgray'
        }

        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate(self, graph: ConcreteGraph, algorithm_result: AlgorithmResult,
                 base_filename: str = "graph") -> List[str]:
        """Generate DOT files for all algorithm states."""
        if not algorithm_result.success:
            raise ValueError(f"Cannot generate from failed algorithm: {algorithm_result.error_message}")
        
        self._ensure_output_dir()
        generated_files = []
        
        for i, state in enumerate(algorithm_result.states):
            filename = f"{base_filename}_step_{i:03d}_{state.step:03d}.dot"
            filepath = self.generate_single_state(graph, state, filename)
            generated_files.append(filepath)
            
            if self.render_images:
                image_path = self._render_to_image(filepath)
                if image_path:
                    generated_files.append(image_path)
        
        # Generate summary file with metadata
        summary_file = self._generate_summary(graph, algorithm_result, base_filename)
        generated_files.append(summary_file)
        
        return generated_files
    
    def generate_single_state(self, graph: ConcreteGraph, state: GraphState,
                             filename: str) -> str:
        """Generate DOT file for a single algorithm state."""
        self._ensure_output_dir()
        
        safe_filename = self._sanitize_filename(filename)
        filepath = os.path.join(self.output_dir, safe_filename)
        
        dot_content = self._generate_dot_content(graph, state)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(dot_content)
        
        return filepath
    
    def _generate_dot_content(self, graph: ConcreteGraph, state: GraphState) -> str:
        """Generate the actual DOT content for a state."""
        lines = []
        
        # Graph declaration
        graph_type = "digraph" if graph.is_directed else "graph"
        lines.append(f'{graph_type} "{graph.name}_step_{state.step}" {{')
        
        # Graph attributes
        lines.append('  // Graph attributes')
        lines.append('  rankdir=TB;')
        lines.append('  bgcolor=white;')
        lines.append('  node [fontname="Arial"];')
        lines.append('  edge [fontname="Arial"];')
        lines.append('')
        
        # Title/label for the state
        title = f"Step {state.step}"
        lines.append(f'  label="{title}";')
        lines.append('  labelloc=top;')
        lines.append('  fontsize=14;')
        lines.append('')

        legend_text = state.description.replace('"', '\\"')
        lines.append('  // Legend')
        lines.append('  legend [')
        lines.append('    shape=box,')
        lines.append('    style="filled,rounded",')
        lines.append('    fillcolor=lightyellow,')
        lines.append('    fontsize=10,')
        lines.append(f'    label="{legend_text}",')
        lines.append('    margin=0.1')
        lines.append('  ];')
        lines.append('')

        lines.append('  {rank=sink; legend}')
        lines.append('')




        # Add algorithm-specific metadata as label
        if state.metadata:
            metadata_lines = self._format_metadata(state)
            if metadata_lines:
                lines.extend(metadata_lines)
                lines.append('')
        
        # Nodes
        lines.append('  // Nodes')
        for node_id, node in graph.nodes.items():
            node_attrs = self._get_node_attributes(node_id, node, state)
            attrs_str = ', '.join(f'{k}="{v}"' for k, v in node_attrs.items())
            lines.append(f'  "{node_id}" [{attrs_str}];')
        
        lines.append('')
        
        # Edges
        lines.append('  // Edges')
        edge_op = " -> " if graph.is_directed else " -- "
        
        for edge in graph.edges:
            edge_attrs = self._get_edge_attributes(edge, state)
            attrs_str = ', '.join(f'{k}="{v}"' for k, v in edge_attrs.items()) if edge_attrs else ""
            attrs_part = f" [{attrs_str}]" if attrs_str else ""
            lines.append(f'  "{edge.source}"{edge_op}"{edge.target}"{attrs_part};')
        
        lines.append('}')
        
        return '\n'.join(lines)
    
    def _get_node_attributes(self, node_id: str, node, state: GraphState) -> Dict[str, str]:
        """Get DOT attributes for a node based on algorithm state."""
        attrs = self.default_node_style.copy()
        
        # Apply node's original attributes
        if hasattr(node, 'attributes') and node.attributes:
            for key, value in node.attributes.items():
                attrs[key] = str(value)
        
        # Apply state-based coloring
        if state.node_colors and node_id in state.node_colors:
            color = state.node_colors[node_id]
            if color == 'green':
                attrs['fillcolor'] = self.algorithm_colors['visited']
            elif color == 'red':
                attrs['fillcolor'] = self.algorithm_colors['current']
                attrs['penwidth'] = '3'
            elif color == 'yellow':
                attrs['fillcolor'] = self.algorithm_colors['queued']
            elif color == 'blue':
                attrs['fillcolor'] = self.algorithm_colors['path']
                attrs['penwidth'] = '2'
        
        # Mark current node
        if state.current_node == node_id:
            attrs['fillcolor'] = self.algorithm_colors['current']
            attrs['penwidth'] = '3'
        
        # Add distance information for shortest path algorithms
        if state.distances and node_id in state.distances:
            distance = state.distances[node_id]
            if distance != float('inf'):
                current_label = attrs.get('label', node_id)
                attrs['label'] = f"{current_label}\\nd:{distance}"
        
        return attrs
    
    def _get_edge_attributes(self, edge: GraphEdge, state: GraphState) -> Dict[str, str]:
        """Get DOT attributes for an edge based on algorithm state."""
        attrs = self.default_edge_style.copy()
        
        # Apply edge's original attributes
        if edge.attributes:
            for key, value in edge.attributes.items():
                if key == 'weight':
                    attrs['label'] = str(value)
                else:
                    attrs[key] = str(value)
        
        # Apply state-based styling
        edge_tuple = (edge.source, edge.target)
        reverse_tuple = (edge.target, edge.source)
        
        if state.edge_colors:
            if edge_tuple in state.edge_colors:
                color = state.edge_colors[edge_tuple]
                attrs['color'] = color
                if color == 'red':
                    attrs['penwidth'] = '2'
            elif not edge.directed and reverse_tuple in state.edge_colors:
                color = state.edge_colors[reverse_tuple]
                attrs['color'] = color
                if color == 'red':
                    attrs['penwidth'] = '2'
        
        # Highlight edges
        if state.highlighted_edges:
            if edge_tuple in state.highlighted_edges or (not edge.directed and reverse_tuple in state.highlighted_edges):
                attrs['color'] = 'red'
                attrs['penwidth'] = '2'
        
        return attrs
    
    def _format_metadata(self, state: GraphState) -> List[str]:
        """Format algorithm metadata for display."""
        lines = []
        metadata = state.metadata or {}
        
        # Algorithm name
        if 'algorithm' in metadata:
            lines.append(f'  // Algorithm: {metadata["algorithm"]}')
        
        # Queue/Stack state
        if state.queue:
            queue_str = ', '.join(state.queue)
            lines.append(f'  // Queue: [{queue_str}]')
        
        if state.stack:
            stack_str = ', '.join(state.stack)
            lines.append(f'  // Stack: [{stack_str}]')
        
        # Priority queue for Dijkstra
        if 'priority_queue' in metadata and metadata['priority_queue']:
            pq_items = [f"({d}, {n})" for d, n in metadata['priority_queue']]
            pq_str = ', '.join(pq_items)
            lines.append(f'  // Priority Queue: [{pq_str}]')
        
        # Visit order
        if 'visit_order' in metadata and metadata['visit_order']:
            visit_str = ' → '.join(metadata['visit_order'])
            lines.append(f'  // Visit Order: {visit_str}')
        
        # Shortest path
        if 'shortest_path' in metadata and metadata['shortest_path']:
            path_str = ' → '.join(metadata['shortest_path'])
            lines.append(f'  // Shortest Path: {path_str}')
        
        return lines
    
    def _generate_summary(self, graph: ConcreteGraph, algorithm_result: AlgorithmResult,
                         base_filename: str) -> str:
        """Generate a summary file with algorithm execution information."""
        summary_filename = f"{base_filename}_summary.txt"
        filepath = os.path.join(self.output_dir, summary_filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"GraphGif Algorithm Execution Summary\n")
            f.write(f"{'=' * 40}\n\n")
            
            f.write(f"Graph: {graph.name}\n")
            f.write(f"Type: {'Directed' if graph.is_directed else 'Undirected'}\n")
            f.write(f"Nodes: {len(graph.nodes)}\n")
            f.write(f"Edges: {len(graph.edges)}\n\n")
            
            f.write(f"Algorithm Execution:\n")
            f.write(f"Success: {algorithm_result.success}\n")
            f.write(f"Steps: {len(algorithm_result.states)}\n")
            f.write(f"Execution Time: {algorithm_result.execution_time:.4f}s\n")
            
            if algorithm_result.final_result:
                f.write(f"\nFinal Result:\n")
                for key, value in algorithm_result.final_result.items():
                    f.write(f"  {key}: {value}\n")
            
            if algorithm_result.error_message:
                f.write(f"\nError: {algorithm_result.error_message}\n")
            
            # List generated files
            f.write(f"\nGenerated Files:\n")
            for i, state in enumerate(algorithm_result.states):
                dot_file = f"{base_filename}_step_{i:03d}_{state.step:03d}.dot"
                f.write(f"  Step {state.step}: {dot_file}\n")
        
        return filepath
    
    def _render_to_image(self, dot_filepath: str) -> Optional[str]:
        """Render DOT file to image using Graphviz (if available)."""
        try:
            import subprocess
            
            # Generate output image path
            base_path = os.path.splitext(dot_filepath)[0]
            image_path = f"{base_path}.{self.image_format}"
            
            # Run dot command
            cmd = ['dot', f'-T{self.image_format}', dot_filepath, '-o', image_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                return image_path
            else:
                print(f"Warning: Failed to render {dot_filepath}: {result.stderr}")
                return None
                
        except (ImportError, FileNotFoundError):
            print("Warning: Graphviz not available for image rendering")
            return None
    
    def generate_animation_script(self, base_filename: str) -> str:
        """Generate a script to create animated GIF from generated images."""
        script_filename = f"{base_filename}_animate.sh"
        script_path = os.path.join(self.output_dir, script_filename)
        
        with open(script_path, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("# Animation script for GraphGif algorithm visualization\n\n")
            
            f.write("# Check if ImageMagick is available\n")
            f.write("if ! command -v convert &> /dev/null; then\n")
            f.write('    echo "ImageMagick not found. Please install it to create animations."\n')
            f.write("    exit 1\n")
            f.write("fi\n\n")
            
            f.write("# Create animated GIF\n")
            f.write(f"convert -delay 100 {base_filename}_step_*.{self.image_format} ")
            f.write(f"{base_filename}_animation.gif\n\n")
            
            f.write(f'echo "Animation created: {base_filename}_animation.gif"\n')
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        return script_path
