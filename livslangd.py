import pandas as pd
import sys
import shutil
import matplotlib.pyplot as plt
import json
from pathlib import Path

LINEWIDTH = 2


def generate_line_chart(data, file_name, config):
    """
    Generate and save a line chart comparing 'Ny Pump', 'Renoverad Pump', and 'Besparing',
    where 'Besparing' is plotted on a secondary Y-axis.
    """

    # Convert cm to inches (Matplotlib expects inches)
    fig_width, fig_height = 32 / 2.54, 8 / 2.54

    # Expect at least three required columns
    required_columns = ['Ny Pump', 'Renoverad Pump', 'Besparing']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Missing required column: '{col}'")

    # Create figure and two Y-axes
    fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))
    ax2 = ax1.twinx()  # Secondary Y-axis for 'Besparing'

    # --- Left axis (Ny Pump & Renoverad Pump) --- Filled 
    # ax1.fill_between(
    #     data.index, data['Ny Pump'], alpha=0.4, color='#6F895F', label='Ny Pump'
    # )
    # ax1.fill_between(
    #     data.index, data['Renoverad Pump'], alpha=0.4, color='#4E5E40', label='Renoverad Pump'
    # )

    # --- Left axis (Ny Pump & Renoverad Pump) --- Line 
    ax1.plot(
        data.index, data['Ny Pump'],
        marker='', label='Ny Pump', color='#6F895F', linewidth=LINEWIDTH
    )
    ax1.plot(
        data.index, data['Renoverad Pump'],
        marker='', label='Renoverad Pump', color='#4E5E40', linewidth=LINEWIDTH
    )
    ax1.set_xlabel("Månader", fontsize=10)
    ax1.set_ylabel("t CO₂e/år (Pumpar)", fontsize=10, color='#4E5E40')
    ax1.tick_params(axis='y', labelcolor='#4E5E40')
    ax1.grid(True, linestyle='--', alpha=0.6)

    # --- Right axis (Besparing) --- Filled
    # ax2.fill_between(
    #    data.index, data['Besparing'], alpha=0.3, color='#C4D2C9', label='Besparing'
    # )
    # --- Right axis (Besparing) --- Line    
    ax2.plot(
        data.index, data['Besparing'],
        marker='', label='Besparing', color='#C4D2C9', linewidth=LINEWIDTH
    )
    ax2.set_ylabel("Besparing (t CO₂e/år)", fontsize=10, color='#C4D2C9')
    ax2.tick_params(axis='y', labelcolor='#C4D2C9')

    # --- Combine legends from both axes ---
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='best', fontsize=9)

    # --- Title & layout ---
    plt.title("Livslängd – Ny Pump, Renoverad Pump, Besparing", fontsize=12)
    plt.tight_layout()

    # --- Save output ---
    output_path = Path(config["livslangd"]["utdata"]) / file_name
    plt.savefig(output_path)
    plt.close()
    print(f"Chart saved as {output_path}")


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python livslangd.py <csv_file_basename>")
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
    indata = Path(config["livslangd"]["indata"])
    arkiv = Path(config["livslangd"]["arkiv"])

    # Construct CSV and output file names
    csv_file = indata / f"{sys.argv[1]}.csv"
    file_name = f"{sys.argv[1]}_livslangd.png"

    try:
        # Read CSV
        data = pd.read_csv(csv_file)

        # Generate line chart
        generate_line_chart(data, file_name, config)

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
