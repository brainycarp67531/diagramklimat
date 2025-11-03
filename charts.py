import pandas as pd
import sys
import shutil
import matplotlib.pyplot as plt
import json
from pathlib import Path


def generate_bar_chart(data, file_name, config, chart_type):
    """
    Generate and save a bar chart for either 'energi' or 'material' type.

    Parameters:
        data (pd.DataFrame): Input data with at least 3 columns.
        file_name (str): Name of the output PNG file.
        config (dict): Configuration dictionary loaded from config.json.
        chart_type (str): Either 'energi' or 'material'.
    """

    # Convert cm to inches (Matplotlib expects inches)
    fig_width, fig_height = 16 / 2.54, 8 / 2.54

    if data.shape[1] < 3:
        raise ValueError("CSV must have at least 3 columns for comparison and savings.")

    # Define labels and colors depending on chart type
    if chart_type == "energi":
        categories = ["Före", "Efter", "Besparing"]
        colors_left = ["#6F895F", "#6F895F"]
        color_right = "#C4D2C9"
        title = "Årlig CO₂e-besparing vid energiminskning (t CO₂e/år)"
        cfg_section = "energi"
    elif chart_type == "material":
        categories = ["Ny Pump", "Renoverad Pump", "Besparing"]
        colors_left = ["#6F895F", "#6F895F"]
        color_right = "#C4D2C9"
        title = "Materialrelaterad CO₂e-besparing (t CO₂e/år)"
        cfg_section = "material"
    else:
        raise ValueError("chart_type must be either 'energi' or 'material'.")

    # Extract values for plotting
    values_left = data.iloc[0, 0:2].tolist()
    value_right = data.iloc[0, 2]

    # Create the figure and two Y-axes
    fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))
    ax2 = ax1.twinx()

    # Plot bars
    bars_left = ax1.bar(categories[:2], values_left, color=colors_left, label=["Klimatavtryck", ""])
    bar_right = ax2.bar(categories[2], value_right, color=color_right, label="Besparing")

    # Add value labels
    for bar in bars_left:
        ax1.annotate(
            f"{bar.get_height():.2f}",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, -12),
            textcoords="offset points",
            ha="center",
            fontsize=9,
        )

    for bar in bar_right:
        ax2.annotate(
            f"{bar.get_height():.2f}",
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, -12),
            textcoords="offset points",
            ha="center",
            fontsize=9,
        )

    # Combine legends
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(
        handles1 + handles2,
        labels1 + labels2,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.15),
        ncol=3,
        fontsize=9,
    )

    # Add title and save
    plt.title(title)
    plt.tight_layout()

    # Save to configured output folder
    output_path = Path(config[cfg_section]["utdata"]) / file_name
    plt.savefig(output_path)
    plt.close()

    print(f"✅ Chart saved as {output_path}")


def main():
    """Unified entry point for energi and material charts."""
    if len(sys.argv) < 3:
        print("Usage: python charts.py <chart_type> <csv_file_basename>")
        print("Example: python charts.py energi mydata")
        return

    chart_type = sys.argv[1].lower()
    csv_basename = sys.argv[2]

    # Load configuration
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("❌ Error: config.json not found.")
        return
    except json.JSONDecodeError:
        print("❌ Error decoding JSON in config.json.")
        return

    # Validate chart type
    if chart_type not in config:
        print(f"❌ Error: '{chart_type}' not found in config.json.")
        return

    # Build paths
    indata = Path(config[chart_type]["indata"])
    arkiv = Path(config[chart_type]["arkiv"])
    csv_file = indata / f"{csv_basename}.csv"
    file_name = f"{csv_basename}_{chart_type}.png"

    try:
        # Read CSV
        data = pd.read_csv(csv_file, index_col=0)

        # Generate chart
        generate_bar_chart(data, file_name, config, chart_type)

        # Move CSV to archive
        arkiv.mkdir(parents=True, exist_ok=True)
        shutil.move(str(csv_file), str(arkiv / csv_file.name))
        print(f"📦 Moved '{csv_file.name}' to archive folder.")

    except FileNotFoundError:
        print(f"❌ Error: File not found: {csv_file}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
