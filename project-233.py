import pandas as pd

# Read CSV using Pandas library
df = pd.read_csv('projectC233_studentData.csv')

# Task 01: Get Total marks obtained by using the SUM function of Pandas
df['Total_marks_obtained'] = df.iloc[:, [2, 3, 4]].sum(axis=1)

# Task 02: Apply conditions to get the Grades
df.loc[df['Total_marks_obtained'] > 250, 'Grade'] = 'A'
df.loc[df['Total_marks_obtained'] <= 250, 'Grade'] = 'B'

# Task 03: Calculate the overall percentage obtained
df['Percentage'] = (df['Total_marks_obtained'] / df['Overall_Total']) * 100

# Display the dataframe
print(df)

