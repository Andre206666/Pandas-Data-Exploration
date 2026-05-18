import pandas as pd
employees = pd.DataFrame({
    "name": ["Diego", "Carlo", "Paulo", "Maria", "Valentina", "Roberto"],
    "department": ["Economics", "Sales", "Marketing", "Technology", "Resources humans", "Lab"],
    "salary": [1000000, 2000000, 1500000, 3000000, 4000000, 2000000],
    "years": [4, 6, 8, 12, 9, 11]

})
employees['bonus'] = employees['salary'] * 0.10
employees['level'] = employees['years'].apply(lambda x: "Senior" if x > 8 else "Junior")


employees.groupby('department')['salary'].mean()
print(employees.groupby("department")["salary"].mean())
print(employees.shape)
print(employees.describe())
employees.groupby("department")["years"].mean()
print(employees.groupby("department")["years"].mean())
employees.groupby("salary")["department"].sum()
print(employees.groupby("salary")["department"].sum())
print(employees[employees["salary"] > 2000000])
employees.groupby("department")["bonus"].sum()
seniors = employees[employees["level"] == "Senior"]
print(seniors[seniors['salary'] == seniors['salary'].max()])
print(employees.groupby("name")["salary"])
employees['bonus'] = employees['salary'] * 0.10
print(employees.groupby("department")["bonus"].sum())
employees.sort_values("salary", ascending=False)
print(employees.sort_values("salary", ascending=False))
print(employees[employees['years'] > 3])
print(employees)
employees['level'] = employees['years'].apply(lambda x: "Senior" if x > 8 else "Junior")
print(employees)
print(employees)

students = pd.DataFrame({
    "name": ["Andre", "Ernesto", "Perry", "Diego", "Sebas"],
    "grade": [9, 8, 7, 10, 9],
    "age": [18, 17, 19, 21, 18],
    "city": ["London", "La", "Hongkong", "Bejing", "New York"]
})
students.to_csv("students.csv")
df = pd.read_csv("students.csv")
print(df)
students.loc[0, 'grade'] = None
students.loc[2, 'age'] = None
print(students.isnull())
students = students.fillna(0)
print(students)
print(students)

sales = pd.DataFrame({
    "product": ["Cellphone", "Tv", "Watch"],
    "price": [200, 500, 200],
    "quantity": [12, 5, 20],
    "category": ["Luxury", "Poor", "Luxury" ]
})
sales.to_csv("sales.csv", index=False)
sales["revenue"] = sales["price"] * sales["quantity"]
print(df)
print(sales.groupby("category")["revenue"].sum())
print(sales[sales["price"] == sales["price"].max()])
print(sales[sales["quantity"] > 50])
print(sales.sort_values("revenue", ascending=False))
sales.to_csv("sales_final.csv", index=False)
print("Saved!")





