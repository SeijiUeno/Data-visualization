import pandas as pd
import os

def clean_data(input_filepath, output_filepath):
    # Load the dataset
    data = pd.read_csv(input_filepath)

    # Clean the 'percentage  Debt to Equity' column
    data['Debt to Equity %'] = data['percentage  Debt to Equity'] \
        .str.replace(',', '.') \
        .str.replace('%', '') \
        .str.strip() \
        .replace({'': None, 'N/A': None, '-': None, '—': None})

    # Convert to float, setting errors to NaN
    data['Debt to Equity %'] = pd.to_numeric(data['Debt to Equity %'], errors='coerce')

    # Drop the old column
    data.drop(columns=['percentage  Debt to Equity'], inplace=True)

    # Save the cleaned data
    data.to_csv(output_filepath, index=False)
    print(f"Cleaned data saved to {output_filepath}")

if __name__ == "__main__":
    input_filepath = os.path.join('data', 'raw', 'Top_12_German_Companies.csv')
    output_filepath = os.path.join('data', 'processed', 'cleaned_data.csv')
    clean_data(input_filepath, output_filepath)
