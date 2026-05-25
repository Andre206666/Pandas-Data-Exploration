import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print("\n===Survived by Pclass===")
print(df.groupby("Pclass")["Survived"].mean())

print("\n===Sort values by Pclass===")
print(df.sort_values(by="Pclass", ascending=False))

print("\n===Average age by Sex===")
print(df.groupby("Sex")["Age"].mean())

print("\n===New column===")
df["Rich guys"] = df["Pclass"].apply(lambda x: "Rich" if x == 1 else "Poor")

print("\n===Survival by port===")
print(df.groupby("Embarked")["Survived"].mean())

print("\n===Rich guys===")
print(df["Rich guys"].value_counts())