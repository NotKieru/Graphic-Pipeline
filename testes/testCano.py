import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def hermite_curve(p0, p1, t0, t1, num_points=100):
    t = np.linspace(0, 1, num_points)
    h00 = 2 * t**3 - 3 * t**2 + 1
    h01 = -2 * t**3 + 3 * t**2
    h10 = t**3 - 2 * t**2 + t
    h11 = t**3 - t**2
    
    curve = (h00[:, np.newaxis] * p0 + 
             h01[:, np.newaxis] * p1 + 
             h10[:, np.newaxis] * t0 + 
             h11[:, np.newaxis] * t1)
    return curve

def plot_cano(p0, p1, t0, t1, radius, num_points=20, num_circle_points=30, num_edges=50):
    curve_points = hermite_curve(p0, p1, t0, t1, num_points)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    theta = np.linspace(0, 2 * np.pi, num_circle_points)
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)
    circle_z = np.zeros(num_circle_points)
    
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
            x = circle_x[j]
            y = circle_y[j]
            z = circle_z[j]
            circle_point = x * a + y * b + z * direction
            circle_points.append(p1 + circle_point)
        circle_points = np.array(circle_points)
        
        ax.plot(circle_points[:, 0], circle_points[:, 1], circle_points[:, 2], color='b')
        
        if i < len(curve_points) - 1:
            next_circle_points = []
            for k in range(num_circle_points):
                x = circle_x[k]
                y = circle_y[k]
                z = circle_z[k]
                next_circle_point = x * a + y * b + z * direction
                next_circle_points.append(p2 + next_circle_point)
            next_circle_points = np.array(next_circle_points)
            
            edge_indices = np.linspace(0, num_circle_points - 1, num_edges, dtype=int)
            for edge in edge_indices:
                next_edge = (edge + 1) % num_circle_points
                ax.plot([circle_points[edge, 0], next_circle_points[edge, 0]], 
                        [circle_points[edge, 1], next_circle_points[edge, 1]], 
                        [circle_points[edge, 2], next_circle_points[edge, 2]], 
                        color='b')
                ax.plot([circle_points[next_edge, 0], next_circle_points[next_edge, 0]], 
                        [circle_points[next_edge, 1], next_circle_points[next_edge, 1]], 
                        [circle_points[next_edge, 2], next_circle_points[next_edge, 2]], 
                        color='b')
    
    ax.plot(curve_points[:, 0], curve_points[:, 1], curve_points[:, 2], color='r', label='Curva de Hermite')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()

P1 = np.array([0, 0, 0])
P2 = np.array([1, 1, 1])
T1 = np.array([1, 0, 0])
T2 = np.array([0, 1, 0])
radius = 0.1
num_edges = 10

plot_cano(P1, P2, T1, T2, radius, num_edges=num_edges)
