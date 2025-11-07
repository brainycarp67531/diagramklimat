#!/usr/bin/env python3
"""
Main entry point for chart generation.

This script serves as a unified interface for generating different types of charts:
- energi: Energy-related CO2e savings (bar chart)
- material: Material-related CO2e savings (bar chart)
- livslangd: Lifespan comparison (line chart)

Usage:
    python main.py <chart_type> <csv_file_basename>

Examples:
    python main.py energi 123456
    python main.py material 456789
    python main.py livslangd 789012
"""

import sys
import subprocess


def main():
    """Main entry point that routes to the appropriate chart generator."""
    if len(sys.argv) < 3:
        print("Usage: python main.py <chart_type> <csv_file_basename>")
        print("\nChart types:")
        print("  energi     - Energy-related CO2e savings (bar chart)")
        print("  material   - Material-related CO2e savings (bar chart)")
        print("  livslangd  - Lifespan comparison (line chart)")
        print("\nExamples:")
        print("  python main.py energi 123456")
        print("  python main.py material 456789")
        print("  python main.py livslangd 789012")
        sys.exit(1)

    chart_type = sys.argv[1].lower()
    csv_basename = sys.argv[2]

    # Route to the appropriate chart generator
    if chart_type in ["energi", "material"]:
        # Both energi and material are handled by charts.py
        result = subprocess.run(
            [sys.executable, "charts.py", chart_type, csv_basename],
            capture_output=False
        )
        sys.exit(result.returncode)
    elif chart_type == "livslangd":
        # livslangd is handled by livslangd.py
        result = subprocess.run(
            [sys.executable, "livslangd.py", csv_basename],
            capture_output=False
        )
        sys.exit(result.returncode)
    else:
        print(f"❌ Error: Unknown chart type '{chart_type}'")
        print("Valid chart types: energi, material, livslangd")
        sys.exit(1)


if __name__ == "__main__":
    main()
