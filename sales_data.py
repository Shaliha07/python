import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales_data.csv')

# Calculate total revenue
df['Total Revenue'] = df['price'] * df['quantity']

# Display the DataFrame
print(df)

# Find the product with the highest revenue
max_revenue = df[df['Total Revenue'] == df['Total Revenue'].max()]
print("Product with the highest revenue:", max_revenue['product'].values[0])

# Plot total revenue for each product
plt.bar(df['product'], df['Total Revenue'])
plt.title("Total Revenue by Product")
plt.xlabel("product")
plt.ylabel("Revenue")
plt.show()

#pie chart
plt.figure(figsize=(8, 6))
plt.pie(df['Total Revenue'], labels=df['product'], autopct='%1.1f%%', startangle=140)
plt.title("Percentage Contribution of Each Product to Total Revenue")
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()

#line chart
plt.figure(figsize=(10, 6))
plt.plot(df['product'], df['price'], marker='o')
plt.title("Product Prices")
plt.xlabel("product")
plt.ylabel("price")
plt.grid()
plt.xticks(rotation=45)  # Rotate x labels for better visibility
plt.show()