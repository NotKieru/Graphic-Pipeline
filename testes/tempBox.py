import numpy as np


def create_box(side_length, height, origin=(0, 0, 0)):
    """
    Cria uma caixa de madeira sem tampa.

    Parâmetros:
    - side_length: comprimento do lado da base quadrada.
    - height: altura da caixa.
    - origin: coordenadas da origem do objeto (opcional).

    Retorna:
    - vertices: Matriz de vértices da caixa.
    - edges: Lista de arestas que conectam os vértices.
    """
    ox, oy, oz = origin

    # Definição dos vértices da caixa
    vertices = np.array([
        [ox, oy, oz],  # Vértice 0: base inferior, canto inferior esquerdo
        [ox + side_length, oy, oz],  # Vértice 1: base inferior, canto inferior direito
        [ox + side_length, oy + side_length, oz],  # Vértice 2: base inferior, canto superior direito
        [ox, oy + side_length, oz],  # Vértice 3: base inferior, canto superior esquerdo

        [ox, oy, oz + height],  # Vértice 4: lateral, canto inferior esquerdo
        [ox + side_length, oy, oz + height],  # Vértice 5: lateral, canto inferior direito
        [ox + side_length, oy + side_length, oz + height],  # Vértice 6: lateral, canto superior direito
        [ox, oy + side_length, oz + height]  # Vértice 7: lateral, canto superior esquerdo
    ])

    # Definição das arestas da caixa (sem a tampa)
    edges = [
        (0, 1),  # Base inferior: lado inferior
        (1, 2),
        (2, 3),
        (3, 0),

        (4, 5),  # Face lateral 1
        (5, 6),
        (6, 7),
        (7, 4),

        (0, 4),  # Face lateral 2
        (1, 5),
        (2, 6),
        (3, 7)
    ]

    return vertices, edges
