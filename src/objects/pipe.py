import numpy as np

from src.helpers.hermite import hermite


def generate_cano_coordinates(p0, p1, t0, t1, radius, num_points=20, num_circle_points=30):
    curve_points = hermite(p0, t0, p1, t1, num_points)
    circle_points_list = []

    theta = np.linspace(0, 2 * np.pi, num_circle_points)

    for i in range(len(curve_points) - 1):
        p1 = curve_points[i]
        p2 = curve_points[i + 1]

        direction = p2 - p1
        direction = direction / np.linalg.norm(direction)

        a = np.array([1, 0, 0])
        if np.allclose(direction, a):
            a = np.array([0, 1, 0])
        b = np.cross(direction, a)
        b = b / np.linalg.norm(b)
        a = np.cross(b, direction)

        circle_points = []
        for j in range(num_circle_points):
            x = radius * np.cos(theta[j])
            y = radius * np.sin(theta[j])
            z = 0
            circle_point = x * a + y * b
            circle_points.append(p1 + circle_point)

        circle_points_list.append(np.array(circle_points))

    return curve_points, circle_points_list