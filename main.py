#!/usr/bin/env python3
"""
Main entry point for chart generation.

Usage:
    python main.py [CHART_TYPE] [FILENAME]

Examples:
    python main.py energi 123456
    python main.py material 123456
    python main.py livslangd 123456

Chart types:
    - energi: Generate energy-related CO₂e savings chart
    - material: Generate material-related CO₂e savings chart
    - livslangd: Generate lifetime comparison chart
"""

import sys
import subprocess


def main():
    """Main entry point that routes to the appropriate chart generator."""
    if len(sys.argv) < 3:
        print("Usage: python main.py <chart_type> <filename>")
        print("\nChart types:")
        print("  - energi: Generate energy-related CO₂e savings chart")
        print("  - material: Generate material-related CO₂e savings chart")
        print("  - livslangd: Generate lifetime comparison chart")
        print("\nExamples:")
        print("  python main.py energi 123456")
        print("  python main.py material 123456")
        print("  python main.py livslangd 123456")
        sys.exit(1)

    chart_type = sys.argv[1].lower()
    filename = sys.argv[2]

    # Route to appropriate script based on chart type
    if chart_type in ['energi', 'material']:
        # Use charts.py for energi and material
        result = subprocess.run(
            [sys.executable, 'charts.py', chart_type, filename],
            capture_output=False
        )
        sys.exit(result.returncode)
    elif chart_type == 'livslangd':
        # Use livslangd.py for livslangd
        result = subprocess.run(
            [sys.executable, 'livslangd.py', filename],
            capture_output=False
        )
        sys.exit(result.returncode)
    else:
        print(f"❌ Error: Unknown chart type '{chart_type}'")
        print("Valid chart types: energi, material, livslangd")
        sys.exit(1)


if __name__ == "__main__":
    main()
