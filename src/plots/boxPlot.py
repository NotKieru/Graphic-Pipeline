from src.helpers.transformations import transform_vertices
from src.objects.box import *


def plot_solid_box(fig, side_length, inner_offset):
    vertices, faces = create_open_box(side_length)
    inner_vertices, inner_faces = create_inner_box(side_length, inner_offset)

    # Defina a base vetorial da câmera e o vetor de translação
    R = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    t = np.array([-5, 5, 0])

    # Transforme os vértices
    transformed_vertices = transform_vertices(vertices, R, t)
    transformed_inner_vertices = transform_vertices(inner_vertices, R, t)

    # Adiciona as faces externas
    for face in faces:
        x = [transformed_vertices[i][0] for i in face['vertices']] + [transformed_vertices[face['vertices'][0]][0]]
        y = [transformed_vertices[i][1] for i in face['vertices']] + [transformed_vertices[face['vertices'][0]][1]]
        z = [transformed_vertices[i][2] for i in face['vertices']] + [transformed_vertices[face['vertices'][0]][2]]
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color='green')
        ))

    # Adiciona as faces internas
    for face in inner_faces:
        x = [transformed_inner_vertices[i][0] for i in face['vertices']] + [transformed_inner_vertices[face['vertices'][0]][0]]
        y = [transformed_inner_vertices[i][1] for i in face['vertices']] + [transformed_inner_vertices[face['vertices'][0]][1]]
        z = [transformed_inner_vertices[i][2] for i in face['vertices']] + [transformed_inner_vertices[face['vertices'][0]][2]]
        fig.add_trace(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color='green')
        ))

    # Conecta os vértices internos aos externos mais próximos
    for inner_vertex in transformed_inner_vertices:
        distances = np.linalg.norm(transformed_vertices - np.array(inner_vertex), axis=1)
        closest_vertex_index = np.argmin(distances)
        closest_vertex = transformed_vertices[closest_vertex_index]
        fig.add_trace(go.Scatter3d(
            x=[inner_vertex[0], closest_vertex[0]],
            y=[inner_vertex[1], closest_vertex[1]],
            z=[inner_vertex[2], closest_vertex[2]],
            mode='lines',
            line=dict(color='green')
        ))

    # Adiciona 'X' e '+' nas faces superiores e laterais da caixa externa
    top_faces = [0]  # Apenas a base da caixa externa
    for i in top_faces:
        v0 = transformed_vertices[faces[i]['vertices'][0]]
        v1 = transformed_vertices[faces[i]['vertices'][1]]
        v2 = transformed_vertices[faces[i]['vertices'][2]]
        v3 = transformed_vertices[faces[i]['vertices'][3]]
        plot_x_and_plus_on_face(fig, v0, v1, v2, v3)

    # Adiciona 'X' e '+' nas faces laterais da caixa externa
    plot_x_and_plus_on_lateral_faces(fig, transformed_vertices, faces)

