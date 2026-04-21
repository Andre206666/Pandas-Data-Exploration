import pandas as pd
import numpy as np

school_data = {
    'Student': ['Andrew', 'Max', 'Lorena', 'Alice', 'John'],
    'Score': [95, np.nan, 88, 70, np.nan],
    'Attendance': [90, 80, 95, 60, 85]
}
df = pd.DataFrame(school_data)
df = df.fillna(60)
df = df[df['Attendance'] > 80]
df = df.sort_values(by='Score', ascending=False)

print(df)
import pandas as pd
import numpy as np
data = {"Score" : [10, np.nan, 30], "Name": ["A", "B", "C"]}
df = pd.DataFrame(data)
df = df.fillna(0)
df = df[df["Score"] > 5]
df = df.sort_values(by="Score", ascending=False)
print(df)
import pandas as pd
import numpy as np

store_data = {
    'Customer': ['Andrew', 'John', 'Lorena', 'Alice', 'Bob'],
    'Total_Spent': [150, np.nan, 300, 50, np.nan],
    'Member': [True, False, True, True, False]
}
df = pd.DataFrame(store_data)
df = df.fillna(0)
df = df[df["Member"] == True]
df = df.sort_values(by="Total_Spent", ascending=False)
print(df)
import pandas as pd

grades_data = {
    'Subject': ['Calculus', 'Calculus', 'Statistics', 'Statistics', 'Python'],
    'Type': ['Exam', 'Homework', 'Exam', 'Homework', 'Exam'],
    'Score': [80, 100, 90, 85, 95]
}
df = pd.DataFrame(grades_data)

subject_averages = df.groupby('Subject')['Score'].mean()

print("--- Average Grade per Subject ---")
print(subject_averages)
