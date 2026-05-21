import pandas as pd

countries = pd.DataFrame({
    "country": ["Mexico", "Brasil", "Germany", "Italy", "France", "England"],
    "continent": ["Latin america", "South america", "Europe", "Europe", "Europe", "Europe"],
    "pupulation": [100000000, 20000000, 5000000, 40000000, 65000000, 8000000000],
    "gdp": [900000000000000, 100000000000, 200000000000, 300000000000, 9999999999999, 900000000],
    "life_expectancy": [74, 70, 82, 83, 84, 73]
})

print("\n===Countries with life_expectancy ===")
print(countries[countries["life_expectancy"] > 75])

print("\n===Average GDP per continent ===")
print(countries.groupby("continent")["gdp"].mean())

print("\n===Sprt by population descending===")
print(countries.sort_values(by="pupulation", ascending=False))

print("\n===New column ===")
countries["Developed"] = countries["gdp"].apply(lambda x: "Developed" if x > 3000000 else "Developing" if x < 100000 else "Underdeloped")
print(countries)

print("\n===Save countries.csv")
countries.to_csv("countries.csv", index=False)
print("Saved!")