import pandas as pd

df_passengers = pd.DataFrame({
    "year": [1949, 1950, 1951, 1952],
    "total_passengers": [1520, 1676, 2042, 2364]
})

df_info = pd.DataFrame({
    "year": [1949, 1950, 1951, 1953],
    "event": ["Post-war boom", "Korean War", "Jet age begins", "New routes added"]
})

df_merged = pd.merge(df_passengers, df_info, on="year")
print(df_merged)


df_outer = pd.merge(df_passengers, df_info, on="year", how="outer")
print(df_outer)

df_left = pd.merge(df_passengers, df_info, on="year", how="left")
print(df_left)

df_right = pd.merge(df_passengers, df_info, on="year", how="right")
print(df_right)