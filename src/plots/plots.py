# plots.py
import plotly.graph_objects as go

from src.objects.box import create_open_box
from src.objects.cone import create_cone
from src.objects.coneTrunk import create_tronco
from src.objects.pipe import generate_cano_coordinates


def plot_solid_box(fig, side_length):
    vertices, faces = create_open_box(side_length)
    vertices[:, 0] -= 7.5
    vertices[:, 1] += 7.5

    for face in faces:
        x = [vertices[i][0] for i in face['vertices']] + [vertices[face['vertices'][0]][0]]
        y = [vertices[i][1] for i in face['vertices']] + [vertices[face['vertices'][0]][1]]
        z = [vertices[i][2] for i in face['vertices']] + [vertices[face['vertices'][0]][2]]
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color='blue')
        ))


def plot_solid_cano(fig, p0, p1, t0, t1, radius):
    curve_points, circle_points_list = generate_cano_coordinates(p0, p1, t0, t1, radius)

    for circle_points in circle_points_list:
        circle_points[:, 0] -= 7.5  # Translada no eixo X
        circle_points[:, 1] -= 7.5  # Translada no eixo Y
        fig.add_trace(go.Scatter3d(
            x=circle_points[:, 0],
            y=circle_points[:, 1],
            z=circle_points[:, 2],
            mode='lines',
            line=dict(color='blue')
        ))

    num_circles = len(circle_points_list)
    for i in range(num_circles - 1):
        current_circle = circle_points_list[i]
        next_circle = circle_points_list[i + 1]
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

    num_circles = len(circle_points_list)
    for i in range(num_circles - 1):
        current_circle = circle_points_list[i]
        next_circle = circle_points_list[i + 1]
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

def plot_solid_cone(fig, radius, height):
    vertices, faces = create_cone(radius, height)
    vertices[:, 0] -= 7.5
    vertices[:, 1] -= 7.5
    for face in faces:
        x = [vertices[i][0] for i in face['vertices']]
        y = [vertices[i][1] for i in face['vertices']]
        z = [vertices[i][2] for i in face['vertices']]
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color='orange')
        ))

def plot_solid_tronco(fig, radius1, radius2, height):
    vertices, faces = create_tronco(radius1, radius2, height)
    vertices[:, 0] -= 6
    vertices[:, 1] += 7.5

    for face in faces:
        x = [vertices[i][0] for i in face['vertices']]
        y = [vertices[i][1] for i in face['vertices']]
        z = [vertices[i][2] for i in face['vertices']]
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color='purple')
        ))


def plot_solid_mug(fig, mug_params):
    # Desempacote os valores conforme esperado
    if len(mug_params) == 2:
        mug_lines, edge_color = mug_params
    elif len(mug_params) == 3:
        mug_lines, edge_color = mug_params
    else:
        raise ValueError("Número inesperado de valores em mug_params")


    for line in mug_lines:
        x_line = [line[0][0], line[1][0]]
        y_line = [line[0][1], line[1][1]]
        z_line = [line[0][2], line[1][2]]
        fig.add_trace(go.Scatter3d(
            x=x_line,
            y=y_line,
            z=z_line,
            mode='lines',
            line=dict(color=edge_color)  # Usando edge_color em vez de cor fixa
        ))

