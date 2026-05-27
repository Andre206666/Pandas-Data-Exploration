import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")

print(df.head())
print(df.columns)

print("\n===boddy_mass_g per sex===")
print(df.groupby("sex")["body_mass_g"].mean())

print("Penguins who have body_mass higher than 3800")
print(df[df["body_mass_g"] > 3800])

print("\n===Calculate the average beak length of the penguins===")
print(df.groupby("species")["bill_length_mm"].mean())

print("\n===Show only bill_length_mm > 45===")
print(df[df["bill_length_mm"] > 45])

print("\n===Sorted by flipper size===")
print(df.sort_values(by="flipper_length_mm", ascending=False))