import numpy as np
import plotly.graph_objects as go


def create_cylinder(radius, height, num_points=20):
    # Cria os pontos para a base e o topo do cilindro
    theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z_base = np.zeros(num_points)  # Base no plano z=0
    z_top = np.full(num_points, height)  # Topo no plano z=height

    base_circle = np.column_stack((x, y, z_base))
    top_circle = np.column_stack((x, y, z_top))

    return base_circle, top_circle


def plot_solid_cylinder(fig, radius, height, num_points):
    base_circle, top_circle = create_cylinder(radius, height, num_points=num_points)

    # Adiciona as curvas da base e do topo
    fig.add_trace(go.Scatter3d(
        x=base_circle[:, 0],
        y=base_circle[:, 1],
        z=base_circle[:, 2],
        mode='lines',
        line=dict(color='blue')
    ))
    fig.add_trace(go.Scatter3d(
        x=top_circle[:, 0],
        y=top_circle[:, 1],
        z=top_circle[:, 2],
        mode='lines',
        line=dict(color='blue')
    ))

    # Conecta as bordas da base e do topo
    for i in range(num_points):
        fig.add_trace(go.Scatter3d(
            x=[base_circle[i, 0], top_circle[i, 0]],
            y=[base_circle[i, 1], top_circle[i, 1]],
            z=[base_circle[i, 2], top_circle[i, 2]],
            mode='lines',
            line=dict(color='blue')
        ))

    # Conecta os pontos da base entre si para formar linhas horizontais
    for i in range(num_points):
        x_line = [base_circle[i, 0], base_circle[(i + 1) % num_points, 0]]
        y_line = [base_circle[i, 1], base_circle[(i + 1) % num_points, 1]]
        z_line = [base_circle[i, 2], base_circle[(i + 1) % num_points, 2]]
        fig.add_trace(go.Scatter3d(
            x=x_line,
            y=y_line,
            z=z_line,
            mode='lines',
            line=dict(color='blue')
        ))

    # Conecta os pontos do topo entre si para formar linhas horizontais
    for i in range(num_points):
        x_line = [top_circle[i, 0], top_circle[(i + 1) % num_points, 0]]
        y_line = [top_circle[i, 1], top_circle[(i + 1) % num_points, 1]]
        z_line = [top_circle[i, 2], top_circle[(i + 1) % num_points, 2]]
        fig.add_trace(go.Scatter3d(
            x=x_line,
            y=y_line,
            z=z_line,
            mode='lines',
            line=dict(color='blue')
        ))

    # Adiciona arestas conectando todos os pontos da base
    for i in range(num_points):
        # Ponto central da base
        central_point = i
        # Ponto diametralmente oposto
        opposite_point = (i + num_points // 2) % num_points
        # Pontos adjacentes
        left_point = (i - 1) % num_points
        right_point = (i + 1) % num_points

        # Conecta o ponto central ao ponto diametralmente oposto
        fig.add_trace(go.Scatter3d(
            x=[base_circle[central_point, 0], base_circle[opposite_point, 0]],
            y=[base_circle[central_point, 1], base_circle[opposite_point, 1]],
            z=[base_circle[central_point, 2], base_circle[opposite_point, 2]],
            mode='lines',
            line=dict(color='blue')
        ))



# Exemplo de uso
fig = go.Figure()
plot_solid_cylinder(fig, radius=5, height=10, num_points=20)
fig.show()
