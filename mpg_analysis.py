import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")

print(df.head())
print(df.columns)
print(df.shape)

print("\n===Cars who acelerations is biggest than 40===")
print(df[df["acceleration"]> 40])

print("\n===horse power average per weight===")
print(df.groupby("cylinders")["horsepower"].mean())

print("\n===full efiency per gallon per model===")
print(df.groupby("name")["mpg"].mean())

print("\n===Which year has the most efficient cars===")
print(df.groupby("model_year")["mpg"].max())

print("\n===Which origin make the most efficient cars===")
print(df.groupby("origin")["mpg"].max())

print("\n===Does weight affect mpg?===")
print(df[["mpg", "weight", "horsepower", "cylinders"]].corr())

print("\n===Pivot table average mpg by origin and cylinders===")
print(df.pivot_table(values="mpg", index="origin", columns="cylinders", aggfunc="mean"))

print("\n===Multiple filters efficient american cars===")
print(df[(df["origin"] == "usa") & (df["mpg"] > 30)])