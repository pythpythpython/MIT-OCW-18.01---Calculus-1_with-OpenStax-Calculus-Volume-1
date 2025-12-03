"""
LaTeX Rendering Utilities for MIT OCW 18.01

Provides functions for beautiful mathematical formatting in Jupyter notebooks
using LaTeX syntax with SymPy integration.
"""

import sympy as sp
from sympy import latex, simplify, expand, factor, cancel
from IPython.display import display, Math, Markdown, Latex
import re

class LatexFormatter:
    """Format mathematical expressions in LaTeX"""
    
    @staticmethod
    def format_equation(lhs, rhs, label=None):
        """Format an equation in LaTeX
        
        Args:
            lhs: Left-hand side expression
            rhs: Right-hand side expression  
            label: Optional equation label/number
            
        Returns:
            Displays formatted equation
        """
        if isinstance(lhs, str):
            lhs = sp.sympify(lhs)
        if isinstance(rhs, str):
            rhs = sp.sympify(rhs)
        
        eq_str = f"{latex(lhs)} = {latex(rhs)}"
        
        if label:
            eq_str += f" \\quad [{label}]"
        
        display(Math(eq_str))
    
    @staticmethod
    def format_derivative(func, var, order=1, evaluated=None):
        """Format derivative notation
        
        Args:
            func: Function being differentiated
            var: Variable
            order: Order of derivative
            evaluated: Optional evaluated result
            
        Returns:
            Displays formatted derivative
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        if order == 1:
            deriv_notation = f"\\frac{{d}}{{d{latex(var)}}} {latex(func)}"
        else:
            deriv_notation = f"\\frac{{d^{order}}}{{d{latex(var)}^{order}}} {latex(func)}"
        
        if evaluated is not None:
            if isinstance(evaluated, str):
                evaluated = sp.sympify(evaluated)
            deriv_str = f"{deriv_notation} = {latex(evaluated)}"
        else:
            deriv_str = deriv_notation
        
        display(Math(deriv_str))
    
    @staticmethod
    def format_integral(func, var, lower=None, upper=None, evaluated=None):
        """Format integral notation
        
        Args:
            func: Integrand
            var: Variable of integration
            lower: Optional lower limit
            upper: Optional upper limit
            evaluated: Optional evaluated result
            
        Returns:
            Displays formatted integral
        """
        if isinstance(func, str):
            func = sp.sympify(func)
        
        if lower is not None and upper is not None:
            # Definite integral
            integral_str = f"\\int_{{{latex(lower)}}}^{{{latex(upper)}}} {latex(func)} \\, d{latex(var)}"
        else:
            # Indefinite integral
            integral_str = f"\\int {latex(func)} \\, d{latex(var)}"
        
        if evaluated is not None:
            if isinstance(evaluated, str):
                evaluated = sp.sympify(evaluated)
            integral_str += f" = {latex(evaluated)}"
            if lower is None:  # Add constant for indefinite
                integral_str += " + C"
        
        display(Math(integral_str))
    
    @staticmethod
    def format_limit(expr, var, point, direction=None, evaluated=None):
        """Format limit notation
        
        Args:
            expr: Expression
            var: Variable
            point: Limit point
            direction: '+', '-', or None
            evaluated: Optional evaluated result
            
        Returns:
            Displays formatted limit
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        
        arrow = "\\to"
        if direction == '+':
            arrow += "^+"
        elif direction == '-':
            arrow += "^-"
        
        limit_str = f"\\lim_{{{latex(var)} {arrow} {latex(point)}}} {latex(expr)}"
        
        if evaluated is not None:
            if isinstance(evaluated, str):
                evaluated = sp.sympify(evaluated)
            limit_str += f" = {latex(evaluated)}"
        
        display(Math(limit_str))
    
    @staticmethod
    def format_series(expr, var, start, end=None):
        """Format series/summation notation
        
        Args:
            expr: Term expression
            var: Index variable
            start: Starting value
            end: Ending value (oo for infinity)
            
        Returns:
            Displays formatted series
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        
        if end is None:
            end = sp.oo
        
        series_str = f"\\sum_{{{latex(var)}={latex(start)}}}^{{{latex(end)}}} {latex(expr)}"
        display(Math(series_str))
    
    @staticmethod
    def format_theorem(name, statement):
        """Format a theorem statement
        
        Args:
            name: Theorem name
            statement: Theorem statement (can include LaTeX)
            
        Returns:
            Displays formatted theorem
        """
        theorem_md = f"""\n**{name}**\n\n{statement}\n"""
        display(Markdown(theorem_md))
    
    @staticmethod
    def format_definition(term, definition):
        """Format a definition
        
        Args:
            term: Term being defined
            definition: Definition text
            
        Returns:
            Displays formatted definition
        """
        def_md = f"""\n**Definition ({term})**\n\n{definition}\n"""
        display(Markdown(def_md))
    
    @staticmethod
    def format_step_by_step(steps, title="Solution Steps"):
        """Format step-by-step solution
        
        Args:
            steps: List of (description, expression) tuples
            title: Title for the solution
            
        Returns:
            Displays formatted steps
        """
        md_str = f"### {title}\n\n"
        
        for i, (description, expr) in enumerate(steps, 1):
            md_str += f"**Step {i}:** {description}\n\n"
            
            if isinstance(expr, str):
                # Plain text or already formatted LaTeX
                if '$' in expr or '\\' in expr:
                    md_str += f"{expr}\n\n"
                else:
                    try:
                        expr = sp.sympify(expr)
                        md_str += f"$${latex(expr)}$$\n\n"
                    except:
                        md_str += f"{expr}\n\n"
            else:
                # SymPy expression
                md_str += f"$${latex(expr)}$$\n\n"
        
        display(Markdown(md_str))
    
    @staticmethod
    def format_problem_solution(problem, solution_steps, answer):
        """Format complete problem with solution
        
        Args:
            problem: Problem statement
            solution_steps: List of (description, expression) tuples
            answer: Final answer
            
        Returns:
            Displays formatted problem and solution
        """
        md_str = f"""\n### Problem\n\n{problem}\n\n---\n\n### Solution\n\n"""
        
        for i, (description, expr) in enumerate(solution_steps, 1):
            md_str += f"**Step {i}:** {description}\n\n"
            
            if expr is not None:
                if isinstance(expr, str):
                    md_str += f"{expr}\n\n"
                else:
                    md_str += f"$${latex(expr)}$$\n\n"
        
        md_str += f"---\n\n### Answer\n\n"
        if isinstance(answer, str):
            md_str += f"{answer}\n"
        else:
            md_str += f"$${latex(answer)}$$\n"
        
        display(Markdown(md_str))

class ExpressionSimplifier:
    """Simplify and manipulate expressions with formatted output"""
    
    @staticmethod
    def show_simplification(expr, steps=True):
        """Show expression simplification with intermediate steps
        
        Args:
            expr: Expression to simplify
            steps: Whether to show intermediate steps
            
        Returns:
            Simplified expression
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        
        print("Original expression:")
        display(Math(latex(expr)))
        
        if steps:
            # Try different simplification approaches
            expanded = expand(expr)
            if expanded != expr:
                print("\nExpanded form:")
                display(Math(latex(expanded)))
            
            factored = factor(expr)
            if factored != expr:
                print("\nFactored form:")
                display(Math(latex(factored)))
            
            simplified = simplify(expr)
            if simplified != expr:
                print("\nSimplified form:")
                display(Math(latex(simplified)))
        
        result = simplify(expr)
        print("\nFinal result:")
        display(Math(latex(result)))
        
        return result
    
    @staticmethod
    def show_algebraic_steps(expr, target_form, steps_description=None):
        """Show algebraic manipulation steps
        
        Args:
            expr: Starting expression
            target_form: Target form
            steps_description: Optional descriptions of transformations
            
        Returns:
            Displays transformation
        """
        if isinstance(expr, str):
            expr = sp.sympify(expr)
        if isinstance(target_form, str):
            target_form = sp.sympify(target_form)
        
        print("Starting expression:")
        display(Math(latex(expr)))
        
        if steps_description:
            for desc in steps_description:
                print(f"\n{desc}")
        
        print("\nTarget form:")
        display(Math(latex(target_form)))
        
        # Verify equivalence
        if simplify(expr - target_form) == 0:
            print("\n✓ Expressions are equivalent")
        else:
            print("\n⚠ Warning: Expressions may not be equivalent")

# Convenience functions for quick formatting
def show_equation(lhs, rhs, label=None):
    """Quick equation display"""
    LatexFormatter.format_equation(lhs, rhs, label)

def show_derivative(func, var, order=1, result=None):
    """Quick derivative display"""
    LatexFormatter.format_derivative(func, var, order, result)

def show_integral(func, var, lower=None, upper=None, result=None):
    """Quick integral display"""
    LatexFormatter.format_integral(func, var, lower, upper, result)

def show_limit(expr, var, point, direction=None, result=None):
    """Quick limit display"""
    LatexFormatter.format_limit(expr, var, point, direction, result)

def show_steps(steps, title="Solution Steps"):
    """Quick step-by-step display"""
    LatexFormatter.format_step_by_step(steps, title)

# Export main classes and functions
__all__ = [
    'LatexFormatter',
    'ExpressionSimplifier',
    'show_equation',
    'show_derivative',
    'show_integral',
    'show_limit',
    'show_steps'
]
