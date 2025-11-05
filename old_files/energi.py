import pandas as pd
import sys
import shutil
import matplotlib.pyplot as plt
import json
from pathlib import Path


def generate_bar_chart(data, file_name, config):
    """
    Generate and save a bar chart comparing 'Före', 'Efter', and 'Besparing'.

    Parameters:
        data (pd.DataFrame): Input data containing at least three columns.
        file_name (str): Name of the PNG file to save.
        config (dict): Configuration dictionary loaded from config.json.
    """
    # Convert cm to inches (Matplotlib expects inches)
    fig_width, fig_height = 16 / 2.54, 8 / 2.54

    # Expecting one row with at least three columns (Före, Efter, Besparing)
    if data.shape[1] < 3:
        raise ValueError("CSV must have at least 3 columns: Före, Efter, and Besparing.")

    categories = ['Före', 'Efter', 'Besparing']

    # Extract values for plotting
    values_left = data.iloc[0, 0:2].tolist()  # First two values (Före, Efter)
    value_right = data.iloc[0, 2]             # Third value (Besparing)

    # Define colors for bars
    colors_left = ['#6F895F', '#6F895F']      # Darker green for Före/Efter
    color_right = '#C4D2C9'                   # Lighter green for Besparing

    # Create the figure and two Y-axes (shared X-axis)
    fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))
    ax2 = ax1.twinx()

    # Plot 'Före' and 'Efter' on left axis
    bars_left = ax1.bar(categories[:2], values_left, color=colors_left, label=['Klimatavtryck', ''])

    # Plot 'Besparing' on right axis
    bar_right = ax2.bar(categories[2], value_right, color=color_right, label='Besparing')

    # Add value labels on top of bars
    for bar in bars_left:
        ax1.annotate(
            f'{bar.get_height():.2f}',
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, -12),
            textcoords="offset points",
            ha='center',
            fontsize=9
        )

    for bar in bar_right:
        ax2.annotate(
            f'{bar.get_height():.2f}',
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, -12),
            textcoords="offset points",
            ha='center',
            fontsize=9
        )

    # Combine legends from both axes
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(
        handles1 + handles2,
        labels1 + labels2,
        loc='upper center',
        bbox_to_anchor=(0.5, -0.15),
        ncol=3,
        fontsize=9
    )

    # Set title and layout
    plt.title("Årlig CO₂e-besparing vid energiminskning (t CO₂e/år)")
    plt.tight_layout()

    # Save to output folder specified in config
    output_path = Path(config["energi"]["utdata"]) / file_name
    plt.savefig(output_path)
    plt.close()

    print(f"Chart saved as {output_path}")


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python energi.py <csv_file_basename>")
        return

    # Load configuration
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: config.json not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON in config.json.")
        return

    # Build folder paths from config
    indata = Path(config["energi"]["indata"])
    arkiv = Path(config["energi"]["arkiv"])

    # Construct CSV and output file names
    csv_file = indata / f"{sys.argv[1]}.csv"
    file_name = f"{sys.argv[1]}_energi.png"

    try:
        # Read CSV
        data = pd.read_csv(csv_file, index_col=0)

        # Generate bar chart
        generate_bar_chart(data, file_name, config)

        # Move the CSV file to the archive folder
        arkiv.mkdir(parents=True, exist_ok=True)
        shutil.move(str(csv_file), str(arkiv / csv_file.name))
        print(f"Moved '{csv_file.name}' to archive folder.")

    except FileNotFoundError:
        print(f"Error: File not found: {csv_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
