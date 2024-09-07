# mundo.py
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

from plots import plot_solid_box, plot_solid_cano, plot_solid_cone, plot_solid_tronco, plot_solid_mug
from src.mug import create_mug


def create_3d_lines():
    lines = [
        {'x': [0, 0], 'y': [0, 0], 'z': [-10, 10]},
        {'x': [0, 0], 'y': [-10, 10], 'z': [0, 0]},
        {'x': [-10, 10], 'y': [0, 0], 'z': [0, 0]}
    ]
    return lines


def compute_camera_basis(solid_centers):
    # Compute the average center of all solids
    average_center = np.mean(solid_centers, axis=0)

    # Define the new camera basis vectors (unit vectors along the coordinate axes)
    camera_basis = np.eye(3)  # For simplicity, assuming that the camera basis is aligned with the world axes

    # Compute the transformation matrix from world to camera coordinates
    translation = -average_center
    transformation_matrix = np.hstack([camera_basis, translation.reshape(-1, 1)])
    transformation_matrix = np.vstack([transformation_matrix, [0, 0, 0, 1]])

    return transformation_matrix


def transform_coordinates(points, transformation_matrix):
    points_transformed = []
    for point_set in points:
        # Convert the points to homogeneous coordinates
        points_homogeneous = np.vstack([np.array(point_set), np.ones(len(point_set[0]))])
        # Apply the transformation matrix
        points_transformed_homogeneous = transformation_matrix @ points_homogeneous
        # Convert back to non-homogeneous coordinates
        points_transformed = [points_transformed_homogeneous[0, :], points_transformed_homogeneous[1, :],
                              points_transformed_homogeneous[2, :]]
        points_transformed.append(points_transformed)

    return points_transformed


def plot_image(points, mundo=None, box_params=None, cano_params=None, cone_params=None, tronco_params=None,
               mug_params=None):
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
        plot_solid_box(fig, *box_params)

    if cano_params:
        p0, p1, t0, t1, radius = cano_params
        plot_solid_cano(fig, p0, p1, t0, t1, radius)

    if cone_params:
        radius, height = cone_params
        plot_solid_cone(fig, radius, height)

    if tronco_params:
        radius1, radius2, height = tronco_params
        plot_solid_tronco(fig, radius1, radius2, height)

    if mug_params:
        plot_solid_mug(fig, mug_params)

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
    # Definir os centros de massa dos sólidos
    box_center = np.array([2, 2, 2])
    cano_center = (np.array([1, 1, 1]) + np.array([2, 2, 2])) / 2
    cone_center = np.array([0, 0, 0])
    tronco_center = np.array([0, 0, 0])
    mug_center = np.array([0, 0, 0])

    solid_centers = np.array([box_center, cano_center, cone_center, tronco_center, mug_center])

    # Calcular a matriz de transformação
    transformation_matrix = compute_camera_basis(solid_centers)

    # Coordenadas dos sólidos (exemplo de dados)
    points = [
        ([0, 0, 0], [0, 0, 0], [0, 0, 0])  # Exemplo de dados vazios
    ]

    # Transformar coordenadas para o sistema de coordenadas da câmera
    points_transformed = transform_coordinates(points, transformation_matrix)

    box_params = (5, 0.5)  # Lado da caixa e deslocamento do cubo interno
    cano_params = (np.array([1, 1, 1]), np.array([2, 2, 2]), np.array([2, 1, 1]), np.array([1, 2, 1]), 0.5)
    cone_params = (1, 3)  # Raio e altura do cone
    tronco_params = (2, 1, 2)  # Raio 1, Raio 2 e altura do tronco
    mug_params = create_mug()  # Adiciona a caneca

    plot_image(points_transformed, box_params=box_params, cano_params=cano_params, cone_params=cone_params,
               tronco_params=tronco_params, mug_params=mug_params)


if __name__ == "__main__":
    main()
