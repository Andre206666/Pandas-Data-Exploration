import pandas as pd

players = pd.DataFrame ({
    "name": ["Ronaldo", "Messi", "lewandowski", "Raul", "Vega", "Vinicious"],
    "Team": ["Real madrid", "Barcelona", "Wolves", "Toluca", "Madrid", "Azul"],
    "Goals": [30, 35, 49, 17, 12, 21],
    "Assists": [12, 21, 12, 5, 7, 9],
    "minutes_played": [2000, 4000, 2500, 3000, 4000, 1500]

})

print("===\nPlayers with more than 5 goals===")
print(players[players["Goals"] > 5])

print("===\nAverage gol per team===")
print(players.groupby("Team")["Goals"].mean())

print("\n===Sort by assists descending===")
print(players.sort_values("Assists", ascending=False))

print("\n===New column===")
players["Rating"] = players["Goals"].apply(lambda x: "Elite" if x > 10 else "Good" if x >= 5 else "Average")
print(players)

print("===Total goals per team===")
print(players.groupby("Team")["Goals"].sum())

print("\n===save to sport.csv")
players.to_csv("sport_analyisis.csv", index=False)
print("Saved!")

movies = pd.DataFrame ({
    "tile": ["Star wars", "It", "Batman", "Superman", "Avengers"],
    "genre": ["History", "Terro", "Action", "Villians", "Superheroes"],
    "rating": [18, 21, 14, 16, 16]
})

print("===\nMovies rating > 7")
print(movies[movies["rating"] > 7])

movies["status"] = movies["rating"].apply(lambda x: "Hit" if x > 8 else "Flop" if x <= 6 else "Average")
print(movies)