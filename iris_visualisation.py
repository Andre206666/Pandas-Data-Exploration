import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
print(df.head())
print(df.columns)

sns.heatmap(df[["sepal_length", "sepal_width", "petal_length", "petal_width"]].corr(),
            annot=True, cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.show()

sns.barplot(data=df, x="species", y="petal_length")
plt.show()

sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")
plt.show()

sns.histplot(data=df, x="sepal_length",  hue="species")
plt.show()