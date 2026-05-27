import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")

print(df.head())
print(df.columns)
print(df.shape)

print("\n===Average price per cut quality===")
print(df.groupby("cut")["price"].mean())

print("\n===Filter diamonds with price > 1000")
print(df[df["price"] > 1000])

print("\n===Sort by carat descending===")
print(df.sort_values(by="carat", ascending=False))

print("\n===New column===")
df["size_category"] = df["carat"].apply(lambda x: "Large" if x > 1.5 else "Small" if x < 0.5 else "Medium")

print("\n===Average price per size_category")
print(df.groupby("size_category")["price"].mean())

print("\n===Which color has the highest avg price===")
print(df.groupby("color")["price"].mean())

df.to_csv("diamonds.csv", index=False)
print("Saved!")
