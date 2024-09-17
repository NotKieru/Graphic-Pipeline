import plotly.graph_objects as go

from src.helpers.transformations import apply_transformation
from src.objects.pipe import *


def plot_solid_cano(fig, p0, p1, t0, t1, radius):
    curve_points, circle_points_list = generate_cano_coordinates(p0, p1, t0, t1, radius)

    # Transformação para o cano
    scale = np.array([1, 1, 1])
    rotation = np.eye(3)  # Identidade (sem rotação)
    translation = np.array([-5, 5, 2])  # Translação para o octante desejado

    transformed_circle_points_list = []

    # Transformar cada conjunto de pontos de círculo
    for circle_points in circle_points_list:
        transformed_points = apply_transformation(circle_points, scale, rotation, translation)
        transformed_circle_points_list.append(transformed_points)

        # Adicionar o círculo ao gráfico
        fig.add_trace(go.Scatter3d(
            x=transformed_points[:, 0],
            y=transformed_points[:, 1],
            z=transformed_points[:, 2],
            mode='lines',
            line=dict(color='blue')
        ))

    num_circles = len(transformed_circle_points_list)

    # Adicionar arestas conectando os círculos adjacentes
    for i in range(num_circles - 1):
        current_circle = transformed_circle_points_list[i]
        next_circle = transformed_circle_points_list[i + 1]
        num_circle_points = len(current_circle)

        for j in range(num_circle_points):
            x_line = [current_circle[j][0], next_circle[j][0]]
            y_line = [current_circle[j][1], next_circle[j][1]]
            z_line = [current_circle[j][2], next_circle[j][2]]
            fig.add_trace(go.Scatter3d(
                x=x_line,
                y=y_line,
                z=z_line,
                mode='lines',
                line=dict(color='blue')
            ))