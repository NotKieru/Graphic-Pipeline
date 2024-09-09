import numpy as np

def create_tronco(radius1, radius2, height, num_points=30):
    theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    base1_x = radius1 * np.cos(theta)
    base1_y = radius1 * np.sin(theta)
    base1_z = np.zeros(num_points)

    base2_x = radius2 * np.cos(theta)
    base2_y = radius2 * np.sin(theta)
    base2_z = np.ones(num_points) * height

    vertices = np.vstack([base1_x, base1_y, base1_z]).T
    vertices = np.vstack([vertices, np.vstack([base2_x, base2_y, base2_z]).T])

    faces = []

    for i in range(num_points):
        next_i = (i + 1) % num_points
        # Faces laterais
        faces.append({'vertices': [i, next_i, num_points + next_i], 'color': 'purple'})
        faces.append({'vertices': [i, num_points + next_i, num_points + i], 'color': 'purple'})

    # Faces das bases
    base1_start = 0
    base2_start = num_points
    for i in range(num_points):
        next_i = (i + 1) % num_points
        # Face da base inferior
        faces.append({'vertices': [base1_start + i, base1_start + next_i, base1_start], 'color': 'purple'})
        # Face da base superior
        faces.append({'vertices': [base2_start + i, base2_start + next_i, base2_start], 'color': 'purple'})

    return vertices, faces