import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [1000, 50, 75, 300],
    "Quantity": [4, 10, 6, 2]
}

df = pd.DataFrame(data)

# Viewing the first few rows
print(df.head())

# Accessing a column
print(df["Product"])

# Adding a new column
df["Total Revenue"] = df["Price"] * df["Quantity"]
print(df)

# Filtering data
filtered_df = df[df["Price"] > 100]
print(filtered_df)

# Data
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
revenues = [4000, 500, 450, 600]

# Create a bar chart
plt.bar(products, revenues)
plt.title("Product Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
