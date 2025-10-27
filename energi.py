import pandas as pd
import sys
import matplotlib.pyplot as plt

def generate_bar_chart(data, xlabel="X-axis", ylabel="Y-axis"):
    plt.figure(figsize=(10, 6))
    
    # Set the color for the bars. 
    colors = ["#6F895F", '#C4D2C9']
    
    ax = data.plot(kind='bar', color=colors)
    plt.title("Energianvändning (t CO2e/år)")
    # Sätt egna etiketter om det finns exakt två indexrader
    if len(data.index) == 2:
        ax.set_xticks(range(len(data.index)))
        # Sätter etiketterna under varje stapel. 
        ax.set_xticklabels(['Före', 'Efter'])
    else:
        ax.set_xticklabels(data.index.astype(str), rotation=0)
    plt.xticks(rotation=0)

    # --- Lägg till värden över varje stapel ---
    for p in ax.patches:
        height = p.get_height()
        # hoppa över NaN
        if pd.isna(height):
            continue
        ax.annotate(f'{height:.2f}',  # Changed from .0f to .2f to show two decimal place
                    (p.get_x() + p.get_width() / 2, height),
                    xytext=(0, 3),  # offset i punkter
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=9)
    # ------------------------------------

    plt.tight_layout()
    plt.savefig('bar_chart.png')
    plt.close()

def main():
    if len(sys.argv) < 2:
        print("Usage: python energi.py <csv_file>")
        return

    csv_file = sys.argv[1]

    try:
        data = pd.read_csv(csv_file)
        generate_bar_chart(data)
        print("Bar chart generated as 'bar_chart.png'")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()