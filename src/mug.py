import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from src.cano import generate_cano_coordinates
from src.hermite import hermite


def generate_circle(center, tangent, radius, num_points):
    theta = np.linspace(0, 2 * np.pi, num_points)
    v = np.cross(tangent, [1, 0, 0])
    if np.linalg.norm(v) < 1e-6:
        v = np.cross(tangent, [0, 1, 0])
    v /= np.linalg.norm(v)
    u = np.cross(tangent, v)
    u /= np.linalg.norm(u)
    circle = np.array([center + radius * (np.cos(t) * u + np.sin(t) * v) for t in theta])
    return circle

def create_cano(p0, t0, p1, t1, num_pointsH=20, num_pointsC=20, radius=0.5):
    cano = []
    edge_color = "#bc57cd"
    face_color = "#ffd700"

    # Gera os pontos ao longo da curva e os círculos transversais
    curve_points, circle_points_list = generate_cano_coordinates(p0, p1, t0, t1, radius, num_pointsH, num_pointsC)

    previous_circle = None
    for i in range(len(circle_points_list)):
        circle = circle_points_list[i]

        if previous_circle is not None:
            for j in range(len(circle) - 1):
                cano.append([previous_circle[j], previous_circle[j + 1], circle[j + 1], circle[j]])

        previous_circle = circle

    return cano, face_color, edge_color


def create_mug(height=1, radius=1, num_points_mug=20, handle_radius=0.1,
               num_points_handle=20, num_points_handle_circle=20):
    face_color = "#215b20"
    edge_color = "#52ed0a"

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

    mug_cylinder = []
    for i in range(len(base_vertices_bottom) - 1):
        if i == num_points_mug // 2 - 1:
            continue
        p1 = base_vertices_bottom[i]
        p2 = base_vertices_bottom[i + 1]
        p3 = base_vertices_top[i + 1]
        p4 = base_vertices_top[i]
        mug_cylinder.append([p1, p2, p3, p4])

    mug_cylinder += [base_vertices_bottom]

    p0_handler = np.array([radius, 0, height * 0.25])
    p1_handler = np.array([radius, 0, height * 0.75])
    arc_t1_handler = np.array([radius, 0, 0])
    arc_t2_handler = np.array([-radius, 0, 0])

    cano, face_color_handle, edge_color_handle = create_cano(p0_handler, arc_t1_handler, p1_handler,
                                arc_t2_handler, num_points_handle, num_points_handle_circle, handle_radius)
    mug_cylinder += cano

    return mug_cylinder, face_color, edge_color

def plot_3d(ax, polygon, face_color, edge_color):
    poly3d = Poly3DCollection(polygon, facecolors=face_color, edgecolors=edge_color)
    ax.add_collection3d(poly3d)
    ax.auto_scale_xyz([-5, 5], [-5, 5], [-5, 5])

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    caneca1, face_color, edge_color = create_mug()
    caneca1 = [np.array(polygon) for polygon in caneca1]
    plot_3d(ax, caneca1, face_color, edge_color)

    plt.show()

if __name__ == "__main__":
    main()
