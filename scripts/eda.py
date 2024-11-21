import pandas as pd
import os

def load_data(filepath):
    """Load the dataset from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def summarize_data(data):
    """Print summary statistics and check for missing values."""
    print("\n### Dataset Overview ###")
    print(data.head(), "\n")
    
    print("\n### Dataset Info ###")
    print(data.info(), "\n")
    
    print("\n### Missing Values ###")
    print(data.isnull().sum(), "\n")
    
    print("\n### Statistical Summary ###")
    print(data.describe(include='all'), "\n")

def main():
    # Define file paths
    data_dir = os.path.join(os.getcwd(), 'data', 'processed')
    filepath = os.path.join(data_dir, 'cleaned_data.csv')
    
    # Load data
    data = load_data(filepath)
    if data is None:
        return
    
    # Summarize data
    summarize_data(data)

if __name__ == "__main__":
    main()
