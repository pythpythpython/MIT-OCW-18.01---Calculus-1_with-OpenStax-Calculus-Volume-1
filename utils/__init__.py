"""
Utility Package for MIT OCW 18.01 Calculus

This package provides comprehensive utilities for calculus operations,
visualization, and LaTeX rendering in Jupyter notebooks.
"""

from .calculus_utils import *
from .plotting_utils import *
from .latex_rendering import *

__version__ = '1.0.0'
__author__ = 'MIT OCW 18.01 Study Project'

# Export all utility functions
__all__ = [
    # From calculus_utils
    'DerivativeCalculator',
    'IntegralCalculator',
    'LimitCalculator',
    'SeriesCalculator',
    'NumericalMethods',
    'derivative',
    'integrate',
    'limit',
    'tangent',
    
    # From plotting_utils
    'FunctionPlotter',
    'IntegralVisualizer',
    'InteractivePlots',
    'plot',
    'plot_tangent',
    'plot_derivative',
    'plot_area',
    
    # From latex_rendering
    'LatexFormatter',
    'ExpressionSimplifier',
    'show_equation',
    'show_derivative',
    'show_integral',
    'show_limit',
    'show_steps'
]
