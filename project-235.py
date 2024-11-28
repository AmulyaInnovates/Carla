import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Task 01: Collect and print the highest Premier League Goals of each Club
dataset = pd.read_csv("projectC234_EPL.csv")
Football_club = dataset['Club'].value_counts().head(20)
print(Football_club)

data = go.Pie(labels=Football_club.index, values=Football_club.values, hole=0.5)

layout = go.Layout(title='Club with Maximum Penalty Accuracy', showlegend=True)

fig = go.Figure(data=[data], layout=layout)
fig.show()
