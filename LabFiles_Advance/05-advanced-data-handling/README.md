
# Advanced Data Handling

In the financial services industry, managing and analyzing large volumes of transactional data is crucial. Advanced data handling techniques enable efficient data manipulation, storage, and retrieval, which is essential for generating reports, detecting fraud, and making informed business decisions.

## Install necessary libraries

To complete this lab, you need to install the following libraries:

```bash
pip install pandas sqlalchemy
```

## Examples 1: Load a CSV file into a Pandas DataFrame

1. Open file `LabFiles_Advance/05-advanced-data-handling/data_handling.py` 
2. Load a CSV file into a Pandas DataFrame

```python
import pandas as pd

# Load dataset
df = pd.read_csv('transactions.csv')
print(df.head())
```

3. Save file
4. Run the python script

```bash
python data_handling.py
```

5. You should see the first five rows of the dataset printed to the console.

## Example 2: Manipulate data using Pandas

1. Back to the file
2. Manipulate data using Pandas, like the code below:

```python
import pandas as pd

df = pd.read_csv('transactions.csv')
print(df.head())

# Create new dataframe with only the columns 'transaction_id' and 'amount'
df2 = df[['transaction_id', 'amount']]
print(df2.head())
```

3. Save file
4. Run the python script

```bash
python data_handling.py
```
5. You should see the first five rows of the dataset and the new dataframe with only the columns 'transaction_id' and 'amount' printed to the console.


## Example 3: Advanced data manipulation using Pandas

1. Back to the file
2. Perform advanced data manipulation using Pandas, like the code below:

```python
import pandas as pd

df = pd.read_csv('transactions.csv')
# print(df.head())

df2 = df[['transaction_id', 'amount']]
# print(df2.head())

# Filter transactions from January 2023
df_jan2023 = df[(df['date'] >= '2023-01-01') & (df['date'] <= '2023-01-15')]
print(df_jan2023.head())
```

3. Save file, and run the python script

```bash
python data_handling.py
```

4. You should see the first five rows of the filtered dataframe with only transactions before January 15, 2023 printed to the console.
5. Edit the code in the file like the one below: 

```python
import pandas as pd
df = pd.read_csv('transactions.csv')
# print(df.head())

df2 = df[['transaction_id', 'amount']]
# print(df2.head())


df_jan2023 = df[(df['date'] >= '2023-01-01') & (df['date'] <= '2023-01-15')]
# print(df_jan2023.head())

# Group by customer_id and calculate the total amount
total_transactions = df.groupby('customer_id')['amount'].sum().reset_index()
print(total_transactions.head())

# Load customer data
customers = pd.read_csv('customers.csv')

# Merge with transaction data
merged_data = pd.merge(total_transactions, customers, on='customer_id', how='inner')
print(merged_data.head())
```

6. Save file, and run the python script

```bash
python data_handling.py
```

7. You should see the first five rows of the merged dataframe with the total transaction amount per customer and customer data printed to the console.

## Example 4: Store data in a SQLite database

1. Back to the file, ensure the code is like the one below:

```python
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

```

2. At the end of the file, add the code below:

```python
# Create a SQLite database named `financial_data.db` 
engine = create_engine('sqlite:///financial_data.db')

# Creates a base class for declarative ORM models.
Base = declarative_base()

# Defines an ORM model named `CustomerTransaction` with columns `id`, `customer_id`, `amount`, `name`, and `email`.
class CustomerTransaction(Base):
    __tablename__ = 'customer_transactions'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    amount = Column(Float)
    name = Column(String)
    email = Column(String)

# creates the table in the database based on the ORM model.
Base.metadata.create_all(engine)
```

3. Add the end of the file, add the code below:

```python
# Create session, this will allow us to interact with the database.
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into database. This will iterate over the rows in the merged dataframe and insert each row into the database.
for index, row in merged_data.iterrows():
    transaction = CustomerTransaction(
        customer_id=row['customer_id'],
        amount=row['amount'],
        name=row['name'],
        email=row['email']
    )
    session.add(transaction)

# Commit the transaction, this will save the data to the database.
session.commit()
```

4. Add the code below at the end of the file:

```python
# Query data
transactions = session.query(CustomerTransaction).filter_by(customer_id=101).all()
for transaction in transactions:
    print(transaction.name, transaction.amount)
```

5. Save file, and run the python script

```bash
python sqlite.py
```

6. You should see the name and amount of transactions for customer_id 101 printed to the console.

## Complete code

```python
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
```