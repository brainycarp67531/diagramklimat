import pandas as pd
import sys
import matplotlib.pyplot as plt

def generate_bar_chart(data):
    fig_width, fig_height = 16/2.54, 8/2.54

    # Expecting one row with three columns
    if data.shape[1] < 3:
        raise ValueError("CSV must have at least 3 columns for Före, Efter, and Besparing.")

    categories = ['Före', 'Efter', 'Besparing']
    values_left = data.iloc[0, 0:2].tolist()  # First two values
    value_right = data.iloc[0, 2]             # Third value

    colors_left = ['#6F895F', '#6F895F']
    color_right = '#C4D2C9'

    fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))

    bars_left = ax1.bar(categories[:2], values_left, color=colors_left, label=['Före', 'Efter'])
    # ax1.set_ylabel('Vänster Y-axel')

    ax2 = ax1.twinx()
    bar_right = ax2.bar(categories[2], value_right, color=color_right, label='Besparing')
    # ax2.set_ylabel('Höger Y-axel')

    # Add annotations
    for bar in bars_left:
        ax1.annotate(f'{bar.get_height():.2f}', (bar.get_x() + bar.get_width()/2, bar.get_height()),
                     xytext=(0, -12), textcoords="offset points", ha='center', fontsize=9)
    for bar in bar_right:
        ax2.annotate(f'{bar.get_height():.2f}', (bar.get_x() + bar.get_width()/2, bar.get_height()),
                     xytext=(0, -12), textcoords="offset points", ha='center', fontsize=9)

    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(handles1 + handles2, labels1 + labels2, loc='upper center',
               bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize=9)

    plt.title("Årlig CO₂e-besparing vid energiminskning (t CO₂e/år)")
    plt.tight_layout()
    plt.savefig('energy.png')
    plt.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: python energy.py <csv_file>")
        return

    csv_file = sys.argv[1]

    try:
        data = pd.read_csv(csv_file, index_col=0)
        generate_bar_chart(data)
        print("Bar chart generated as 'energy_chart.png'")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()