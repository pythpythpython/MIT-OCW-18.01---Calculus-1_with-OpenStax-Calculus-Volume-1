"""
Calculus Utilities for MIT OCW 18.01

Provides comprehensive functions for calculus operations including:
- Derivatives and integrals
- Limits and continuity
- Series and sequences
- Numerical methods
"""

import numpy as np
import sympy as sp
from sympy import *
from typing import Union, Tuple, List, Callable
import warnings

# Initialize SymPy symbols
x, y, z, t = sp.symbols('x y z t')
n, k, m = sp.symbols('n k m', integer=True)
a, b, c, h = sp.symbols('a b c h', real=True)

class DerivativeCalculator:
    """Calculate and analyze derivatives"""
    
    @staticmethod
    def compute_derivative(expr, var=x, order=1):
        """Compute derivative of expression
        
        Args:
            expr: SymPy expression
            var: Variable to differentiate with respect to
            order: Order of derivative (default 1)
            
        Returns:
            SymPy expression of derivative
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        return sp.diff(expr, var, order)
    
    @staticmethod
    def tangent_line(func, point, var=x):
        """Find tangent line at a point
        
        Args:
            func: Function expression
            point: x-coordinate of tangent point
            var: Variable (default x)
            
        Returns:
            Tuple of (tangent_line_expr, slope, y_value)
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        slope = sp.diff(func, var).subs(var, point)
        y_val = func.subs(var, point)
        tangent = slope * (var - point) + y_val
        
        return tangent, slope, y_val
    
    @staticmethod
    def normal_line(func, point, var=x):
        """Find normal line (perpendicular to tangent) at a point"""
        if isinstance(func, str):
            func = sp.sympify(func)
        
        slope = sp.diff(func, var).subs(var, point)
        y_val = func.subs(var, point)
        
        if slope != 0:
            normal_slope = -1 / slope
            normal = normal_slope * (var - point) + y_val
        else:
            # Vertical normal line
            normal = None
            
        return normal, y_val
    
    @staticmethod
    def implicit_derivative(equation, dependent_var=y, independent_var=x):
        """Compute implicit derivative dy/dx from equation F(x,y) = 0
        
        Args:
            equation: Expression equal to zero (F(x,y) = 0)
            dependent_var: Dependent variable (default y)
            independent_var: Independent variable (default x)
            
        Returns:
            Expression for dy/dx
        """
        if isinstance(equation, str):
            equation = sp.sympify(equation)
        
        # Use implicit differentiation: dF/dx + dF/dy * dy/dx = 0
        # Solve for dy/dx = -(dF/dx) / (dF/dy)
        dF_dx = sp.diff(equation, independent_var)
        dF_dy = sp.diff(equation, dependent_var)
        
        dy_dx = -dF_dx / dF_dy
        return sp.simplify(dy_dx)

class IntegralCalculator:
    """Calculate and analyze integrals"""
    
    @staticmethod
    def indefinite_integral(expr, var=x):
        """Compute indefinite integral
        
        Args:
            expr: Expression to integrate
            var: Variable of integration
            
        Returns:
            Antiderivative (without constant of integration)
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        return sp.integrate(expr, var)
    
    @staticmethod
    def definite_integral(expr, var, lower, upper):
        """Compute definite integral
        
        Args:
            expr: Expression to integrate
            var: Variable of integration
            lower: Lower limit
            upper: Upper limit
            
        Returns:
            Numerical or symbolic value of definite integral
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        return sp.integrate(expr, (var, lower, upper))
    
    @staticmethod
    def area_between_curves(f1, f2, var, lower, upper):
        """Calculate area between two curves
        
        Args:
            f1, f2: Two functions
            var: Variable
            lower, upper: Integration bounds
            
        Returns:
            Area between curves
        """
        if isinstance(f1, str):
            f1 = sp.sympify(f1)
        if isinstance(f2, str):
            f2 = sp.sympify(f2)
        
        area = sp.integrate(sp.Abs(f1 - f2), (var, lower, upper))
        return area
    
    @staticmethod
    def volume_disk_method(radius_func, var, lower, upper):
        """Calculate volume using disk method: V = π∫[R(x)]² dx
        
        Args:
            radius_func: Radius as function of var
            var: Variable of integration
            lower, upper: Bounds
            
        Returns:
            Volume
        """
        if isinstance(radius_func, str):
            radius_func = sp.sympify(radius_func)
        
        volume = sp.pi * sp.integrate(radius_func**2, (var, lower, upper))
        return volume
    
    @staticmethod
    def volume_shell_method(radius_func, height_func, var, lower, upper):
        """Calculate volume using shell method: V = 2π∫r(x)h(x) dx
        
        Args:
            radius_func: Radius to shell
            height_func: Height of shell
            var: Variable of integration
            lower, upper: Bounds
            
        Returns:
            Volume
        """
        if isinstance(radius_func, str):
            radius_func = sp.sympify(radius_func)
        if isinstance(height_func, str):
            height_func = sp.sympify(height_func)
        
        volume = 2 * sp.pi * sp.integrate(
            radius_func * height_func, (var, lower, upper)
        )
        return volume
    
    @staticmethod
    def arc_length(func, var, lower, upper):
        """Calculate arc length: L = ∫√(1 + (dy/dx)²) dx
        
        Args:
            func: Function y = f(x)
            var: Variable
            lower, upper: Bounds
            
        Returns:
            Arc length
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        derivative = sp.diff(func, var)
        integrand = sp.sqrt(1 + derivative**2)
        length = sp.integrate(integrand, (var, lower, upper))
        return length

class LimitCalculator:
    """Calculate and analyze limits"""
    
    @staticmethod
    def compute_limit(expr, var, point, direction=None):
        """Compute limit of expression as var approaches point
        
        Args:
            expr: Expression
            var: Variable
            point: Point to approach (can be oo for infinity)
            direction: '+', '-', or None for two-sided
            
        Returns:
            Limit value
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        
        if direction == '+':
            return sp.limit(expr, var, point, '+')
        elif direction == '-':
            return sp.limit(expr, var, point, '-')
        else:
            return sp.limit(expr, var, point)
    
    @staticmethod
    def check_continuity(func, var, point):
        """Check if function is continuous at a point
        
        A function is continuous at point a if:
        1. f(a) exists
        2. lim(x→a) f(x) exists
        3. lim(x→a) f(x) = f(a)
        
        Returns:
            Tuple (is_continuous, explanation)
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        try:
            # Check if f(a) exists
            f_a = func.subs(var, point)
            if f_a in [sp.nan, sp.zoo, sp.oo, -sp.oo]:
                return False, f"f({point}) does not exist"
            
            # Check if limit exists
            lim_val = sp.limit(func, var, point)
            if lim_val in [sp.nan, sp.zoo]:
                return False, f"limit as x→{point} does not exist"
            
            # Check if limit equals function value
            if sp.simplify(lim_val - f_a) == 0:
                return True, "Function is continuous"
            else:
                return False, f"limit = {lim_val} ≠ f({point}) = {f_a}"
                
        except Exception as e:
            return False, f"Error checking continuity: {str(e)}"
    
    @staticmethod
    def lhopital_rule(numerator, denominator, var, point, max_iterations=5):
        """Apply L'Hôpital's rule for indeterminate forms
        
        Args:
            numerator: Numerator function
            denominator: Denominator function
            var: Variable
            point: Limit point
            max_iterations: Maximum applications of L'Hôpital's rule
            
        Returns:
            Limit value and list of steps
        """
        if isinstance(numerator, str):
            numerator = sp.sympify(numerator)
        if isinstance(denominator, str):
            denominator = sp.sympify(denominator)
        
        steps = []
        num, den = numerator, denominator
        
        for i in range(max_iterations):
            # Evaluate current form
            num_val = sp.limit(num, var, point)
            den_val = sp.limit(den, var, point)
            
            steps.append({
                'iteration': i,
                'numerator': num,
                'denominator': den,
                'num_limit': num_val,
                'den_limit': den_val
            })
            
            # Check if indeterminate
            if (num_val, den_val) not in [(0, 0), (sp.oo, sp.oo), (-sp.oo, -sp.oo)]:
                if den_val != 0:
                    return num_val / den_val, steps
                else:
                    return sp.oo, steps
            
            # Apply L'Hôpital's rule
            num = sp.diff(num, var)
            den = sp.diff(den, var)
        
        # Final attempt
        result = sp.limit(num / den, var, point)
        return result, steps

class SeriesCalculator:
    """Work with series and sequences"""
    
    @staticmethod
    def taylor_series(func, var, point, order):
        """Compute Taylor series expansion
        
        Args:
            func: Function to expand
            var: Variable
            point: Point of expansion
            order: Order of expansion
            
        Returns:
            Taylor polynomial
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        return sp.series(func, var, point, order).removeO()
    
    @staticmethod
    def maclaurin_series(func, var, order):
        """Compute Maclaurin series (Taylor series at 0)"""
        return SeriesCalculator.taylor_series(func, var, 0, order)
    
    @staticmethod
    def power_series_representation(func, var, order=10):
        """Find power series representation"""
        if isinstance(func, str):
            func = sp.sympify(func)
        
        return sp.series(func, var, 0, order)

class NumericalMethods:
    """Numerical methods for calculus"""
    
    @staticmethod
    def newtons_method(func, initial_guess, var=x, tolerance=1e-10, max_iterations=100):
        """Find root using Newton's method
        
        Args:
            func: Function to find root of
            initial_guess: Starting point
            var: Variable
            tolerance: Convergence tolerance
            max_iterations: Maximum iterations
            
        Returns:
            Tuple (root, iterations_list)
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        # Convert to numerical function
        f = sp.lambdify(var, func, 'numpy')
        df = sp.lambdify(var, sp.diff(func, var), 'numpy')
        
        iterations = []
        xn = float(initial_guess)
        
        for i in range(max_iterations):
            fxn = f(xn)
            dfxn = df(xn)
            
            iterations.append({
                'iteration': i,
                'x': xn,
                'f(x)': fxn,
                "f'(x)": dfxn
            })
            
            if abs(fxn) < tolerance:
                return xn, iterations
            
            if abs(dfxn) < 1e-15:
                warnings.warn("Derivative near zero, Newton's method may fail")
                return None, iterations
            
            xn = xn - fxn / dfxn
        
        warnings.warn("Maximum iterations reached")
        return xn, iterations
    
    @staticmethod
    def riemann_sum(func, lower, upper, n, method='midpoint', var=x):
        """Calculate Riemann sum
        
        Args:
            func: Function to integrate
            lower, upper: Bounds
            n: Number of rectangles
            method: 'left', 'right', 'midpoint', 'trapezoid'
            var: Variable
            
        Returns:
            Approximation of integral
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        f = sp.lambdify(var, func, 'numpy')
        dx = (upper - lower) / n
        
        if method == 'left':
            x_vals = np.linspace(lower, upper - dx, n)
            return np.sum(f(x_vals) * dx)
        elif method == 'right':
            x_vals = np.linspace(lower + dx, upper, n)
            return np.sum(f(x_vals) * dx)
        elif method == 'midpoint':
            x_vals = np.linspace(lower + dx/2, upper - dx/2, n)
            return np.sum(f(x_vals) * dx)
        elif method == 'trapezoid':
            x_vals = np.linspace(lower, upper, n + 1)
            y_vals = f(x_vals)
            return dx * (np.sum(y_vals) - (y_vals[0] + y_vals[-1])/2)
    
    @staticmethod
    def simpsons_rule(func, lower, upper, n, var=x):
        """Calculate integral using Simpson's rule
        
        Args:
            func: Function to integrate
            lower, upper: Bounds
            n: Number of intervals (must be even)
            var: Variable
            
        Returns:
            Approximation of integral
        """
        if n % 2 != 0:
            raise ValueError("n must be even for Simpson's rule")
        
        if isinstance(func, str):
            func = sp.sympify(func)
        
        f = sp.lambdify(var, func, 'numpy')
        h = (upper - lower) / n
        x_vals = np.linspace(lower, upper, n + 1)
        y_vals = f(x_vals)
        
        # Simpson's rule: (h/3) * [y0 + 4*y1 + 2*y2 + 4*y3 + ... + yn]
        result = y_vals[0] + y_vals[-1]
        result += 4 * np.sum(y_vals[1:-1:2])  # Odd indices
        result += 2 * np.sum(y_vals[2:-1:2])  # Even indices
        result *= h / 3
        
        return result

# Convenience functions for quick calculations
def derivative(expr, var=x, order=1):
    """Quick derivative calculation"""
    return DerivativeCalculator.compute_derivative(expr, var, order)

def integrate(expr, var=x, lower=None, upper=None):
    """Quick integration (definite if bounds provided)"""
    if lower is not None and upper is not None:
        return IntegralCalculator.definite_integral(expr, var, lower, upper)
    else:
        return IntegralCalculator.indefinite_integral(expr, var)

def limit(expr, var, point, direction=None):
    """Quick limit calculation"""
    return LimitCalculator.compute_limit(expr, var, point, direction)

def tangent(func, point, var=x):
    """Quick tangent line calculation"""
    return DerivativeCalculator.tangent_line(func, point, var)

# Export main classes and functions
__all__ = [
    'DerivativeCalculator',
    'IntegralCalculator', 
    'LimitCalculator',
    'SeriesCalculator',
    'NumericalMethods',
    'derivative',
    'integrate',
    'limit',
    'tangent',
    'x', 'y', 'z', 't', 'n', 'k', 'm', 'a', 'b', 'c', 'h'
]
