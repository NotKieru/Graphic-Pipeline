import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

from src.plots.boxPlot import plot_solid_box
from src.plots.conePlot import plot_solid_cone
from src.plots.coneTrunk import plot_solid_tronco
from src.plots.mugPlot import plot_solid_mug
from src.plots.pipePlot import plot_solid_cano


def transform_vertices(vertices, rotation_matrix, translation_vector):
    """Aplica a rotação e a translação aos vértices."""
    return np.dot(vertices, rotation_matrix.T) + translation_vector

def apply_transformation(vertices, scale, rotation, translation):
    """Aplica a escala, rotação e translação aos vértices."""
    scaled_vertices = vertices * scale
    rotated_vertices = np.dot(scaled_vertices, rotation.T)
    translated_vertices = rotated_vertices + translation
    return translated_vertices

def create_3d_lines():
    lines = [
        {'x': [-10, 10], 'y': [0, 0], 'z': [0, 0]},
        {'x': [0, 0], 'y': [-10, 10], 'z': [0, 0]},
        {'x': [0, 0], 'y': [0, 0], 'z': [-10, 10]}
    ]
    return lines

def get_octant_config(octant):
    if octant == 1:
        return {
            'xaxis': dict(range=[0, 10]),
            'yaxis': dict(range=[0, 10]),
            'zaxis': dict(range=[0, 10]),
            'camera': {
                'eye': dict(x=10, y=10, z=10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    elif octant == 2:
        return {
            'xaxis': dict(range=[-10, 0]),
            'yaxis': dict(range=[0, 10]),
            'zaxis': dict(range=[0, 10]),
            'camera': {
                'eye': dict(x=-10, y=10, z=10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    elif octant == 3:
        return {
            'xaxis': dict(range=[0, 10]),
            'yaxis': dict(range=[-10, 0]),
            'zaxis': dict(range=[0, 10]),
            'camera': {
                'eye': dict(x=10, y=-10, z=10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    elif octant == 4:
        return {
            'xaxis': dict(range=[-10, 0]),
            'yaxis': dict(range=[-10, 0]),
            'zaxis': dict(range=[0, 10]),
            'camera': {
                'eye': dict(x=-10, y=-10, z=10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    elif octant == 5:
        return {
            'xaxis': dict(range=[0, 10]),
            'yaxis': dict(range=[0, 10]),
            'zaxis': dict(range=[-10, 0]),
            'camera': {
                'eye': dict(x=10, y=10, z=-10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    elif octant == 6:
        return {
            'xaxis': dict(range=[-10, 0]),
            'yaxis': dict(range=[0, 10]),
            'zaxis': dict(range=[-10, 0]),
            'camera': {
                'eye': dict(x=-10, y=10, z=-10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    elif octant == 7:
        return {
            'xaxis': dict(range=[0, 10]),
            'yaxis': dict(range=[-10, 0]),
            'zaxis': dict(range=[-10, 0]),
            'camera': {
                'eye': dict(x=10, y=-10, z=-10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    elif octant == 8:
        return {
            'xaxis': dict(range=[-10, 0]),
            'yaxis': dict(range=[-10, 0]),
            'zaxis': dict(range=[-10, 0]),
            'camera': {
                'eye': dict(x=-10, y=-10, z=-10),
                'center': dict(x=0, y=0, z=0),
                'up': dict(x=0, y=0, z=1)
            }
        }
    else:
        raise ValueError("Octante inválido. Escolha um valor entre 1 e 8.")

def plot_image(octante, box_params=None, cone_params=None, cano_params=None, tronco_params=None, mug_params=None):
    fig = go.Figure()

    if box_params:
        plot_solid_box(fig, *box_params)

    if cone_params:
        plot_solid_cone(fig, *cone_params)

    if cano_params:
        plot_solid_cano(fig, *cano_params)

    if tronco_params:
        plot_solid_tronco(fig, *tronco_params)

    if mug_params:
        plot_solid_mug(fig, mug_params)

    # Adicionar linhas para o sistema de coordenadas ou outros elementos 3D
    lines = create_3d_lines()
    for line in lines:
        fig.add_trace(go.Scatter3d(
            x=line['x'],
            y=line['y'],
            z=line['z'],
            mode='lines',
            line=dict(color='black')
        ))

    octant_config = get_octant_config(octante)
    fig.update_layout(
        scene=dict(
            xaxis=octant_config['xaxis'],
            yaxis=octant_config['yaxis'],
            zaxis=octant_config['zaxis'],
            aspectmode="manual",
            camera=dict(
                eye=octant_config['camera']['eye'],
                up=octant_config['camera']['up'],
                center=octant_config['camera']['center']
            )
        )
    )

    pio.show(fig)

