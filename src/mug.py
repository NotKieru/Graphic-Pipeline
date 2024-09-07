import numpy as np

from src.cano import generate_cano_coordinates
from src.hermite import hermite


def generate_circle(center, tangent, radius, num_points):
    theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    v = np.cross(tangent, [1, 0, 0])
    if np.linalg.norm(v) < 1e-6:
        v = np.cross(tangent, [0, 1, 0])
    v /= np.linalg.norm(v)
    u = np.cross(tangent, v)
    u /= np.linalg.norm(u)
    circle = np.array([center + radius * (np.cos(t) * u + np.sin(t) * v) for t in theta])
    return circle

def create_cano(p0, t0, p1, t1, num_pointsH=25, num_pointsC=20, radius=0.75):
    cano = []
    # Gera os pontos ao longo da curva e os círculos transversais
    curve_points, circle_points_list = generate_cano_coordinates(p0, p1, t0, t1, radius, num_pointsH, num_pointsC)

    previous_circle = None
    for i in range(len(circle_points_list)):
        circle = circle_points_list[i]

        if previous_circle is not None:
            for j in range(len(circle) - 1):
                cano.append([previous_circle[j], previous_circle[j + 1], circle[j + 1], circle[j]])

        previous_circle = circle

    return cano

def create_mug(height=1, radius=1, num_points_mug=20, handle_radius=0.1,
               num_points_handle=35, num_points_handle_circle=20):
    edge_color = "red"

    p0_bottom = np.array([0, 0, 0])
    p1_bottom = np.array([radius, 0, 0])
    arc_t1_bottom = np.array([0, radius * 2, 0])
    arc_t2_bottom = np.array([0, -radius * 2, 0])

    p0_top = np.array([0, 0, height])
    p1_top = np.array([radius, 0, height])
    arc_t1_top = np.array([0, radius * 2, 0])
    arc_t2_top = np.array([0, -radius * 2, 0])

    base_vertices_bottom = np.vstack([
        hermite(p0_bottom, arc_t1_bottom, p1_bottom, arc_t2_bottom, round(num_points_mug / 2)),
        hermite(p0_bottom, arc_t2_bottom, p1_bottom, arc_t1_bottom, round(num_points_mug / 2))
    ])

    base_vertices_top = np.vstack([
        hermite(p0_top, arc_t1_top, p1_top, arc_t2_top, round(num_points_mug / 2)),
        hermite(p0_top, arc_t2_top, p1_top, arc_t1_top, round(num_points_mug / 2))
    ])

    mug_lines = []
    num_points = len(base_vertices_bottom)

    # Conectar os pontos da base inferior entre si
    for i in range(num_points):
        mug_lines.append([base_vertices_bottom[i], base_vertices_bottom[(i + 1) % num_points]])

    # Conectar os pontos da base superior entre si
    for i in range(num_points):
        mug_lines.append([base_vertices_top[i], base_vertices_top[(i + 1) % num_points]])

    # Conectar a base inferior à base superior
    for i in range(num_points):
        mug_lines.append([base_vertices_bottom[i], base_vertices_top[i]])

    # Criar a alça
    p0_handler = np.array([radius, 0, height * 0.25])
    p1_handler = np.array([radius, 0, height * 0.75])
    arc_t1_handler = np.array([radius, 0, 0])
    arc_t2_handler = np.array([-radius, 0, 0])

    cano = create_cano(p0_handler, arc_t1_handler, p1_handler,
                       arc_t2_handler, num_points_handle,
                       num_points_handle_circle, handle_radius)

    # Adiciona a alça
    for circle in cano:
        for i in range(len(circle)):
            mug_lines.append([circle[i], circle[(i + 1) % len(circle)]])

    return mug_lines, edge_color

