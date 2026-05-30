import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())


plt.scatter(df["total_bill"], df["tip"])
plt.title("Tip vs Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()


df.groupby("day")["tip"].mean().plot(kind="bar")

plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.show()


df.groupby("smoker")["tip"].mean().plot(kind="bar")

plt.title("Average Tip by Smoker Status")
plt.xlabel("Smoker")
plt.ylabel("Average Tip")
plt.show()

df.groupby(["smoker", "day"])["tip"].mean().unstack().plot(kind="bar")

plt.title("Average Tip by Smoker and Day")
plt.xlabel("smoker / Day")
plt.ylabel("Average Tip")

plt.show()