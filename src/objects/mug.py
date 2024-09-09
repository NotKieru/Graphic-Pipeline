import numpy as np

from src.objects.pipe import generate_cano_coordinates, hermite


def create_mug(height=1, radius=1, num_points_mug=20, handle_radius=0.1,
               num_points_handle=35, num_points_handle_circle=20):
    edge_color = "orange"

    # Definindo pontos para a base e topo do mug
    p0_bottom = np.array([0, 0, 0])
    p1_bottom = np.array([radius, 0, 0])
    arc_t1_bottom = np.array([0, radius * 2, 0])
    arc_t2_bottom = np.array([0, -radius * 2, 0])

    p0_top = np.array([0, 0, height])
    p1_top = np.array([radius, 0, height])
    arc_t1_top = np.array([0, radius * 2, 0])
    arc_t2_top = np.array([0, -radius * 2, 0])

    # Gerar vértices da base e topo
    base_vertices_bottom = np.vstack([
        hermite(p0_bottom, arc_t1_bottom, p1_bottom, arc_t2_bottom, round(num_points_mug / 2)),
        hermite(p0_bottom, arc_t2_bottom, p1_bottom, arc_t1_bottom, round(num_points_mug / 2))
    ])

    base_vertices_top = np.vstack([
        hermite(p0_top, arc_t1_top, p1_top, arc_t2_top, round(num_points_mug / 2)),
        hermite(p0_top, arc_t2_top, p1_top, arc_t1_top, round(num_points_mug / 2))
    ])

    # Criar linhas para o mug
    mug_lines = []
    num_points = len(base_vertices_bottom)

    for i in range(num_points):
        mug_lines.append([base_vertices_bottom[i], base_vertices_bottom[(i + 1) % num_points]])

    for i in range(num_points):
        mug_lines.append([base_vertices_top[i], base_vertices_top[(i + 1) % num_points]])

    for i in range(num_points):
        mug_lines.append([base_vertices_bottom[i], base_vertices_top[i]])

    # Definir pontos para o alça
    p0_handler = np.array([radius, 0, height * 0.25])
    p1_handler = np.array([radius, 0, height * 0.75])
    arc_t1_handler = np.array([radius, 0, 0])
    arc_t2_handler = np.array([-radius, 0, 0])

    # Gerar coordenadas do cano
    cano = generate_cano_coordinates(p0_handler, p1_handler, arc_t1_handler, arc_t2_handler,
                                     handle_radius, num_points_handle, num_points_handle_circle)

    for circle in cano[1]:
        for i in range(len(circle)):
            mug_lines.append([circle[i], circle[(i + 1) % len(circle)]])

    return mug_lines, edge_color