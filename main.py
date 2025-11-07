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
from pathlib import Path


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

    # Determine which script to use based on chart type
    if chart_type in ["energi", "material"]:
        script_name = "charts.py"
        script_args = [chart_type, csv_basename]
    elif chart_type == "livslangd":
        script_name = "livslangd.py"
        script_args = [csv_basename]
    else:
        print(f"❌ Error: Unknown chart type '{chart_type}'")
        print("Valid chart types: energi, material, livslangd")
        sys.exit(1)

    # Verify the target script exists
    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        print(f"❌ Error: Required script '{script_name}' not found")
        sys.exit(1)

    # Run the appropriate chart generator
    result = subprocess.run(
        [sys.executable, script_name] + script_args,
        capture_output=False
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
