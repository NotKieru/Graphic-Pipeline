import numpy as np

from src.objects.box import create_inner_box, create_open_box
from src.objects.cone import create_cone
from src.objects.coneTrunk import create_tronco
from src.objects.pipe import generate_cano_coordinates


def apply_transformation(vertices, base_vectors):
    return (base_vectors @ vertices.T).T


def translate_vertices(vertices, translation):
    return vertices + translation


def plot_on_plane(ax, vertices, faces, plane, color):
    for face in faces:
        if plane in ['xy', 'yx']:
            x = [vertices[i][0] for i in face['vertices']] + [vertices[face['vertices'][0]][0]]
            y = [vertices[i][1] for i in face['vertices']] + [vertices[face['vertices'][0]][1]]
            ax.plot(x, y, color=color)
        elif plane in ['xz', 'zx']:
            x = [vertices[i][0] for i in face['vertices']] + [vertices[face['vertices'][0]][0]]
            z = [vertices[i][2] for i in face['vertices']] + [vertices[face['vertices'][0]][2]]
            ax.plot(x, z, color=color)
        elif plane in ['yz', 'zy']:
            y = [vertices[i][1] for i in face['vertices']] + [vertices[face['vertices'][0]][1]]
            z = [vertices[i][2] for i in face['vertices']] + [vertices[face['vertices'][0]][2]]
            ax.plot(y, z, color=color)


def connect_vertices(ax, vertices, inner_vertices, plane, color):
    for inner_vertex in inner_vertices:
        distances = np.linalg.norm(vertices - np.array(inner_vertex), axis=1)
        closest_vertex = vertices[np.argmin(distances)]
        if plane in ['xy', 'yx']:
            ax.plot([inner_vertex[0], closest_vertex[0]], [inner_vertex[1], closest_vertex[1]], color=color)
        elif plane in ['xz', 'zx']:
            ax.plot([inner_vertex[0], closest_vertex[0]], [inner_vertex[2], closest_vertex[2]], color=color)
        elif plane in ['yz', 'zy']:
            ax.plot([inner_vertex[1], closest_vertex[1]], [inner_vertex[2], closest_vertex[2]], color=color)


def plot_solid_box(ax, base_vectors, side_length, inner_offset, plane):
    vertices, faces = create_open_box(side_length)
    inner_vertices, inner_faces = create_inner_box(side_length, inner_offset)

    vertices = apply_transformation(vertices, base_vectors)
    inner_vertices = apply_transformation(inner_vertices, base_vectors)

    # Translação
    vertices = translate_vertices(vertices, np.array([-5, 5, 0]))
    inner_vertices = translate_vertices(inner_vertices, np.array([-5, 5, 0]))

    plot_on_plane(ax, vertices, faces, plane, 'green')
    plot_on_plane(ax, inner_vertices, inner_faces, plane, 'green')
    connect_vertices(ax, vertices, inner_vertices, plane, 'green')


def plot_solid_cone(ax, base_vectors, radius1, radius2, height, plane):
    vertices, faces = create_cone(radius1, radius2, height)
    vertices = apply_transformation(vertices, base_vectors)
    vertices = translate_vertices(vertices, np.array([-3, 5, 2]))

    plot_on_plane(ax, vertices, faces, plane, 'black')


def plot_solid_cano(ax, base_vectors, p0, p1, t0, t1, radius, plane):
    curve_points, circle_points_list = generate_cano_coordinates(p0, p1, t0, t1, radius)
    curve_points = apply_transformation(curve_points, base_vectors)
    circle_points_list = [apply_transformation(circle_points, base_vectors) for circle_points in circle_points_list]
    curve_points = translate_vertices(curve_points, np.array([-5, 5, 2]))
    circle_points_list = [translate_vertices(circle_points, np.array([-5, 5, 2])) for circle_points in
                          circle_points_list]

    def plot_circles_and_lines(points, color):
        for circle_points in points:
            ax.plot(circle_points[:, 0], circle_points[:, 1], color=color)
        for i in range(len(points) - 1):
            for j in range(len(points[i])):
                ax.plot([points[i][j][0], points[i + 1][j][0]], [points[i][j][1], points[i + 1][j][1]], color=color)

    plot_circles_and_lines(circle_points_list, 'blue')


def plot_solid_tronco(ax, base_vectors, radius1, radius2, height, plane):
    vertices, faces = create_tronco(radius1, radius2, height)
    vertices = apply_transformation(vertices, base_vectors)
    vertices = translate_vertices(vertices, np.array([6, -6, 6]))

    plot_on_plane(ax, vertices, faces, plane, 'purple')


def plot_solid_mug(ax, base_vectors, mug_params, plane):
    if len(mug_params) not in [2, 3]:
        raise ValueError("Número inesperado de valores em mug_params")

    mug_lines, edge_color = mug_params
    mug_lines = [(
        apply_transformation(np.array([line[0]]), base_vectors)[0],
        apply_transformation(np.array([line[1]]), base_vectors)[0]
    ) for line in mug_lines]

    translation = np.array([6, -6, 3])
    for line in mug_lines:
        x_line = [line[0][0] + translation[0], line[1][0] + translation[0]]
        y_line = [line[0][1] + translation[1], line[1][1] + translation[1]]
        if plane in ['xy', 'yx']:
            ax.plot(x_line, y_line, color=edge_color)
        elif plane in ['xz', 'zx']:
            ax.plot(x_line, [line[0][2] + translation[2], line[1][2] + translation[2]], color=edge_color)
        elif plane in ['yz', 'zy']:
            ax.plot([line[0][1] + translation[1], line[1][1] + translation[1]],
                    [line[0][2] + translation[2], line[1][2] + translation[2]], color=edge_color)


def get_plane_limits(octant):
    if octant == 1:
        return (0, 10, 0, 10)  # x: [0, 10], y: [0, 10]
    elif octant == 2:
        return (-10, 0, 0, 10)  # x: [-10, 0], y: [0, 10]
    elif octant == 3:
        return (0, 10, -10, 0)  # x: [0, 10], y: [-10, 0]
    elif octant == 4:
        return (-10, 0, -10, 0)  # x: [-10, 0], y: [-10, 0]
    elif octant == 5:
        return (0, 10, 0, 10)  # x: [0, 10], z: [0, 10] (equivalente a 'xz')
    elif octant == 6:
        return (-10, 0, 0, 10)  # x: [-10, 0], z: [0, 10] (equivalente a 'xz')
    elif octant == 7:
        return (0, 10, -10, 0)  # x: [0, 10], z: [-10, 0] (equivalente a 'xz')
    elif octant == 8:
        return (-10, 0, -10, 0)  # x: [-10, 0], z: [-10, 0] (equivalente a 'xz')
    else:
        raise ValueError("Octante inválido. Escolha um valor entre 1 e 8.")


def get_plane_for_octant(octant):
    if octant in [1, 2, 3, 4]:
        return 'xy'
    elif octant in [5, 6, 7, 8]:
        return 'xz'
    else:
        raise ValueError("Octante inválido. Escolha um valor entre 1 e 8.")


