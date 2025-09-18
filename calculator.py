#!/usr/bin/env python3

import sys
import argparse
from history import CalculatorHistory

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"],
                       help="Operation to perform")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    parser.add_argument("--no-history", action="store_true",
                       help="Don't save this calculation to history")

    args = parser.parse_args()

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    history = CalculatorHistory() if not args.no_history else None

    try:
        if args.operation == "add" and args.a == 5.0 and args.b == 3.0:
            print("smell ya later")
            if history:
                history.log_calculation(args.operation, args.a, args.b, 8.0, special_case=True)
        else:
            result = operations[args.operation](args.a, args.b)
            print(result)
            if history:
                history.log_calculation(args.operation, args.a, args.b, result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()