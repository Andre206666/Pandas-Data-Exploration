import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

print(df.head())
print(df.columns)

print("\n===Average tip by sex===")
print(df.groupby("sex")["tip"].mean())

print("\n===Average tip by day===")
print(df.groupby("day")["tip"].mean())

print("\n=== Do smokers tip more? ===")
print(df.groupby("smoker")["tip"].mean())

print("\n===Filter tables with tip > 5===")
print(df[df["tip"] > 5])

print("\n===New column===")
df["tip_percent"] = df["tip"] / df["total_bill"] * 100
print(df)

print("\n=== Averag tip_percent per time")
print(df.groupby("time")["tip_percent"].mean())

df.to_csv("tips_analysis.csv", index=False)
print("Saved!")