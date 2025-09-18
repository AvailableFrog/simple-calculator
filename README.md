# Simple Calculator

A command-line calculator written in Python that performs basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)
- Command-line interface with argument parsing
- Calculation history logging with timestamps
- History viewing, statistics, and management

## Usage

```bash
python3 calculator.py <operation> <number1> <number2> [--no-history]
```

### Examples

```bash
# Addition
python3 calculator.py add 5 3
# Output: 8.0

# Subtraction
python3 calculator.py subtract 10 4
# Output: 6.0

# Multiplication
python3 calculator.py multiply 3 7
# Output: 21.0

# Division
python3 calculator.py divide 15 3
# Output: 5.0

# Calculate without saving to history
python3 calculator.py add 2 2 --no-history
# Output: 4.0
```

### Available Operations

- `add` - Add two numbers
- `subtract` - Subtract second number from first
- `multiply` - Multiply two numbers
- `divide` - Divide first number by second

## Requirements

- Python 3.x

## Installation

1. Clone the repository
2. Run the calculator with Python 3

## History Management

The calculator automatically saves calculation history to `calculator_history.json`. Use the history module to manage your calculation history:

```bash
# View calculation history
python3 history.py view

# View last 5 calculations
python3 history.py view --limit 5

# Show calculation statistics
python3 history.py stats

# Clear all history
python3 history.py clear
```

### History Features

- Automatic timestamping of all calculations
- JSON-based storage for portability
- Statistics showing operation breakdown
- Special case tracking (like easter eggs)
- Optional history disabling with `--no-history` flag

## Error Handling

The calculator includes proper error handling for:
- Division by zero
- Invalid arguments
- Incorrect number of arguments
- History file I/O errors