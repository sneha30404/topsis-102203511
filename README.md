# TOPSIS Assignment

Python implementation of the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** algorithm, a popular method for multi-criteria decision-making. TOPSIS ranks alternatives based on their proximity to the ideal solution and distance from the worst-case solution, making it widely applicable in decision-making scenarios.

## Features
- Normalize the decision matrix for comparability.
- Apply weights to criteria to adjust their importance.
- Calculate distances to the ideal best and worst solutions.
- Generate scores and rank alternatives.

## Installation

Install the package directly from PyPI using `pip`:

```bash
pip install topsis-102203511
```

## How to Use
Input Format
- Prepare your data in a CSV file.
- Use the installation directly or enter code in CLI.
- 
## Command-Line Interface (CLI)
The package also supports a command-line interface for convenience. For Example:

```bash
topsis input.csv "0.4,0.3,0.2,0.1" "max,max,min,max" output.csv
```
- Replace input.csv with the path to your dataset.
- Specify weights and criteria as comma-separated strings.
- Results are saved in output.csv.

## Testing
Run tests to validate functionality:

```bash
python -m unittest discover tests
```

