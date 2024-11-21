import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')  # Ensure a GUI backend is used
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Top_12_German_Companies.csv'  # Adjust to the actual file location
data = pd.read_csv(file_path)

# Cleaning the 'percentage  Debt to Equity' column
data['Debt to Equity %'] = data['percentage  Debt to Equity'].str.replace(',', '.').str.replace('%', '').astype(float)

# Drop the old column for clarity
data.drop(columns=['percentage  Debt to Equity'], inplace=True)

# Aggregate numeric data by Company
aggregated_data = data.groupby('Company', as_index=False).mean(numeric_only=True)

# Print backend to confirm GUI is working
print("Using backend:", matplotlib.get_backend())

# Plot: Total Revenue vs. Net Income for each company
plt.figure(figsize=(12, 6))
plt.bar(aggregated_data['Company'], aggregated_data['Revenue'] / 1e6, label='Revenue (in millions)', alpha=0.7)
plt.bar(aggregated_data['Company'], aggregated_data['Net Income'] / 1e6, label='Net Income (in millions)', alpha=0.7)

# Adding labels and title
plt.title("Revenue vs. Net Income of German Companies", fontsize=16)
plt.xlabel("Company", fontsize=14)
plt.ylabel("Amount (in millions EUR)", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.legend(fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()
