
import pandas as pd

# Load dataset
df = pd.read_csv('transactions.csv')
print(df.head())

# Create new dataframe with only the columns 'transaction_id' and 'amount'
df2 = df[['transaction_id', 'amount']]
print(df2.head())


# Filter transactions from January 2023
df_jan2023 = df[(df['date'] >= '2023-01-01') & (df['date'] <= '2023-01-15')]
print(df_jan2023.head())

# Group by customer_id and calculate the total amount
total_transactions = df.groupby('customer_id')['amount'].sum().reset_index()
print(total_transactions.head())


# Load customer data
customers = pd.read_csv('customers.csv')

# Merge with transaction data
merged_data = pd.merge(total_transactions, customers, on='customer_id', how='inner')
print(merged_data.head())