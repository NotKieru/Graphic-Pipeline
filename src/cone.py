import numpy as np
def create_cone(radius, height, num_points=30):

    # Vértices da base do cone
    theta = np.linspace(0, 2 * np.pi, num_points)
    base_x = radius * np.cos(theta)
    base_y = radius * np.sin(theta)
    base_z = np.zeros(num_points)

    # Vértices do cone (base e vértice superior)
    vertices = np.vstack([base_x, base_y, base_z]).T
    vertices = np.vstack([vertices, [0, 0, height]])

    # Faces do cone #TODO
    faces = []
    for i in range(num_points):
        next_i = (i + 1) % num_points
        faces.append({'vertices': [i, next_i, num_points], 'color': 'orange'})

    return vertices, faces
