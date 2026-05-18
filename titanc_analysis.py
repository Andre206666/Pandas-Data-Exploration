import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("=== Basic Stats ===")
print(f"Total survivors: {df['Survived'].sum()}")
print(f"Average age: {df['Age'].mean():.1f}")

print("\n=== Fare by Class ===")
print(df.groupby("Pclass")["Fare"].mean())

print("\n=== Passengers by Sex ===")
print(df.groupby("Sex")["PassengerId"].count())

print("\n=== Survival by Sex ===")
print(df.groupby("Sex")["Survived"].mean())

print("\n=== Average Age by Class ===")
print(df.groupby("Pclass")["Age"].mean())

print("\n=== Survival by Class ===")
print(df.groupby("Pclass")["Survived"].mean())

print("\n=== Oldest Passenger ===")
print(df[df["Age"] == df["Age"].max()][["Name", "Age", "Survived"]])

print("\n=== Survival by Sex + Class ===")
print(df.groupby(["Sex", "Pclass"])["Survived"].mean())

print("\n=== Survival by Age Group ===")
df["AgeGroup"] = df["Age"].apply(lambda x: "Child" if x < 18 else "Adult")
print(df.groupby("AgeGroup")["Survived"].mean())