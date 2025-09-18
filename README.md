# Simple Calculator

A command-line calculator written in Python that performs basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)
- Command-line interface with argument parsing

## Usage

```bash
python calculator.py <operation> <number1> <number2>
```

### Examples

```bash
# Addition
python calculator.py add 5 3
# Output: 8.0

# Subtraction
python calculator.py subtract 10 4
# Output: 6.0

# Multiplication
python calculator.py multiply 3 7
# Output: 21.0

# Division
python calculator.py divide 15 3
# Output: 5.0
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

## Error Handling

The calculator includes proper error handling for:
- Division by zero
- Invalid arguments
- Incorrect number of arguments