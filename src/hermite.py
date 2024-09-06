import numpy as np
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