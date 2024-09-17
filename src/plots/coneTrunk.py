import plotly.graph_objects as go

from src.helpers.transformations import apply_transformation
from src.objects.coneTrunk import *


def plot_solid_tronco(fig, radius1, radius2, height):
    vertices, faces = create_tronco(radius1, radius2, height)

    # Transformação para o tronco de cone
    scale = np.array([1, 1, 1])
    rotation = np.eye(3)  # Identidade (sem rotação)
    translation = np.array([6, -6, 6])  # Translação para o octante diferente

    vertices = apply_transformation(vertices, scale, rotation, translation)

    for face in faces:
        x = [vertices[i][0] for i in face['vertices']]
        y = [vertices[i][1] for i in face['vertices']]
        z = [vertices[i][2] for i in face['vertices']]
        fig.add_trace(go.Scatter3d(
            x=x + [x[0]],  # Fechar o loop
            y=y + [y[0]],  # Fechar o loop
            z=z + [z[0]],  # Fechar o loop
            mode='lines',
            line=dict(color=face['color'])
        ))