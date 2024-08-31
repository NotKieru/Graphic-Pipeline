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

def plot_cano(p0, p1, t0, t1, radius, num_points=20, num_circle_points=50):

    curve_points = hermite_curve(p0, p1, t0, t1, num_points)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for point in curve_points:
        circle_points = []
        for i in range(num_circle_points):
            angle = 2 * np.pi * i / num_circle_points
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            z = 0
            circle_points.append([x, y, z])
        
        circle_points = np.array(circle_points)
        circle_points = circle_points @ np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # Rotaciona
        circle_points += point  # Translada o ponto da curva
        
        ax.plot(circle_points[:, 0], circle_points[:, 1], circle_points[:, 2], color='b')
    
    ax.plot(curve_points[:, 0], curve_points[:, 1], curve_points[:, 2], color='r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# pontos e tangentes 
P1 = np.array([0, 0, 0])
P2 = np.array([1, 1, 1])
T1 = np.array([1, 0, 0])
T2 = np.array([0, 1, 0])
radius = 0.1

plot_cano(P1, P2, T1, T2, radius)
