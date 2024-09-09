import numpy as np
def transform_vertices(vertices, rotation_matrix, translation_vector):
    """Aplica a rotação e a translação aos vértices."""
    return np.dot(vertices, rotation_matrix.T) + translation_vector

def apply_transformation(vertices, scale, rotation, translation):
    """Aplica a escala, rotação e translação aos vértices."""
    scaled_vertices = vertices * scale
    rotated_vertices = np.dot(scaled_vertices, rotation.T)
    translated_vertices = rotated_vertices + translation
    return translated_vertices
