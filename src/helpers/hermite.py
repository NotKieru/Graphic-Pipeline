import numpy as np
def hermite(p0, t0, p1, t1, num_points=100):
    t = np.linspace(0, 1, num_points)
    h00 = 2 * t**3 - 3 * t**2 + 1
    h10 = t**3 - 2 * t**2 + t
    h01 = -2 * t**3 + 3 * t**2
    h11 = t**3 - t**2
    return (h00[:, None] * p0 + h10[:, None] * t0 +
            h01[:, None] * p1 + h11[:, None] * t1)
