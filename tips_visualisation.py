import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

print(df.head())

plt.figure(figsize=(8, 5))
plt.scatter(df["total_bill"], df["tip"])
plt.title("Bill vs Tip")
plt.xlabel("Total Bill($)")
plt.ylabel("Tip($)")
plt.show()

plt.figure(figsize=(8, 5))
df.groupby("day")["tip"].mean().plot(kind="bar")
plt.title("Average Tip per Day")
plt.xlabel("Day of the Week")
plt.ylabel("Average Tip ($)")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["total_bill"], bins=20, edgecolor='black')
plt.title("Distribution of Total Bill Amounts")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.show()