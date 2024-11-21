# Top 12 German Companies Financial Analysis

## Project Overview

This project provides a comprehensive analysis of financial data for the top 12 German companies. The objective is to extract insights on revenue, profitability, debt levels, and market share. The analysis involves data cleaning, exploratory data analysis (EDA), visualization, and reporting of key findings.

## Table of Contents

- Project Overview
- Directory Structure
- Prerequisites
- Installation
- Usage
    - 1. Data Cleaning
    - 2. Exploratory Data Analysis and Visualization
- Packages Used
- Results
- License
- Acknowledgments


## Directory Structure

- **data/:** Contains data files.
    - **raw/:** Original data files.
    - **processed/:** Cleaned and processed data files.
- **notebooks/:** Jupyter notebooks for EDA and visualization.
- **scripts/:** Python scripts for data cleaning and analysis.
- **reports/:** Generated reports and figures.
    - **figures/:** Visualizations and plots.
- **environment/:** Contains `requirements.txt` for dependencies.
- **.gitignore:** Specifies files and directories to ignore in version control.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

Install 1  Required Packages   
 1. 
pip install -r environment/requirements.txt
Note: Ensure you have an updated version of Node.js installed locally, as it may be required for Jupyter extensions.

Usage
1. Data Cleaning
Run the data cleaning script to process the raw data.

Bash
python scripts/data_cleaning.py

What This Does:
Reads the raw CSV file from data/raw/Top_12_German_Companies.csv.
Cleans and processes the data (handles missing values, converts data types, formats columns).
Saves the cleaned data to data/processed/cleaned_data.csv.
2. Exploratory Data Analysis and Visualization
Launch Jupyter Notebook to explore the data interactively.

Bash
jupyter notebook

Steps:

Open Notebooks:
Navigate to the notebooks/ directory.
Open eda.ipynb for exploratory data analysis.
Open visualization.ipynb for generating visualizations and insights.
Run Cells:
Execute the cells sequentially to perform the analysis.
Modify and experiment with the code as needed.
Alternatively, run the analysis scripts directly from the terminal:

Bash
python scripts/eda.py
python scripts/visualization.py
Note: The scripts will generate outputs and figures in the reports/ directory.

Packages Used:
pandas: Data manipulation and analysis.\n
numpy: Numerical computing.\n
matplotlib: Plotting and visualization.\n
seaborn: Statistical data visualization.\n
jupyter: Interactive notebooks for exploratory analysis.\n
Node.js: Required for some JupyterLab extensions (ensure it's updated).\n

Acknowledgments
Data Source: https://www.kaggle.com/datasets/willianoliveiragibin/top-12-german-companies
