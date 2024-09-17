import numpy as np
import plotly.graph_objects as go

from src.helpers.transformations import apply_transformation


def plot_solid_mug(fig, mug_params):
    if len(mug_params) == 2:
        mug_lines, edge_color = mug_params
    else:
        raise ValueError("Número inesperado de valores em mug_params")

    # Transformação para a caneca
    scale = np.array([1, 1, 1])
    rotation = np.eye(3)  # Identidade (sem rotação)
    translation = np.array([6, -6, 3])  # Translação para o octante diferente do tronco e cano

    # Aplicar a transformação
    transformed_lines = []
    for line in mug_lines:
        start_point = apply_transformation(np.array([line[0]]), scale, rotation, translation)[0]
        end_point = apply_transformation(np.array([line[1]]), scale, rotation, translation)[0]
        transformed_lines.append((start_point, end_point))

    # Plotar as linhas transformadas
    for line in transformed_lines:
        x = [line[0][0], line[1][0]]
        y = [line[0][1], line[1][1]]
        z = [line[0][2], line[1][2]]
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color=edge_color)
        ))
