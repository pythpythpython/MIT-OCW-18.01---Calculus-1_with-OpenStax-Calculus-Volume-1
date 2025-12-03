# MIT OCW 18.01 Single Variable Calculus with OpenStax Calculus Volume 1

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## 📚 Overview

This repository provides a comprehensive, academically rigorous study framework for **MIT OCW 18.01 Single Variable Calculus** (Fall 2006) integrated with **OpenStax Calculus Volume 1**. The structure follows pedagogical best practices including spaced repetition, active recall, deliberate practice, and the Feynman Technique.

### Course Information
- **Course**: MIT 18.01 - Single Variable Calculus
- **Instructor**: Prof. David Jerison
- **Textbook**: OpenStax Calculus Volume 1 (Open Educational Resource)
- **Format**: Jupyter Notebooks with detailed explanations, code, and visualizations

## 🎯 Learning Methodology

This repository implements evidence-based learning techniques:

### 1. **Spaced Repetition & Active Recall**
- Interactive flashcard notebooks for key concepts
- Progressive review systems
- Incremental difficulty scaling

### 2. **Feynman Technique**
- Concepts explained from first principles
- Clear, simple language before technical terminology
- "Teach to learn" approach in notebooks

### 3. **Deliberate Practice**
- 5 problems per notebook with exhaustive analysis
- Multiple solution methods
- Common mistakes highlighted
- Pattern recognition development

### 4. **Interleaving**
- Mixed problem types within sets
- Cross-topic connections
- Review of previous material in new contexts

### 5. **Multi-Modal Learning**
- Visual representations (matplotlib/plotly)
- Symbolic manipulation (SymPy)
- Numerical computation (NumPy)
- Interactive widgets (ipywidgets)

## 📂 Repository Structure

```
MIT-OCW-18.01---Calculus-1_with-OpenStax-Calculus-Volume-1/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── create_scaffolding.py             # Scaffolding generation script
├── course_overview.md                # Detailed course mapping
│
├── utils/                            # Utility functions
│   ├── calculus_utils.py            # Calculus-specific functions
│   ├── plotting_utils.py            # Visualization helpers
│   └── latex_rendering.py           # LaTeX formatting utilities
│
├── unit-01-derivatives/              # Unit 1: Derivatives
│   ├── lecture-01-derivatives-slope-velocity/
│   │   ├── 01_Overview_Master_Dashboard.ipynb
│   │   ├── 02_Lecture_Notes_MIT.ipynb
│   │   ├── 03_OpenStax_Ch3-1_Defining_Derivative.ipynb
│   │   ├── 04_OpenStax_Ch3-2_Derivative_as_Function.ipynb
│   │   ├── 05_Problem_Set_Activities.ipynb
│   │   ├── 06_Activity_Flashcards.ipynb
│   │   ├── 07_Activity_Interactive_Playground.ipynb
│   │   ├── 08_Activity_Exercise_Bank.ipynb
│   │   └── 09_Log_AI_QA_Journal.ipynb
│   ├── lecture-02-limits-continuity/
│   └── [lectures 3-7...]
│
├── unit-02-applications-differentiation/  # Unit 2: Applications
│   └── [lectures 9-16...]
│
├── unit-03-integration/              # Unit 3: Integration
│   └── [lectures 18-24...]
│
├── unit-04-techniques-integration/   # Unit 4: Advanced Techniques
│   └── [lectures 26-35...]
│
├── problem-sets/                     # Problem Sets 1-9
│   ├── ps01/
│   │   ├── 00_Overview.ipynb
│   │   ├── 01_Problems_1-5_Detailed.ipynb
│   │   ├── 02_Problems_6-10_Detailed.ipynb
│   │   └── 03_Solutions_Complete.ipynb
│   └── [ps02-ps09...]
│
├── exams/                            # Exam Materials
│   ├── exam-01/
│   ├── exam-02/
│   ├── exam-03/
│   ├── exam-04/
│   └── final-exam/
│
└── supplementary/                    # Additional Resources
    ├── course-reader-notes/
    ├── reference-materials/
    └── additional-resources/
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Jupyter Lab or Jupyter Notebook
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pythpythpython/MIT-OCW-18.01---Calculus-1_with-OpenStax-Calculus-Volume-1.git
   cd MIT-OCW-18.01---Calculus-1_with-OpenStax-Calculus-Volume-1
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate the scaffolding** (if not already present)
   ```bash
   python create_scaffolding.py
   ```

5. **Launch Jupyter Lab**
   ```bash
   jupyter lab
   ```

## 📖 How to Use This Repository

### For Each Lecture:

1. **Start with the Overview Dashboard** (`01_Overview_Master_Dashboard.ipynb`)
   - Review learning objectives
   - Check prerequisites
   - Track your progress

2. **Study MIT Lecture Notes** (`02_Lecture_Notes_MIT.ipynb`)
   - Complete notes from Prof. Jerison
   - Key insights and examples

3. **Read OpenStax Textbook Sections** (`03-XX_OpenStax_ChX-X.ipynb`)
   - Definitions with examples
   - Theorems with proofs
   - Worked examples step-by-step

4. **Practice with Problem Sets** (`XX_Problem_Set_Activities.ipynb`)
   - 5 problems with complete solutions
   - Multiple approaches shown
   - Common mistakes highlighted

5. **Use Active Learning Tools**
   - **Flashcards**: Spaced repetition practice
   - **Interactive Playground**: Visualizations and explorations
   - **Exercise Bank**: Additional practice problems

6. **Maintain Learning Journal** (`XX_Log_AI_QA_Journal.ipynb`)
   - Record questions and insights
   - Track confusing concepts
   - Note connections between topics

### For Problem Sets:

- Each problem set is divided into manageable chunks (5 problems each)
- Every problem includes:
  - Clear problem statement
  - Concepts being tested
  - Multiple solution strategies
  - Step-by-step detailed solution
  - Alternative approaches
  - Common mistakes to avoid
  - Computational verification

### For Exams:

- Practice exams in exam format
- Solutions split into parts for self-paced learning
- Comprehensive review guides
- Study strategies and tips

## 🎓 Course Outline

### Unit 1: Derivatives (Lectures 1-7)
- Derivatives, slopes, velocity
- Limits and continuity
- Derivatives of products and quotients
- Chain rule
- Implicit differentiation
- Exponential and logarithmic functions

### Unit 2: Applications of Differentiation (Lectures 9-16)
- Linear and quadratic approximations
- Curve sketching
- Optimization problems
- Related rates
- Newton's method
- Mean value theorem
- Differential equations

### Unit 3: Integration (Lectures 18-24)
- Definite integrals
- Fundamental theorem of calculus
- Applications to geometry
- Volumes (disks and shells)
- Work and average value
- Numerical integration

### Unit 4: Techniques of Integration (Lectures 26-35)
- Trigonometric substitution
- Integration by parts
- Parametric equations
- Polar coordinates
- L'Hôpital's rule
- Improper integrals
- Series and Taylor series

## 📊 Progress Tracking

Each lecture folder contains:
- ✅ Overview Dashboard with checkboxes
- 📝 Learning objectives
- 🎯 Progress indicators
- 🔗 Resource links

## 🛠️ Utility Functions

The `utils/` directory contains helper functions:

- **calculus_utils.py**: Derivative/integral calculators, limit evaluators
- **plotting_utils.py**: Function plotters, tangent line visualizers
- **latex_rendering.py**: Beautiful equation formatting

## 📚 Resources

### Primary Sources
- [MIT OCW 18.01 Course Page](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/)
- [OpenStax Calculus Volume 1](https://openstax.org/details/books/calculus-volume-1)

### Additional References
- MIT Course Reader (supplementary notes)
- Problem sets with solutions
- Past exams

## 🤝 Contributing

This is a personal learning repository, but suggestions and corrections are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
- MIT OpenCourseWare for providing free, high-quality educational resources
- OpenStax for their open-access calculus textbook
- Prof. David Jerison for excellent lectures
- Inspired by [The Feynman Lectures on Physics repository structure](https://github.com/pythpythpython/The_Feynman_Lectures_on_Physics)

## 📧 Contact

Questions or feedback? Open an issue on GitHub!

---

**Note**: This repository is for educational purposes. All course materials are from MIT OpenCourseWare (licensed under Creative Commons) and OpenStax (open educational resource).

---

## 🎯 Study Tips

1. **Consistency over intensity**: Study daily rather than cramming
2. **Active engagement**: Work through examples yourself before reading solutions
3. **Space out practice**: Use the flashcards and exercise banks regularly
4. **Connect concepts**: Use the AI Q&A Journal to build mental models
5. **Visualize**: Run the interactive playgrounds to build intuition
6. **Teach others**: Explain concepts to solidify understanding

**Happy Learning! 📐✨**
