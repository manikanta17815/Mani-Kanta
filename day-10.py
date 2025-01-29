#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment-1
import pandas as pd

# Load the banking_data.csv file
df = pd.read_csv("banking_data.csv")


filtered_transaction_amount = df[df["Transaction_Amount"] > 2000]
print("Rows where Transaction_Amount is greater than 2000:")
print(filtered_transaction_amount)

loan_payment_high_balance = df[(df["Transaction_Type"] == "Loan Payment") & (df["Account_Balance"] > 5000)]
print("\nRows where Transaction_Type is 'Loan Payment' and Account_Balance is greater than 5000:")
print(loan_payment_high_balance)


uptown_transactions = df[df["Branch"] == "Uptown"]
print("\nTransactions made in the 'Uptown' branch:")
print(uptown_transactions)


# In[ ]:


#Assignment-2
# Add a new column called Transaction_Fee, calculated as 2% of Transaction_Amount
df["Transaction_Fee"] = df["Transaction_Amount"] * 0.02
print("\nDataFrame after adding the 'Transaction_Fee' column:")
print(df.head())

# Create a new column Balance_Status
# If Account_Balance > 5000, label it as "High Balance", otherwise "Low Balance"
df["Balance_Status"] = df["Account_Balance"].apply(lambda x: "High Balance" if x > 5000 else "Low Balance")
print("\nDataFrame after adding the 'Balance_Status' column:")
print(df.head())

