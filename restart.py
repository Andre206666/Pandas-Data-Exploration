import pandas as pd

df = pd.DataFrame({
    "name": ["Ronaldo", "Lewandwski", "Messi", "benzema"],
    "goals": [50, 43, 69, 35],
    "assists": [10, 21, 8, 12]
})
print(df)
print(df.head())
print(df["goals"])
print(df["assists"])
print(df["assists"].max())
print(df["goals"].max())
print(df["goals"].min())
print(df["goals"].mean())
print(df[df["goals"] > 35])
print(df[df["assists"] > 10])
print(df.sort_values(by="goals", ascending=False))
df["total"] = df["goals"] + df["assists"]
print(df)
print(df["total"].mean())

df = pd.DataFrame({
    "title": ["It", "Prince", "King", "Leyend", "God"],
    "rating": [4, 7, 9, 10, 5],
    "year": [2010, 2005, 2006, 2009, 2010],
    "box_office": [1000000000, 2020203003030, 2323232323, 3232323000, 3232323232323]

})
print(df)
print(df[df["rating"] == df["rating"].max()])
print(df[df["year"] > 2010])
print(df.sort_values(by="box_office", ascending=False))
df["ratio"] = df["rating"] / df["box_office"]
print(df["rating"].mean())

