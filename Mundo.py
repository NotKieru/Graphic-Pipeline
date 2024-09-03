import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

def plot_image(points, mundo=[[0],[0],[0],[1]]):
    dfs = []
    figs = []

    for point_set in points:
        if len(point_set) != 3:
            raise ValueError("Cada item em 'points' deve ser uma lista de três listas (x, y, z).")
        df = pd.DataFrame({"x": point_set[0], "y": point_set[1], "z": point_set[2]})
        dfs.append(df)

    for df in dfs:
        color = np.random.randint(255, size=3)
        fig = px.line_3d(df, x="x", y="y", z="z", color_discrete_sequence=[f'rgb({color[0]}, {color[1]}, {color[2]})'])
        figs.append(fig.data[0])

    fig = go.Figure(data=figs)

    lines = [
        {'x': [0, 0], 'y': [0, 0], 'z': [-20, 20]},
        {'x': [0, 0], 'y': [-20, 20], 'z': [0, 0]},
        {'x': [-20, 20], 'y': [0, 0], 'z': [0, 0]}
    ]

    for line in lines:
        fig.add_scatter3d(mode='lines', x=line['x'], y=line['y'], z=line['z'], line=dict(color='black'))

    new_point = {'x': mundo[0], 'y': mundo[1], 'z': mundo[2]}
    df_mundo = pd.DataFrame(new_point)
    fig.add_trace(px.scatter_3d(df_mundo, x='x', y='y', z='z', size=[0.5]).data[0])

    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[-20, 20]),
            yaxis=dict(range=[-20, 20]),
            zaxis=dict(range=[-20, 20]),
            aspectmode="cube",
        )
    )

    pio.show(fig)

# uso
points = [
    ([1, 2, 3], [4, 5, 6], [7, 8, 9])
]
plot_image(points)



