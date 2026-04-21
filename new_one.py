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
import pandas as pd
import numpy as np

attendance_data = {
    'Student': ['Andrew', 'Max', 'Lorena', 'Alice'],
    'Days': [20, np.nan, 18, np.nan]
}
df = pd.DataFrame(attendance_data)
df_cleaned = df.dropna()
df_filled = df.fillna(0)
print("--- Dropped (Only Andrew and Lorena remain) ---")
print(df_cleaned)

print("\n--- Filled (Max and Alice now have 0) ---")
print(df_filled)

import pandas as pd
import numpy as np

store_data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Webcam'],
    'Price': [1200, np.nan, 300, 75, np.nan],
    'In_Stock': [True, True, False, True, False]
}
df = pd.DataFrame(store_data)
df_filled = df.fillna(50)
expensive = df_filled[df_filled['Price'] > 100]
print(expensive)
import pandas as pd
import numpy as np
store_product = {
    "Product": ["Cellphone", "Control", "Tv", "Webcam"],
    "Price": [1200, np.nan, 500, 2000, np.nan],
    "In_stoc": [True, True, False, False, True]
}
df = pd.DataFrame(store_product)
df_filled = df.fillna(500)
expensive = df_filled[df_filled["Price"] > 1000]

