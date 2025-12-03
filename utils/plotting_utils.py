"""
Plotting Utilities for MIT OCW 18.01

Comprehensive visualization tools for calculus concepts including:
- Function plotting
- Derivative and integral visualization
- Tangent and normal lines
- Area and volume visualization
- Interactive widgets
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
import sympy as sp
from sympy import lambdify
import plotly.graph_objects as go
import plotly.express as px
from typing import Union, List, Tuple, Callable
import warnings

# Set default matplotlib style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

class FunctionPlotter:
    """Plot functions and their properties"""
    
    @staticmethod
    def plot_function(func, var, x_range=(-10, 10), num_points=1000, 
                     title=None, xlabel='x', ylabel='f(x)', ax=None):
        """Plot a function
        
        Args:
            func: SymPy expression or callable
            var: SymPy variable (if func is expression)
            x_range: Tuple of (min, max) for x-axis
            num_points: Number of points to plot
            title: Plot title
            xlabel, ylabel: Axis labels
            ax: Matplotlib axis (creates new if None)
            
        Returns:
            Matplotlib axis object
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        
        # Convert to numerical function if SymPy
        if isinstance(func, sp.Basic):
            f = lambdify(var, func, 'numpy')
        else:
            f = func
        
        x_vals = np.linspace(x_range[0], x_range[1], num_points)
        
        try:
            y_vals = f(x_vals)
            ax.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)')
        except Exception as e:
            warnings.warn(f"Error plotting function: {e}")
        
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        
        if title:
            ax.set_title(title)
        
        ax.legend()
        return ax
    
    @staticmethod
    def plot_with_tangent(func, var, point, x_range=(-10, 10), ax=None):
        """Plot function with tangent line at a point
        
        Args:
            func: Function expression
            var: Variable
            point: Point for tangent
            x_range: x-axis range
            ax: Matplotlib axis
            
        Returns:
            Matplotlib axis
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot function
        f = lambdify(var, func, 'numpy')
        x_vals = np.linspace(x_range[0], x_range[1], 1000)
        y_vals = f(x_vals)
        ax.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)')
        
        # Calculate tangent line
        slope = sp.diff(func, var).subs(var, point)
        y_point = func.subs(var, point)
        tangent_func = slope * (var - point) + y_point
        
        # Plot tangent line
        tangent_f = lambdify(var, tangent_func, 'numpy')
        y_tangent = tangent_f(x_vals)
        ax.plot(x_vals, y_tangent, 'r--', linewidth=2, 
                label=f'Tangent at x={point}')
        
        # Mark the point
        ax.plot(point, float(y_point), 'ro', markersize=10, 
                label=f'Point ({point}, {float(y_point):.2f})')
        
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Function with Tangent Line (slope = {float(slope):.3f})')
        ax.legend()
        
        return ax
    
    @staticmethod
    def plot_derivative_comparison(func, var, x_range=(-10, 10), ax=None):
        """Plot function and its derivative side by side
        
        Args:
            func: Function expression
            var: Variable
            x_range: x-axis range
            ax: Matplotlib axes (creates subplot if None)
            
        Returns:
            Matplotlib figure and axes
        """
        if ax is None:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        else:
            ax1, ax2 = ax
            fig = ax1.get_figure()
        
        x_vals = np.linspace(x_range[0], x_range[1], 1000)
        
        # Plot original function
        f = lambdify(var, func, 'numpy')
        y_vals = f(x_vals)
        ax1.plot(x_vals, y_vals, 'b-', linewidth=2)
        ax1.axhline(y=0, color='k', linewidth=0.5)
        ax1.axvline(x=0, color='k', linewidth=0.5)
        ax1.grid(True, alpha=0.3)
        ax1.set_xlabel('x')
        ax1.set_ylabel('f(x)')
        ax1.set_title('Original Function f(x)')
        
        # Plot derivative
        derivative = sp.diff(func, var)
        df = lambdify(var, derivative, 'numpy')
        dy_vals = df(x_vals)
        ax2.plot(x_vals, dy_vals, 'r-', linewidth=2)
        ax2.axhline(y=0, color='k', linewidth=0.5)
        ax2.axvline(x=0, color='k', linewidth=0.5)
        ax2.grid(True, alpha=0.3)
        ax2.set_xlabel('x')
        ax2.set_ylabel("f'(x)")
        ax2.set_title("Derivative f'(x)")
        
        plt.tight_layout()
        return fig, (ax1, ax2)

class IntegralVisualizer:
    """Visualize integrals and areas"""
    
    @staticmethod
    def plot_riemann_sum(func, var, lower, upper, n, method='midpoint', ax=None):
        """Visualize Riemann sum approximation
        
        Args:
            func: Function to integrate
            var: Variable
            lower, upper: Integration bounds
            n: Number of rectangles
            method: 'left', 'right', or 'midpoint'
            ax: Matplotlib axis
            
        Returns:
            Matplotlib axis
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot function
        f = lambdify(var, func, 'numpy')
        x_vals = np.linspace(lower, upper, 1000)
        y_vals = f(x_vals)
        ax.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)', zorder=3)
        
        # Draw rectangles
        dx = (upper - lower) / n
        
        for i in range(n):
            if method == 'left':
                xi = lower + i * dx
            elif method == 'right':
                xi = lower + (i + 1) * dx
            else:  # midpoint
                xi = lower + (i + 0.5) * dx
            
            height = f(xi)
            rect_x = lower + i * dx
            
            rect = patches.Rectangle((rect_x, 0), dx, height, 
                                     linewidth=1, edgecolor='red', 
                                     facecolor='lightblue', alpha=0.5, zorder=1)
            ax.add_patch(rect)
        
        # Calculate and display sum
        if method == 'left':
            x_sample = np.linspace(lower, upper - dx, n)
        elif method == 'right':
            x_sample = np.linspace(lower + dx, upper, n)
        else:
            x_sample = np.linspace(lower + dx/2, upper - dx/2, n)
        
        riemann_sum = np.sum(f(x_sample) * dx)
        
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3, zorder=0)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'{method.capitalize()} Riemann Sum (n={n})\nApproximation: {riemann_sum:.4f}')
        ax.legend()
        
        return ax
    
    @staticmethod
    def plot_area_between_curves(f1, f2, var, lower, upper, ax=None):
        """Visualize area between two curves
        
        Args:
            f1, f2: Two functions
            var: Variable
            lower, upper: Bounds
            ax: Matplotlib axis
            
        Returns:
            Matplotlib axis and area value
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        
        # Convert to numerical functions
        func1 = lambdify(var, f1, 'numpy')
        func2 = lambdify(var, f2, 'numpy')
        
        x_vals = np.linspace(lower, upper, 1000)
        y1_vals = func1(x_vals)
        y2_vals = func2(x_vals)
        
        # Plot functions
        ax.plot(x_vals, y1_vals, 'b-', linewidth=2, label='f₁(x)')
        ax.plot(x_vals, y2_vals, 'r-', linewidth=2, label='f₂(x)')
        
        # Fill area between curves
        ax.fill_between(x_vals, y1_vals, y2_vals, alpha=0.3, color='green')
        
        # Calculate area
        area = sp.integrate(sp.Abs(f1 - f2), (var, lower, upper))
        
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=lower, color='k', linewidth=0.5, linestyle='--', alpha=0.5)
        ax.axvline(x=upper, color='k', linewidth=0.5, linestyle='--', alpha=0.5)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Area Between Curves: {float(area):.4f}')
        ax.legend()
        
        return ax, area
    
    @staticmethod
    def plot_volume_of_revolution(func, var, lower, upper, axis='x', n_slices=50, ax=None):
        """Visualize volume of revolution (disk method)
        
        Args:
            func: Function to rotate
            var: Variable
            lower, upper: Bounds
            axis: 'x' or 'y' axis of rotation
            n_slices: Number of disks to show
            ax: Matplotlib axis (must be 3D)
            
        Returns:
            Matplotlib 3D axis
        """
        from mpl_toolkits.mplot3d import Axes3D
        
        if ax is None:
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111, projection='3d')
        
        f = lambdify(var, func, 'numpy')
        
        # Create slices
        x_slices = np.linspace(lower, upper, n_slices)
        
        for x_pos in x_slices:
            radius = abs(f(x_pos))
            
            # Create circle for this slice
            theta = np.linspace(0, 2*np.pi, 50)
            y_circle = radius * np.cos(theta)
            z_circle = radius * np.sin(theta)
            x_circle = np.full_like(theta, x_pos)
            
            ax.plot(x_circle, y_circle, z_circle, 'b-', alpha=0.3, linewidth=0.5)
        
        # Create surface
        x_surf = np.linspace(lower, upper, 100)
        theta_surf = np.linspace(0, 2*np.pi, 100)
        X, Theta = np.meshgrid(x_surf, theta_surf)
        R = np.abs(f(X))
        Y = R * np.cos(Theta)
        Z = R * np.sin(Theta)
        
        ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
        
        # Calculate volume
        volume = float(sp.pi * sp.integrate(func**2, (var, lower, upper)))
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title(f'Volume of Revolution: {volume:.4f}')
        
        return ax

class InteractivePlots:
    """Interactive plotly visualizations"""
    
    @staticmethod
    def interactive_function(func, var, x_range=(-10, 10), num_points=1000):
        """Create interactive function plot with Plotly
        
        Args:
            func: Function expression
            var: Variable
            x_range: x-axis range
            num_points: Number of points
            
        Returns:
            Plotly figure object
        """
        f = lambdify(var, func, 'numpy')
        x_vals = np.linspace(x_range[0], x_range[1], num_points)
        y_vals = f(x_vals)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', 
                                name='f(x)', line=dict(width=3)))
        
        fig.update_layout(
            title='Interactive Function Plot',
            xaxis_title='x',
            yaxis_title='f(x)',
            hovermode='x unified',
            template='plotly_white',
            height=600
        )
        
        # Add zero lines
        fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
        fig.add_vline(x=0, line_dash="dash", line_color="gray", opacity=0.5)
        
        return fig
    
    @staticmethod
    def interactive_tangent_slider(func, var, x_range=(-10, 10)):
        """Interactive plot with sliding tangent line
        
        Args:
            func: Function expression
            var: Variable
            x_range: x-axis range
            
        Returns:
            Plotly figure with slider
        """
        f = lambdify(var, func, 'numpy')
        df = lambdify(var, sp.diff(func, var), 'numpy')
        
        x_vals = np.linspace(x_range[0], x_range[1], 1000)
        y_vals = f(x_vals)
        
        # Create frames for different tangent points
        frames = []
        tangent_points = np.linspace(x_range[0], x_range[1], 50)
        
        for point in tangent_points:
            y_point = f(point)
            slope = df(point)
            y_tangent = slope * (x_vals - point) + y_point
            
            frame = go.Frame(
                data=[
                    go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'),
                    go.Scatter(x=x_vals, y=y_tangent, mode='lines', 
                             name='Tangent', line=dict(dash='dash', color='red')),
                    go.Scatter(x=[point], y=[y_point], mode='markers',
                             marker=dict(size=12, color='red'), name='Point')
                ],
                name=f'{point:.2f}'
            )
            frames.append(frame)
        
        # Initial figure
        fig = go.Figure(
            data=[
                go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'),
                go.Scatter(x=x_vals, y=f(x_range[0]) + df(x_range[0])*(x_vals-x_range[0]),
                         mode='lines', name='Tangent', line=dict(dash='dash', color='red')),
                go.Scatter(x=[x_range[0]], y=[f(x_range[0])], mode='markers',
                         marker=dict(size=12, color='red'), name='Point')
            ],
            frames=frames
        )
        
        fig.update_layout(
            title='Interactive Tangent Line',
            xaxis_title='x',
            yaxis_title='y',
            hovermode='x unified',
            updatemenus=[{
                'type': 'buttons',
                'showactive': False,
                'buttons': [
                    {'label': 'Play', 'method': 'animate',
                     'args': [None, {'frame': {'duration': 50}}]},
                    {'label': 'Pause', 'method': 'animate',
                     'args': [[None], {'frame': {'duration': 0}, 'mode': 'immediate'}]}
                ]
            }],
            sliders=[{
                'active': 0,
                'steps': [{'args': [[f.name], {'frame': {'duration': 0}, 'mode': 'immediate'}],
                          'label': f'{float(f.name):.2f}', 'method': 'animate'}
                         for f in frames]
            }]
        )
        
        return fig

# Convenience functions
def plot(func, var=sp.Symbol('x'), x_range=(-10, 10), **kwargs):
    """Quick plot function"""
    return FunctionPlotter.plot_function(func, var, x_range, **kwargs)

def plot_tangent(func, var, point, **kwargs):
    """Quick tangent line plot"""
    return FunctionPlotter.plot_with_tangent(func, var, point, **kwargs)

def plot_derivative(func, var, **kwargs):
    """Quick derivative comparison plot"""
    return FunctionPlotter.plot_derivative_comparison(func, var, **kwargs)

def plot_area(f1, f2, var, lower, upper, **kwargs):
    """Quick area between curves plot"""
    return IntegralVisualizer.plot_area_between_curves(f1, f2, var, lower, upper, **kwargs)

# Export main classes and functions
__all__ = [
    'FunctionPlotter',
    'IntegralVisualizer',
    'InteractivePlots',
    'plot',
    'plot_tangent',
    'plot_derivative',
    'plot_area'
]
