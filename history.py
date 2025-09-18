#!/usr/bin/env python3

import os
import json
from datetime import datetime
from typing import List, Dict, Any

class CalculatorHistory:
    def __init__(self, history_file: str = "calculator_history.json"):
        self.history_file = history_file
        self.history_data = self._load_history()

    def _load_history(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def _save_history(self) -> None:
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history_data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save history: {e}")

    def log_calculation(self, operation: str, a: float, b: float, result: float, special_case: bool = False) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "operand_a": a,
            "operand_b": b,
            "result": result,
            "special_case": special_case
        }
        self.history_data.append(entry)
        self._save_history()

    def get_history(self, limit: int = None) -> List[Dict[str, Any]]:
        if limit:
            return self.history_data[-limit:]
        return self.history_data

    def clear_history(self) -> int:
        count = len(self.history_data)
        self.history_data = []
        self._save_history()
        return count

    def format_entry(self, entry: Dict[str, Any]) -> str:
        timestamp = datetime.fromisoformat(entry["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        if entry.get("special_case"):
            return f"[{timestamp}] {entry['operand_a']} {entry['operation']} {entry['operand_b']} = <special case>"
        else:
            return f"[{timestamp}] {entry['operand_a']} {entry['operation']} {entry['operand_b']} = {entry['result']}"

    def display_history(self, limit: int = None) -> None:
        history = self.get_history(limit)
        if not history:
            print("No calculation history found.")
            return

        print("Calculation History:")
        print("-" * 50)
        for entry in history:
            print(self.format_entry(entry))

    def get_stats(self) -> Dict[str, Any]:
        if not self.history_data:
            return {"total_calculations": 0}

        operations_count = {}
        for entry in self.history_data:
            op = entry["operation"]
            operations_count[op] = operations_count.get(op, 0) + 1

        return {
            "total_calculations": len(self.history_data),
            "operations_breakdown": operations_count,
            "first_calculation": self.history_data[0]["timestamp"] if self.history_data else None,
            "last_calculation": self.history_data[-1]["timestamp"] if self.history_data else None
        }

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Calculator History Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    view_parser = subparsers.add_parser("view", help="View calculation history")
    view_parser.add_argument("--limit", type=int, help="Limit number of entries to show")

    subparsers.add_parser("clear", help="Clear all calculation history")
    subparsers.add_parser("stats", help="Show calculation statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    history = CalculatorHistory()

    if args.command == "view":
        history.display_history(args.limit)
    elif args.command == "clear":
        count = history.clear_history()
        print(f"Cleared {count} calculation(s) from history.")
    elif args.command == "stats":
        stats = history.get_stats()
        if stats["total_calculations"] == 0:
            print("No calculations in history.")
        else:
            print(f"Total calculations: {stats['total_calculations']}")
            print("Operations breakdown:")
            for op, count in stats["operations_breakdown"].items():
                print(f"  {op}: {count}")
            if stats["first_calculation"]:
                first = datetime.fromisoformat(stats["first_calculation"]).strftime("%Y-%m-%d %H:%M:%S")
                last = datetime.fromisoformat(stats["last_calculation"]).strftime("%Y-%m-%d %H:%M:%S")
                print(f"First calculation: {first}")
                print(f"Last calculation: {last}")

if __name__ == "__main__":
    main()