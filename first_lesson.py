import pandas as pd

scores = pd.Series([85, 92, 78, 95, 60], index=['Ana','Luis','Carlos','Maria','Pedro'])

print(scores)
print(scores['Ana'])      # access by label → 85
print(scores.mean())      # average → 82.0

students = pd.DataFrame({
    'name':  ['Ana', 'Luis', 'Carlos', 'Maria'],
    'grade': [85, 92, 78, 95],
    'age':   [20, 22, 21, 23]
})

print(students)           # see the full table
print(students.shape)     # (4, 3) → 4 rows, 3 columns
print(students.dtypes)    # data type of each column
print(students.head(2))   # first 2 rows
print(students['grade'])  # select one column → returns a Series
# loc  → select by LABEL (name)
print(students.loc[0])             # row with index label 0
print(students.loc[0, 'name'])     # row 0, column 'name'

# iloc → select by POSITION (number)
print(students.iloc[0])            # first row
print(students.iloc[0, 1])
# first row, second column


import pandas as pd

products = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
    'price': [1200, 25, 75, 400, 90],
    'stock': [15, 200, 150, 30, 80]
})

# Problem 1
print(products.shape)
print(products.dtypes)

# Problem 2
print(products[["product", "price"]])

# Problem 3
print(products.loc[3])
print(products["price"])       # single brackets
print(type(products["price"]))

print(products[["price"]])     # double brackets
print(type(products[["price"]]))
print(products["price"].mean())
print(products[["price"]].mean())
