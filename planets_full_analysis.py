import pandas as ps
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("planets")
print(df.isnull().sum())

print("\nAverage orbital_period per method ")
print(df.groupby("method")["orbital_period"].mean())

print("\nFilter planets discovered after 2010")
print(df[df["year"] > 2010])

print("\nNew column")
df["era"] = df["year"].apply(lambda x: "Modern" if x > 2005 else "Classic")

print("Total planets discovered per method")
print(df.groupby("method")["number"].sum())

sns.heatmap(df[["number", "mass", "orbital_period"]].corr(),
            annot=True, cmap="YlGnBu")
plt.title("Orbital period per method")
plt.show()

sns.barplot(data=df, x="method", y="number")
plt.title("Average number of planets discovered per method")
plt.show()

sns.scatterplot(data=df, x="number", y="orbital_period", hue="method")
plt.show()

sns.histplot(data=df, x="year", hue="method")
plt.title("Distribution of year")
plt.show()

