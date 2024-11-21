import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def plot_revenue_vs_income(data, output_dir):
    """Generate and save a bar plot of revenue vs. net income."""
    aggregated_data = data.groupby('Company', as_index=False).mean(numeric_only=True)
    
    plt.figure(figsize=(12, 6))
    plt.bar(aggregated_data['Company'], aggregated_data['Revenue'] / 1e6, label='Revenue (in millions)', alpha=0.7)
    plt.bar(aggregated_data['Company'], aggregated_data['Net Income'] / 1e6, label='Net Income (in millions)', alpha=0.7)
    
    plt.title("Revenue vs. Net Income of German Companies", fontsize=16)
    plt.xlabel("Company", fontsize=14)
    plt.ylabel("Amount (in millions EUR)", fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    output_path = os.path.join(output_dir, 'revenue_vs_income.png')
    plt.savefig(output_path)
    print(f"Figure saved to {output_path}")
    plt.close()

def plot_correlation_matrix(data, output_dir):
    """Generate and save a heatmap for the correlation matrix."""
    # Calculate correlation matrix
    correlation_matrix = data.corr(numeric_only=True)

    # Create the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    
    plt.title("Correlation Matrix", fontsize=16)
    plt.tight_layout()
    
    # Save the heatmap
    output_path = os.path.join(output_dir, 'correlation_matrix.png')
    plt.savefig(output_path)
    print(f"Correlation matrix heatmap saved to {output_path}")
    plt.close()

def main():
    # Define file paths
    data_dir = os.path.join(os.getcwd(), 'data', 'processed')
    figure_dir = os.path.join(os.getcwd(), 'reports', 'figures')
    os.makedirs(figure_dir, exist_ok=True)
    
    filepath = os.path.join(data_dir, 'cleaned_data.csv')
    
    # Load data
    data = load_data(filepath)
    if data is None:
        return
    
    # Generate visualizations
    plot_revenue_vs_income(data, figure_dir)
    plot_correlation_matrix(data, figure_dir)

if __name__ == "__main__":
    main()
