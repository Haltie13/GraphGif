"""
Base generator class for GraphGif output formats.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.base import AlgorithmResult, GraphState
from models.graph_model import ConcreteGraph


class BaseGenerator(ABC):
    """Abstract base class for all generators."""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        
    @abstractmethod
    def generate(self, graph: ConcreteGraph, algorithm_result: AlgorithmResult,
                 base_filename: str = "graph") -> List[str]:
        """
        Generate output files for each state of the algorithm execution.
        
        Args:
            graph: The concrete graph being processed
            algorithm_result: Result from algorithm execution containing states
            base_filename: Base name for output files
            
        Returns:
            List of generated file paths
        """
        pass
    
    @abstractmethod
    def generate_single_state(self, graph: ConcreteGraph, state: GraphState,
                             filename: str) -> str:
        """
        Generate output for a single algorithm state.
        
        Args:
            graph: The concrete graph
            state: The specific state to generate
            filename: Output filename
            
        Returns:
            Path to generated file
        """
        pass
    
    def _ensure_output_dir(self) -> None:
        """Ensure output directory exists."""
        import os
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _sanitize_filename(self, filename: str) -> str:
        """Sanitize filename to be filesystem-safe."""
        import re
        # Replace invalid characters with underscores
        return re.sub(r'[<>:"/\\|?*]', '_', filename)
