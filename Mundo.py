import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

def create_dataframe_from_points(point_set):
    """
    Cria um DataFrame a partir de um conjunto de pontos.
    Cada item em 'point_set' deve ser uma lista de coordenadas (x, y, z).
    """
    if len(point_set) != 3:
        raise ValueError("Cada item em 'point_set' deve ser uma lista de três listas (x, y, z).")
    return pd.DataFrame({"x": point_set[0], "y": point_set[1], "z": point_set[2]})

def generate_random_color():
    """
    Gera uma cor RGB aleatória.
    """
    color = np.random.randint(255, size=3)
    return f'rgb({color[0]}, {color[1]}, {color[2]})'

def create_3d_lines():
    """
    Cria linhas de referência para os eixos x, y e z.
    """
    lines = [
        {'x': [0, 0], 'y': [0, 0], 'z': [-20, 20]},
        {'x': [0, 0], 'y': [-20, 20], 'z': [0, 0]},
        {'x': [-20, 20], 'y': [0, 0], 'z': [0, 0]}
    ]
    return lines

def plot_image(points, mundo=[[0],[0],[0],[1]]):
    """
    Plota um gráfico 3D dos pontos fornecidos e um ponto adicional 'mundo'.
    """
    # Criação dos DataFrames e gráficos para os pontos
    dataframes = [create_dataframe_from_points(point_set) for point_set in points]
    traces = [px.line_3d(df, x="x", y="y", z="z", color_discrete_sequence=[generate_random_color()]).data[0] for df in dataframes]

    # Criação da figura principal
    fig = go.Figure(data=traces)

    # Adição das linhas de referência (eixos)
    lines = create_3d_lines()
    for line in lines:
        fig.add_scatter3d(mode='lines', x=line['x'], y=line['y'], z=line['z'], line=dict(color='black'))

    # Adição do ponto 'mundo'
    df_mundo = pd.DataFrame({'x': mundo[0], 'y': mundo[1], 'z': mundo[2]})
    fig.add_trace(px.scatter_3d(df_mundo, x='x', y='y', z='z', size=[0.5]).data[0])

    # Atualização do layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[-20, 20]),
            yaxis=dict(range=[-20, 20]),
            zaxis=dict(range=[-20, 20]),
            aspectmode="cube",
        )
    )

    # Exibição do gráfico
    pio.show(fig)

# Exemplo de uso
points = [
    ([1, 2, 3], [4, 5, 6], [7, 8, 9])
]
plot_image(points)
