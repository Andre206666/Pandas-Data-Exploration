import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.barplot(data=df, x="day", y="tip")
plt.title("Average Tip per Day")
plt.show()

sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Total tip per day")
plt.show()

sns.histplot(data=df, x="total_bill", bins=20)
plt.title("Total tip every day")
plt.show()

sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
plt.title("Bill vs Tip by Sex")
plt.show()

sns.scatterplot(data=df, x="total_bill", y="tip", hue="smoker")
plt.title("Bill vs Tip by smoker")
plt.show()

sns.scatterplot(data=df, x="total_bill", y="tip", hue="day")
plt.title("Bill vs Tip by Day")
plt.show()

sns.scatterplot(data=df, x="day", y="tip", hue="sex")
plt.title("Tips per every day")
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df[["total_bill", "tip", "size"]].corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

df = sns.load_dataset("penguins")

plt.figure(figsize=(8, 6))
sns.heatmap(df[["bill_length_mm", "flipper_length_mm", "body_mass_g"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Penguin Correlations")
plt.show()

plt.scatter(df["bill_length_mm"], df["flipper_length_mm"])
plt.title("Flipper length vs body mass")
plt.show()

sns.barplot(data=df, x="bill_length_mm", y="flipper_length_mm")
plt.title("Flipper length vs body mass")
plt.show()

sns.scatterplot(data=df, x="bill_length_mm", y="flipper_length_mm", hue="species")
plt.title("Flipper length vs body mass")
plt.show()

sns.barplot(data=df, x="species", y="body_mass_g", hue="sex")
plt.title("Average Body Mass by Species and Sex")
plt.show()

df = sns.load_dataset("diamonds")
plt.figure(figsize=(8, 6))
sns.heatmap(df[["carat", "depth", "price"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

plt.scatter(df["carat"], df["price"])
plt.title("Carat vs Price")
plt.show()

sns.barplot(data=df, x="price", y="cut", hue="color")
plt.title("Cut vs price")
plt.show()


df = sns.load_dataset("diamonds")

plt.figure(figsize=(8, 6))
sns.heatmap(df[["carat", "depth", "price"]].corr(), annot=True, cmap="coolwarm")
plt.title("Diamond Correlations")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="carat", y="price", hue="cut", alpha=0.5)
plt.title("Carat vs Price by Cut")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="cut", y="price")
plt.title("Average Price per Cut")
plt.show()