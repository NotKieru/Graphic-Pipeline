# mundo3D.py
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

from plots import plot_solid_box, plot_solid_cano, plot_solid_cone, plot_solid_tronco


def create_3d_lines():
    lines = [
        {'x': [0, 0], 'y': [0, 0], 'z': [-10, 10]},
        {'x': [0, 0], 'y': [-10, 10], 'z': [0, 0]},
        {'x': [-10, 10], 'y': [0, 0], 'z': [0, 0]}
    ]
    return lines

def plot_image(points, mundo=None, box_params=None, cano_params=None, cone_params=None, tronco_params=None):
    if mundo is None:
        mundo = [[0], [0], [0], [1]]

    dataframes = [pd.DataFrame({"x": point_set[0], "y": point_set[1], "z": point_set[2]}) for point_set in points]
    traces = [go.Scatter3d(
        x=df["x"],
        y=df["y"],
        z=df["z"],
        mode='lines',
        line=dict(color='grey')  # Cor cinza para pontos não sólidos
    ) for df in dataframes]

    fig = go.Figure(data=traces)

    # Adiciona as linhas de referência
    lines = create_3d_lines()
    for line in lines:
        fig.add_trace(go.Scatter3d(
            x=line['x'],
            y=line['y'],
            z=line['z'],
            mode='lines',
            line=dict(color='black')
        ))

    # Adiciona os pontos de referência
    df_mundo = pd.DataFrame({'x': mundo[0], 'y': mundo[1], 'z': mundo[2]})
    fig.add_trace(go.Scatter3d(
        x=df_mundo['x'],
        y=df_mundo['y'],
        z=df_mundo['z'],
        mode='markers',
        marker=dict(size=5, color='red')
    ))

    # Adiciona os sólidos
    if box_params:
        plot_solid_box(fig, box_params)

    if cano_params:
        p0, p1, t0, t1, radius = cano_params
        plot_solid_cano(fig, p0, p1, t0, t1, radius)

    if cone_params:
        radius, height = cone_params
        plot_solid_cone(fig, radius, height)

    if tronco_params:
        radius1, radius2, height = tronco_params
        plot_solid_tronco(fig, radius1, radius2, height)

    fig.update_layout(
        scene=dict(
            xaxis=dict(range=[-10, 10]),
            yaxis=dict(range=[-10, 10]),
            zaxis=dict(range=[-10, 10]),
            aspectmode="cube",
        )
    )

    pio.show(fig)


def main():
    points = [
        ([0, 0, 0], [0, 0, 0], [0, 0, 0]) #gambiarra pra sumir com a reta cinza
    ]
    box_params = 5  # Lado da caixa
    cano_params = (np.array([1, 1, 1]), np.array([2, 2, 2]), np.array([2, 1, 1]), np.array([1, 2, 1]), 0.5)
    cone_params = (1, 3)  # Raio e altura do cone
    tronco_params = (2, 1, 2)  # Raio 1, Raio 2 e altura do tronco
    plot_image(points, box_params=box_params, cano_params=cano_params, cone_params=cone_params, tronco_params=tronco_params)


if __name__ == "__main__":
    main()
