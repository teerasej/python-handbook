from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Load dataset
df = pd.read_csv('transactions.csv')
# print(df.head())

# Create new dataframe with only the columns 'transaction_id' and 'amount'
df2 = df[['transaction_id', 'amount']]
#print(df2.head())


# Filter transactions from January 2023
df_jan2023 = df[(df['date'] >= '2023-01-01') & (df['date'] <= '2023-01-15')]
#print(df_jan2023.head())

# Group by customer_id and calculate the total amount
total_transactions = df.groupby('customer_id')['amount'].sum().reset_index()
#print(total_transactions.head())


# Load customer data
customers = pd.read_csv('customers.csv')

# Merge with transaction data
merged_data = pd.merge(total_transactions, customers, on='customer_id', how='inner')
print(merged_data.head())

# Create SQLite database
engine = create_engine('sqlite:///financial_data.db')
Base = declarative_base()

# Define ORM model
class CustomerTransaction(Base):
    __tablename__ = 'customer_transactions'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    amount = Column(Float)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into database
for index, row in merged_data.iterrows():
    transaction = CustomerTransaction(
        customer_id=row['customer_id'],
        amount=row['amount'],
        name=row['name'],
        email=row['email']
    )
    session.add(transaction)

session.commit()

# Query data
transactions = session.query(CustomerTransaction).filter_by(customer_id=101).all()
for transaction in transactions:
    print(transaction.name, transaction.amount)