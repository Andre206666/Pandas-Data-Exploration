import pandas as pd

employees = pd.DataFrame({
    'name': ['Sofia', 'Marco', 'Elena', 'Diego', 'Laura'],
    'department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing'],
    'salary': [3000, 5500, 4800, 3200, 4100],
    'years': [2, 5, 3, 7, 1]
})
print(employees.shape)
print(employees.dtypes)
print(employees[["salary", "name"]])
print(employees["salary"])
print(employees.loc[2])

print(employees[employees["salary"] > 3500])
print(employees[employees["department"] == "HR"])
print(employees[(employees["department"] == "Engineering") & (employees["years"] > 2)])