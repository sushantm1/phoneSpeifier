import pandas as pd
import numpy as np

# Load and clean data
data = pd.read_csv('smartphones.csv')
data = data.dropna().drop_duplicates().reset_index(drop=True)

# Standardize brand names to lowercase
data['brand_name'] = data['brand_name'].str.lower()

# Get unique brand names
brand_names = data['brand_name'].drop_duplicates().reset_index(drop=True)
print("Available brands:\n", brand_names)

# Input first brand from user
first_company_name = input("Enter the first company name: ").lower()

# Filter models by brand
if first_company_name in brand_names.values:
    model_data = data[data['brand_name'] == first_company_name].reset_index(drop=True)
    print("Available models from", first_company_name, ":\n", model_data['model'])
else:
    print("Brand not found. Please check your input.")

