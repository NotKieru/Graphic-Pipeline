import numpy as np
def create_open_box(side_length):
    """
    Cria uma caixa de madeira sem tampa com base quadrada e altura igual ao comprimento dos lados.
    """
    # Definição dos vértices da caixa
    half_side = side_length / 2
    vertices = np.array([
        [-half_side, -half_side, 0],  # Vértice 0
        [half_side, -half_side, 0],   # Vértice 1
        [half_side, half_side, 0],    # Vértice 2
        [-half_side, half_side, 0],   # Vértice 3
        [-half_side, -half_side, side_length],  # Vértice 4
        [half_side, -half_side, side_length],   # Vértice 5
        [half_side, half_side, side_length],    # Vértice 6
        [-half_side, half_side, side_length],   # Vértice 7
    ])

    # Definição das faces da caixa (sem a tampa) #TODO MUdar pra aramado depois
    faces = [
        {'vertices': [0, 1, 2, 3], 'color': 'lightblue'},  # Base
        {'vertices': [0, 1, 5, 4], 'color': 'lightgrey'},  # Lateral 1
        {'vertices': [1, 2, 6, 5], 'color': 'lightgrey'},  # Lateral 2
        {'vertices': [2, 3, 7, 6], 'color': 'lightgrey'},  # Lateral 3
        {'vertices': [3, 0, 4, 7], 'color': 'lightgrey'},  # Lateral 4
    ]

    return vertices, faces
