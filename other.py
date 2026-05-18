import pandas as pd

orders = pd.DataFrame({
    'customer': ['Alice', 'Bob', 'Alice', 'Carlos', 'Bob', 'Carlos'],
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor', 'Mouse'],
    'quantity': [1, 3, 2, 1, 2, 4],
    'price': [1200, 25, 75, 1200, 400, 25]
})

# Problem 1
print(orders.shape)
print(orders.dtypes)

# Problem 2
orders["total"] = orders["quantity"] * orders["price"]
print(orders)

# Problem 3
print(orders[orders["total"] > 200])

# Problem 4
print(orders[(orders["customer"] == "Alice") | (orders["product"] == "Mouse")])
