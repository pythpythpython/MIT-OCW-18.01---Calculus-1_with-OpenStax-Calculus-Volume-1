#!/usr/bin/env python3
"""
Scaffolding Generator for MIT OCW 18.01 Calculus Repository
Creates the complete directory structure and template Jupyter notebooks
"""

import os
import json
from pathlib import Path

# Base directory
BASE_DIR = Path("/workspaces/MIT-OCW-18.01---Calculus-1_with-OpenStax-Calculus-Volume-1")

# Course structure mapping
COURSE_STRUCTURE = {
    "unit-01-derivatives": {
        "lectures": [
            {"num": 1, "title": "derivatives-slope-velocity", "openstax": ["3.1", "3.2"]},
            {"num": 2, "title": "limits-continuity", "openstax": ["2.2", "2.3", "2.4"]},
            {"num": 3, "title": "derivatives-products-quotients", "openstax": ["3.3", "3.4"]},
            {"num": 4, "title": "chain-rule", "openstax": ["3.5", "3.6"]},
            {"num": 5, "title": "implicit-differentiation", "openstax": ["3.7", "3.8"]},
            {"num": 6, "title": "exponential-logarithmic", "openstax": ["3.9"]},
            {"num": 7, "title": "exam-01-review", "openstax": []},
        ],
        "exam": "exam-01"
    },
    "unit-02-applications-differentiation": {
        "lectures": [
            {"num": 9, "title": "linear-quadratic-approximations", "openstax": ["4.2"]},
            {"num": 10, "title": "curve-sketching", "openstax": ["4.5"]},
            {"num": 11, "title": "max-min-problems", "openstax": ["4.7"]},
            {"num": 12, "title": "related-rates", "openstax": ["4.1"]},
            {"num": 13, "title": "newtons-method", "openstax": ["4.9"]},
            {"num": 14, "title": "mean-value-theorem", "openstax": ["4.4"]},
            {"num": 15, "title": "differential-equations-separation", "openstax": ["4.10"]},
            {"num": 16, "title": "differential-equations-first-order", "openstax": ["4.10"]},
        ],
        "exam": "exam-02"
    },
    "unit-03-integration": {
        "lectures": [
            {"num": 18, "title": "definite-integrals", "openstax": ["5.1", "5.2"]},
            {"num": 19, "title": "fundamental-theorem-part1", "openstax": ["5.3"]},
            {"num": 20, "title": "fundamental-theorem-part2", "openstax": ["5.3"]},
            {"num": 21, "title": "applications-to-geometry", "openstax": ["6.1", "6.2"]},
            {"num": 22, "title": "volumes-disks-shells", "openstax": ["6.3"]},
            {"num": 23, "title": "work-average-value", "openstax": ["6.4", "6.5"]},
            {"num": 24, "title": "numerical-integration", "openstax": ["5.5"]},
        ],
        "exam": "exam-03"
    },
    "unit-04-techniques-integration": {
        "lectures": [
            {"num": 26, "title": "trigonometric-substitution", "openstax": ["3.5-Vol2"]},
            {"num": 27, "title": "integration-techniques-1", "openstax": ["3.1-Vol2"]},
            {"num": 28, "title": "integration-techniques-2", "openstax": ["3.2-Vol2"]},
            {"num": 29, "title": "integration-by-parts", "openstax": ["3.1-Vol2"]},
            {"num": 30, "title": "parametric-equations", "openstax": ["7.1-Vol2"]},
            {"num": 31, "title": "polar-coordinates", "openstax": ["7.3-Vol2"]},
            {"num": 32, "title": "indeterminate-forms", "openstax": ["4.8-Vol2"]},
            {"num": 33, "title": "improper-integrals", "openstax": ["3.7-Vol2"]},
            {"num": 34, "title": "infinite-series", "openstax": ["5.1-Vol2"]},
            {"num": 35, "title": "taylor-series", "openstax": ["6.3-Vol2"]},
        ],
        "exam": "exam-04"
    }
}

# Problem sets mapping (9 problem sets total)
PROBLEM_SETS = [
    {"num": 1, "lectures": [1, 2]},
    {"num": 2, "lectures": [3, 4, 5]},
    {"num": 3, "lectures": [9, 10]},
    {"num": 4, "lectures": [11, 12, 13]},
    {"num": 5, "lectures": [18, 19, 20]},
    {"num": 6, "lectures": [21, 22, 23]},
    {"num": 7, "lectures": [26, 27, 28]},
    {"num": 8, "lectures": [29, 30, 31]},
    {"num": 9, "lectures": [32, 33, 34]},
]

def create_notebook_template(title, notebook_type, description=""):
    """Create a Jupyter notebook template with proper structure"""
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [f"# {title}\n", "\n", f"{description}\n"]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## Setup\n"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import sympy as sp\n",
                "from sympy import *\n",
                "import sys\n",
                "sys.path.append('../../utils')\n",
                "from calculus_utils import *\n",
                "from plotting_utils import *\n",
                "\n",
                "# Initialize pretty printing\n",
                "sp.init_printing(use_latex='mathjax')\n",
                "\n",
                "# Matplotlib settings\n",
                "plt.style.use('seaborn-v0_8-darkgrid')\n",
                "plt.rcParams['figure.figsize'] = (10, 6)\n"
            ]
        }
    ]
    
    if notebook_type == "dashboard":
        cells.extend([
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Learning Objectives\n", "\n", "1. [Add objective here]\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Prerequisites\n", "\n", "- [ ] [Add prerequisite here]\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Resources\n", "\n", "- [Link to resource]\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Progress Tracker\n", "\n", "- [ ] Lecture notes reviewed\n", "- [ ] Textbook sections completed\n", "- [ ] Problems attempted\n"]
            }
        ])
    elif notebook_type == "lecture":
        cells.extend([
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Lecture Content\n", "\n", "[Lecture notes will go here]\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Key Concepts\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Examples\n"]
            }
        ])
    elif notebook_type == "textbook":
        cells.extend([
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Definitions\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Theorems\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Worked Examples\n"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Exercises\n"]
            }
        ])
    elif notebook_type == "problems":
        cells.extend([
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Problem 1\n", "\n", "### Problem Statement\n", "\n", "### Concepts Being Tested\n", "\n", "### Solution Strategy\n", "\n", "### Detailed Solution\n", "\n", "### Alternative Approaches\n", "\n", "### Common Mistakes\n", "\n", "### Verification\n"]
            }
        ])
    
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    return notebook

def create_lecture_folder(unit_path, lecture_info):
    """Create a complete lecture folder with all notebooks"""
    lecture_num = lecture_info["num"]
    lecture_title = lecture_info["title"]
    openstax_sections = lecture_info["openstax"]
    
    lecture_folder = unit_path / f"lecture-{lecture_num:02d}-{lecture_title}"
    lecture_folder.mkdir(parents=True, exist_ok=True)
    
    print(f"  Creating Lecture {lecture_num}: {lecture_title}")
    
    # 1. Overview Master Dashboard
    nb = create_notebook_template(
        f"Lecture {lecture_num}: {lecture_title.replace('-', ' ').title()} - Overview",
        "dashboard",
        f"Master dashboard for tracking progress through Lecture {lecture_num}"
    )
    with open(lecture_folder / "01_Overview_Master_Dashboard.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # 2. MIT Lecture Notes
    nb = create_notebook_template(
        f"Lecture {lecture_num}: MIT Lecture Notes",
        "lecture",
        "Complete lecture notes from MIT OCW with examples and insights"
    )
    with open(lecture_folder / "02_Lecture_Notes_MIT.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # 3-N. OpenStax Chapter Sections
    file_num = 3
    for section in openstax_sections:
        nb = create_notebook_template(
            f"OpenStax Section {section}",
            "textbook",
            f"Comprehensive coverage of OpenStax Calculus Volume 1, Section {section}"
        )
        section_safe = section.replace(".", "-")
        with open(lecture_folder / f"{file_num:02d}_OpenStax_Ch{section_safe}.ipynb", "w") as f:
            json.dump(nb, f, indent=2)
        file_num += 1
    
    # Problem Set Activities (if this lecture has associated problems)
    nb = create_notebook_template(
        f"Lecture {lecture_num}: Problem Set Activities",
        "problems",
        "Selected problems from problem sets with detailed solutions"
    )
    with open(lecture_folder / f"{file_num:02d}_Problem_Set_Activities.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    file_num += 1
    
    # Flashcards
    nb = create_notebook_template(
        f"Lecture {lecture_num}: Flashcards",
        "activity",
        "Interactive flashcards for active recall and spaced repetition"
    )
    with open(lecture_folder / f"{file_num:02d}_Activity_Flashcards.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    file_num += 1
    
    # Interactive Playground
    nb = create_notebook_template(
        f"Lecture {lecture_num}: Interactive Playground",
        "activity",
        "Interactive visualizations and explorations of key concepts"
    )
    with open(lecture_folder / f"{file_num:02d}_Activity_Interactive_Playground.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    file_num += 1
    
    # Exercise Bank
    nb = create_notebook_template(
        f"Lecture {lecture_num}: Exercise Bank",
        "problems",
        "Additional practice problems with varying difficulty levels"
    )
    with open(lecture_folder / f"{file_num:02d}_Activity_Exercise_Bank.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    file_num += 1
    
    # AI Q&A Journal
    nb = create_notebook_template(
        f"Lecture {lecture_num}: AI Q&A Journal",
        "activity",
        "Questions, insights, and connections discovered during study"
    )
    with open(lecture_folder / f"{file_num:02d}_Log_AI_QA_Journal.ipynb", "w") as f:
        json.dump(nb, f, indent=2)

def create_problem_set_folder(ps_folder, ps_info):
    """Create a problem set folder with detailed solution notebooks"""
    ps_num = ps_info["num"]
    ps_path = ps_folder / f"ps{ps_num:02d}"
    ps_path.mkdir(parents=True, exist_ok=True)
    
    print(f"  Creating Problem Set {ps_num}")
    
    # Overview
    nb = create_notebook_template(
        f"Problem Set {ps_num}: Overview",
        "dashboard",
        f"Problem set {ps_num} covering lectures {ps_info['lectures']}"
    )
    with open(ps_path / "00_Overview.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # Problems 1-5 (Part 1)
    nb = create_notebook_template(
        f"Problem Set {ps_num}: Problems 1-5",
        "problems",
        "Detailed solutions for problems 1-5 with full explanations"
    )
    with open(ps_path / "01_Problems_1-5_Detailed.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # Problems 6-10 (Part 2)
    nb = create_notebook_template(
        f"Problem Set {ps_num}: Problems 6-10",
        "problems",
        "Detailed solutions for problems 6-10 with full explanations"
    )
    with open(ps_path / "02_Problems_6-10_Detailed.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # Complete Solutions
    nb = create_notebook_template(
        f"Problem Set {ps_num}: Complete Solutions",
        "problems",
        "Comprehensive solutions reference for all problems"
    )
    with open(ps_path / "03_Solutions_Complete.ipynb", "w") as f:
        json.dump(nb, f, indent=2)

def create_exam_folder(exam_folder, exam_name):
    """Create an exam folder with practice and solutions"""
    exam_path = exam_folder / exam_name
    exam_path.mkdir(parents=True, exist_ok=True)
    
    print(f"  Creating {exam_name}")
    
    # Practice Exam
    nb = create_notebook_template(
        f"{exam_name.replace('-', ' ').title()}: Practice Exam",
        "problems",
        "Practice problems in exam format"
    )
    with open(exam_path / "01_Practice_Exam.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # Solutions Part 1
    nb = create_notebook_template(
        f"{exam_name.replace('-', ' ').title()}: Solutions Part 1",
        "problems",
        "Detailed solutions for first half of exam"
    )
    with open(exam_path / "02_Solutions_Part1.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # Solutions Part 2
    nb = create_notebook_template(
        f"{exam_name.replace('-', ' ').title()}: Solutions Part 2",
        "problems",
        "Detailed solutions for second half of exam"
    )
    with open(exam_path / "03_Solutions_Part2.ipynb", "w") as f:
        json.dump(nb, f, indent=2)
    
    # Review Guide
    nb = create_notebook_template(
        f"{exam_name.replace('-', ' ').title()}: Review Guide",
        "dashboard",
        "Comprehensive review guide and study strategies"
    )
    with open(exam_path / "04_Review_Guide.ipynb", "w") as f:
        json.dump(nb, f, indent=2)

def main():
    """Main scaffolding generation function"""
    print("=" * 60)
    print("MIT OCW 18.01 Calculus Repository Scaffolding Generator")
    print("=" * 60)
    print()
    
    # Create utils directory
    print("Creating utilities directory...")
    utils_dir = BASE_DIR / "utils"
    utils_dir.mkdir(parents=True, exist_ok=True)
    
    # Create units and lectures
    print("\nCreating unit and lecture structure...")
    for unit_name, unit_data in COURSE_STRUCTURE.items():
        print(f"\n{unit_name.upper()}")
        unit_path = BASE_DIR / unit_name
        unit_path.mkdir(parents=True, exist_ok=True)
        
        # Create lectures
        for lecture_info in unit_data["lectures"]:
            create_lecture_folder(unit_path, lecture_info)
    
    # Create problem sets
    print("\n\nCreating problem set structure...")
    print("PROBLEM-SETS")
    ps_folder = BASE_DIR / "problem-sets"
    ps_folder.mkdir(parents=True, exist_ok=True)
    
    for ps_info in PROBLEM_SETS:
        create_problem_set_folder(ps_folder, ps_info)
    
    # Create exams
    print("\n\nCreating exam structure...")
    print("EXAMS")
    exam_folder = BASE_DIR / "exams"
    exam_folder.mkdir(parents=True, exist_ok=True)
    
    for unit_name, unit_data in COURSE_STRUCTURE.items():
        create_exam_folder(exam_folder, unit_data["exam"])
    
    # Create final exam
    create_exam_folder(exam_folder, "final-exam")
    
    # Create supplementary folders
    print("\n\nCreating supplementary directories...")
    print("SUPPLEMENTARY")
    supp_folder = BASE_DIR / "supplementary"
    (supp_folder / "course-reader-notes").mkdir(parents=True, exist_ok=True)
    (supp_folder / "reference-materials").mkdir(parents=True, exist_ok=True)
    (supp_folder / "additional-resources").mkdir(parents=True, exist_ok=True)
    print("  Created course-reader-notes")
    print("  Created reference-materials")
    print("  Created additional-resources")
    
    # Create README files
    print("\n\nCreating README files...")
    for unit_name in COURSE_STRUCTURE.keys():
        unit_path = BASE_DIR / unit_name
        readme_path = unit_path / "README.md"
        with open(readme_path, "w") as f:
            f.write(f"# {unit_name.replace('-', ' ').title()}\n\n")
            f.write("This unit contains lecture folders with comprehensive materials.\n")
    
    print("\n" + "=" * 60)
    print("Scaffolding generation complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Install requirements: pip install -r requirements.txt")
    print("2. Review the structure in your file explorer")
    print("3. Start filling in content with lecture materials")
    print("\nTotal notebooks created: Approximately 200+ notebooks")
    print("=" * 60)

if __name__ == "__main__":
    main()
