import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv")

print(df.head())
print(df.columns)
print(df.shape)

print("===\nTotal births per year===")
print(df.groupby("year")["births"].sum())

print("===\nTotal births per month===")
print(df.groupby("month")["births"].mean())

print("===\nWhich gender has more birthdays overall")
print(df.groupby("gender")["births"].sum())

print("===\nSort by births descending top 10===")
print(df.sort_values(by="births", ascending=False))

print("===\nAdd a new column")
df["era"] = df["year"].apply(lambda x: "Modern" if x > 1990 else "Classic")
print(df)

print("===\nTotal births per era===")
print(df.groupby("era")["births"].sum())

df.to_csv("World_cup.csv", index=False)
print("Saved!")

