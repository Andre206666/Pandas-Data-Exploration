import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv")

print(df.shape)

print("\n===Average passengers per year===")
print(df.groupby("year")["passengers"].mean())

print("\n===Month with the highest average person overall")
print(df.groupby("month")["passengers"].mean().idxmax())

print("\n===Filter flights with passengers > 400")
print(df[df["passengers"] > 400])

print("\n===New column===")
df["busy"] = df["passengers"].apply(lambda x: True if x > 300 else False)

print("\n===Highest total passengers per year===")
print(df.groupby("year")["passengers"].count().idxmax())

df.to_csv("flights_analysis.csv", index=False)
print("Saved!")

print("\n===2 filters===")
result = df[(df["passengers"] > 300) & (df["year"] > 1955)]
print(result)

print("\n===2 combine")
result = df[(df["month"] == "December") | (df["passengers"] > 500)]
print(result)

print("\n===filer betwenn===")
result = df[df["year"].between(1950, 1955)]
print(result)

print("\n===New pivot table===")
pivot = df.pivot_table(values="passengers", index="year", columns="month", aggfunc="mean")
print(pivot)

print("\n===Filer corr===")
print(df[["passengers", "year"]].corr())

print("\n===Average passengers per month===")
print(df.groupby("month")["passengers"].mean())

print("\n===Filter only if year his higher than 1960")
print(df[df["year"] > 1960])

print("\n===Create a new pivot table===")
pivot2 = df.pivot_table(values="passengers", index="year", columns="month", aggfunc="sum")
print(pivot2)

print("\n===Correlation===")
print(df[["passengers", "year"]].corr())

print("\n===New column===")
df["era"] = df["year"].apply(lambda x: "Old" if x < 1955 else "New")
print(df)

print("\n===Average passengers per era===")
print(df.groupby("era")["passengers"].mean())

df.to_csv("flights_final.csv", index=False)
print("Saved")

