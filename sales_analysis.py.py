
 # Data analysis
import pandas as pd

# Database connection
from sqlalchemy import create_engine


# Visualization
import matplotlib.pyplot as plt


# Numerical operations
import numpy as np  

pd.set_option('display.max_columns', None);

# Load sales data
df = pd.read_csv("notebook/sample_superstore.csv", encoding='latin1')

# Preview data
df.head()
print(df.head());

# Load data columns and reolace(' ', '_') and lower case

df.columns
print(df.columns);
df.columns = df.columns.str.lower().str.replace(' ', '_')
print(df.columns);


# Check for missing values
df.isnull().sum()
print(df.isnull().sum());

# Convert date columns to datetime

df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date']) 
print(df.dtypes); 

# Summary statistics
df[['sales', 'profit']].describe()
print(df[['sales', 'profit']].describe());

# Total sales and profit
total_sales = df['sales'].sum()
total_profit = df['profit'].sum()
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}");

# Total orders
total_orders = df['order_id'].nunique()
print(f"Total Orders: {total_orders}");

# Sales by category
sales_by_category = df.groupby('category')['sales'].sum().sort_values(ascending=False)
print(sales_by_category);

# Top 10 products by sales
top_10_products = df.groupby('sub-category')['sales'].sum().sort_values(ascending=False).head(10)
print(top_10_products);

# Sales over time
sales_over_time = df.groupby('order_date')['sales'].sum()
print(sales_over_time);

# Visualizations
plt.figure()
plt.hist(df['sales'], bins=30)
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show();

# Sales by category bar chart
plt.figure()
sales_by_category.plot(kind='bar')
plt.title('Total Sales By Category')
plt.xlabel('Category')
plt.ylabel('Total; Sales')
plt.show();

# Top 10 products by sales horizontal bar chart
plt.figure()
top_10_products.plot(kind='barh')
plt.title('Top 10 Products By Sales')
plt.xlabel('sub-category')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.show();

# Sales over time line chart
plt.figure()
sales_over_time.plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('sales')
plt.show();

# Save cleaned data
df.to_csv("notebook/cleaned_sales_data.csv", index=False)

# End of analysis
# game over print("Sales analysis completed and cleaned data saved.");


from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres"      # default user
password = "142003" # the password you set during installation
host = "localhost"         # if running locally
port = "5432"              # default PostgreSQL port
database = "sample_superstore"    # the database you created in pgAdmin

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Step 2: Load DataFrame into PostgreSQL
table_name = "sales_data"   # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")