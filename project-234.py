import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Task 01: Collect and print the highest Premier League Goals of each Club
dataset = pd.read_csv("projectC234_EPL.csv")
sorted_club_data_by_ascending_order = dataset.groupby('Club')['Goals'].sum()

print("Task 01: Highest Premier League Goals of each Club")
print(sorted_club_data_by_ascending_order)

# Task 02: Collect the Top Goal Scorer in the Premier League and print
epl_top_goals = dataset.sort_values(by='Goals', ascending=False)[:10]
print("\nTask 02: Top Goal Scorer in the Premier League")
print(epl_top_goals)

# Task 03: Show the Top Goal Scorer in the Premier League in a Bar Graph
fig = px.bar(epl_top_goals, x='Name', y='Goals', color='Goals',
             hover_data=['Club', 'Age'], text='Goals',
             title='Top Goal Scorer in the Premier League')
fig.show()
