import pandas as pd
employees = pd.DataFrame({
    "name": ["Andre", "Paulo", "Carlo", "Diego", "Ricrado", "Diego"],
    "subject": ["Maths", "Physics", "History", "Linearalgebra", "Calculus", "Languages"],
    "grade": [9, 8.5, 7, 8, 6.5, 10],
    "city": ["Singapur", "Newyork", "Spain", "Netherland", "hongkong", "Shangai"]

})
print(employees[employees["grade"] >= 7])
print(employees.groupby("subject")["grade"].mean())
print(employees.sort_values("grade", ascending=False))
print(employees.to_csv("students_final.txt", index=False))
employees["passed"] = employees["grade"].apply(lambda x: "Yes" if x > 6 else "No")


movies = pd.DataFrame({
    "tile": ["star wars", "Batman", "It", "Avengers", "Dragon ball", "Duna"],
    "genre": ["Fiction", "Action", "terror", "Adventure", "Anime", "History"],
    "year": [1989, 2023, 1986, 2015, 2017, 2024],
    "box_office": [100000000, 200000000, 200000000, 2000000000000, 3000000000000, 232321321321321],
    "rating": [9, 8, 7, 6, 8, 9]
})
print(movies[movies["rating"] > 7])
print(movies.groupby("genre")["rating"].mean())
print(movies.sort_values("rating", ascending=False))
print(movies[movies["rating"] == movies["rating"].max()])
movies["blockbuster"] = movies["box_office"].apply(lambda x: "Yes" if x > 500000000 else "No")
movies.to_csv("movies.csv", index=False)
print("Saved!")



