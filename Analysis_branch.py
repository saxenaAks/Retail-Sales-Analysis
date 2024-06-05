import pandas as pd

# Load sales data into a DataFrame
sales_data = pd.read_csv('sales_data.csv')

# Calculate the average sales amount for the past year
average_sales = sales_data['SalesAmount'].mean()
print(f"The average sales amount for the past year is ${average_sales:.2f}")

# Analyze the impact of customer age on purchasing behavior
# Assuming 'Age' column exists in the sales data
age_groups = sales_data.groupby('Age')
purchase_behavior = age_groups['Purchases'].sum()
print("Customer age groups and their purchasing behavior:")
print(purchase_behavior)

# Identify the top-selling products in each category
top_selling_products = sales_data.groupby('Category')['Product'].value_counts().groupby('Category').head(1)
print("Top-selling products in each category:")
print(top_selling_products)

# Calculate the correlation between advertising spending and sales revenue
correlation = sales_data['AdvertisingSpending'].corr(sales_data['SalesRevenue'])
print(f"Correlation between advertising spending and sales revenue: {correlation:.2f}")

# Analyze sales trends based on seasonality
# Assuming 'Date' column contains date information
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['Month'] = sales_data['Date'].dt.month
monthly_sales = sales_data.groupby('Month')['SalesAmount'].sum()
print("Monthly sales trends:")
print(monthly_sales)

# Calculate the customer retention rate for the past year
# Assuming 'CustomerID' column contains unique customer identifiers
start_customers = sales_data[sales_data['Year'] == 2023]['CustomerID'].nunique()
end_customers = sales_data[sales_data['Year'] == 2024]['CustomerID'].nunique()
retention_rate = (end_customers / start_customers) * 100
print(f"Customer retention rate for the past year: {retention_rate:.2f}%")
