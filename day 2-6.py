import pandas as pd

# Sample DataFrame
data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Quantity': [10, 20, 30, 15, 25, 35, 5, 10, 20, 10, 15, 25]
}

sales_data = pd.DataFrame(data)

# Group by product and sum up quantities sold
product_sales = sales_data.groupby('Product')['Quantity'].sum()

# Sort the products based on total quantity sold
top_products = product_sales.sort_values(ascending=False)

# Select the top 5 products
top_5_products = top_products.head(5)

print(top_5_products)
