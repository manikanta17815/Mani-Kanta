#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load the banking_data.csv file
df = pd.read_csv("banking_data.csv")

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Generate basic statistics of the numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Check for missing values in the dataset
print("\nChecking for missing values:")
print(df.isnull().sum())

