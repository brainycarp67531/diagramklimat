import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import sys

import matplotlib.pyplot as plt

def generate_bar_chart(data, title="Bar Chart", xlabel="X-axis", ylabel="Y-axis"):
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_chart.png')
    plt.close()

def generate_surface_chart(data, title="Surface Chart"):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    x = range(len(data.index))
    y = range(len(data.columns))
    X, Y = np.meshgrid(y, x)
    
    ax.plot_surface(X, Y, data.values, cmap='viridis')
    ax.set_title(title)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.savefig('surface_chart.png')
    plt.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <csv_file> <chart_type>")
        print("Chart types: bar, surface")
        return
    
    csv_file = sys.argv[1]
    chart_type = sys.argv[2].lower()
    
    try:
        data = pd.read_csv(csv_file)
        
        if chart_type == "bar":
            generate_bar_chart(data)
            print("Bar chart generated as 'bar_chart.png'")
        elif chart_type == "surface":
            generate_surface_chart(data)
            print("Surface chart generated as 'surface_chart.png'")
        else:
            print("Invalid chart type. Please use 'bar' or 'surface'")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()