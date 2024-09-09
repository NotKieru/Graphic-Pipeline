import numpy as np
import plotly.graph_objects as go

def create_open_box(side_length):
    """
    Cria uma caixa de madeira sem tampa com base quadrada e altura igual ao comprimento dos lados.
    """
    half_side = side_length / 2
    vertices = np.array([
        [-half_side, -half_side, 0],  # Vértice 0
        [half_side, -half_side, 0],  # Vértice 1
        [half_side, half_side, 0],  # Vértice 2
        [-half_side, half_side, 0],  # Vértice 3
        [-half_side, -half_side, side_length],  # Vértice 4
        [half_side, -half_side, side_length],  # Vértice 5
        [half_side, half_side, side_length],  # Vértice 6
        [-half_side, half_side, side_length],  # Vértice 7
    ])

    faces = [
        {'vertices': [0, 1, 2, 3], 'color': 'lightblue'},  # Base
        {'vertices': [0, 1, 5, 4], 'color': 'lightgrey'},  # Lateral 1
        {'vertices': [1, 2, 6, 5], 'color': 'lightgrey'},  # Lateral 2
        {'vertices': [2, 3, 7, 6], 'color': 'lightgrey'},  # Lateral 3
        {'vertices': [3, 0, 4, 7], 'color': 'lightgrey'},  # Lateral 4
    ]

    return vertices, faces

def create_inner_box(side_length, offset):
    """
    Cria um cubo interno menor e retorna seus vértices e arestas.
    """
    half_side = side_length / 2
    inner_half_side = half_side - offset
    vertices = np.array([
        [-inner_half_side, -inner_half_side, offset],  # Vértice 0
        [inner_half_side, -inner_half_side, offset],  # Vértice 1
        [inner_half_side, inner_half_side, offset],  # Vértice 2
        [-inner_half_side, inner_half_side, offset],  # Vértice 3
        [-inner_half_side, -inner_half_side, side_length - offset],  # Vértice 4
        [inner_half_side, -inner_half_side, side_length - offset],  # Vértice 5
        [inner_half_side, inner_half_side, side_length - offset],  # Vértice 6
        [-inner_half_side, inner_half_side, side_length - offset]  # Vértice 7
    ])

    faces = [
        {'vertices': [0, 1, 2, 3], 'color': 'lightblue'},  # Base
        {'vertices': [0, 1, 5, 4], 'color': 'lightgrey'},  # Lateral 1
        {'vertices': [1, 2, 6, 5], 'color': 'lightgrey'},  # Lateral 2
        {'vertices': [2, 3, 7, 6], 'color': 'lightgrey'},  # Lateral 3
        {'vertices': [3, 0, 4, 7], 'color': 'lightgrey'},  # Lateral 4
    ]

    return vertices, faces

def plot_x_and_plus_on_face(fig, v0, v1, v2, v3):
    """
    Adiciona um 'X' e um '+' nas faces superiores de uma caixa.
    """
    # Diagonais cruzadas formando um "X"
    for (start, end) in [(v0, v2), (v1, v3)]:
        fig.add_trace(go.Scatter3d(
            x=[start[0], end[0]],
            y=[start[1], end[1]],
            z=[start[2], end[2]],
            mode='lines',
            line=dict(color='green')
        ))

    # Linhas formando um "+"
    center_x = (v0[0] + v2[0]) / 2
    center_y = (v0[1] + v2[1]) / 2
    center_z = (v0[2] + v2[2]) / 2

    fig.add_trace(go.Scatter3d(
        x=[v0[0], v1[0]],
        y=[v0[1], v1[1]],
        z=[center_z, center_z],
        mode='lines',
        line=dict(color='green')
    ))

    fig.add_trace(go.Scatter3d(
        x=[center_x, center_x],
        y=[v0[1], v1[1]],
        z=[v0[2], v2[2]],
        mode='lines',
        line=dict(color='green')
    ))

def plot_x_and_plus_on_lateral_faces(fig, vertices, faces):
    """
    Adiciona um 'X' e um '+' nas faces laterais da caixa externa.
    """
    for face in faces:
        if face['vertices'] != [0, 1, 2, 3]:  # Ignora a face da base
            v0 = vertices[face['vertices'][0]]
            v1 = vertices[face['vertices'][1]]
            v2 = vertices[face['vertices'][2]]
            v3 = vertices[face['vertices'][3]]
            plot_x_and_plus_on_face(fig, v0, v1, v2, v3)