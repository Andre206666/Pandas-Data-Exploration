import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/nickhould/craft-beers-dataset/master/data/processed/beers.csv")

print(df.head())
print(df.shape)
print(df.columns)

print("\n===Missing values===")
print(df.isnull().sum())

print("\n===Average alcohol content per style===")
print(df.groupby("style")["abv"].mean())

print("\n===Filters beer with abv > 0.08")
print(df[df["abv"] > 0.08])

print("\n===Sort by ascending abv===")
print(df.sort_values(by="abv", ascending=False))

print("\n===New column===")
df["strengt"] = df["abv"].apply(lambda x: "Strong" if x > 0.08 else "Light" if x < 0.05 else "Medium")

print("\n===Beers per strength category===")
print(df.groupby("strengt")["name"].count())

print("\n===Save file as beersanalysis.csv===")
df.to_csv("beersanalysis.csv", index=False)
print("Saved!")


