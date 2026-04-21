import numpy as np

prices = np.array([150, 50, 200, 300])
is_premium = np.array([True, True, False, True])
names = np.array(["Andrew", "John", "Alice", "Bob"])

mask = (is_premium == True) & (prices > 100)

result = names[mask]
print(f"NumPy Result: {result}")
import pandas as pd
data = {
    "customer_name": ["Andrew", "ALice", "John", "Bob"],
    "total_price": [150, 50, 200, 40],
    "is_premium": [True, True, False, True]
}
df = pd.DataFrame(data)
print(df)

express_orders = df[(df["is_premium"] == True) & (df["total_price"] > 100)]
print("Express shiping_list")
print(express_orders)
cheap_orders = df[df['total_price'] < 100]

average_price = df['total_price'].mean()
print("--- Orders under 100 ---")
print(cheap_orders)

print(f"\nAverage Price of all orders: ${average_price}")
import pandas as pd

data = {
    'player': ['Mbappé', 'Vinícius', 'Rodrygo', 'Bellingham', 'Joselu'],
    'goals': [24, 15, 10, 19, 9],
    'position': ['Forward', 'Forward', 'Forward', 'Midfield', 'Forward']
}
soccer_df = pd.DataFrame(data)
print(soccer_df)
high_scorers = df[df["goals"] > 15]
total_team_goals = soccer_df["goals"].sum()
print("--- High Scorers (> 15 goals) ---")
print(high_scorers)

print(f"\nTotal goals scored by the team: {total_team_goals}")
import pandas as pd

grades_data = {
    'Subject': ['Calculus', 'Statistics', 'Python', 'SQL', 'Linear Algebra'],
    'Score': [85, 92, 98, 90, 88]
}
grades_df = pd.DataFrame(grades_data)
sorted_grades = grades_df.sort_values("Score", ascending=False)
top_subjects = grades_df[grades_df["Score"] >= 90]
grades_df["Status"] = "Pass"
print(sorted_grades)
print(top_subjects)
print(grades_df)


