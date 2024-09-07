import numpy as np
import plotly.graph_objects as go


# Matriz de controle da curva de Hermite
def hermite_matrix(p0, p1, m0, m1):
    return np.array([
        [2, -2, 1, 1],
        [-3, 3, -2, -1],
        [0, 0, 1, 0],
        [1, 0, 0, 0]
    ])


# Curva de Hermite
def hermite_curve(p0, p1, m0, m1, t):
    H = hermite_matrix(p0, p1, m0, m1)
    T = np.array([t ** 3, t ** 2, t, 1])
    return np.dot(T, np.dot(H, np.vstack([p0, p1, m0, m1])))


# Função para gerar as coordenadas das circunferências e interligá-las
def generate_torus_edges(r, R, n=30, phi_range=(0, np.pi)):
    theta = np.linspace(0, 2 * np.pi, n)
    phi = np.linspace(phi_range[0], phi_range[1], n)
    theta, phi = np.meshgrid(theta, phi)

    # Listas para armazenar as coordenadas das circunferências e das arestas
    circles = []
    edges = []

    # Gera as circunferências do toróide
    for i in range(len(phi)):
        x = (R + r * np.cos(theta[i, :])) * np.cos(phi[i])
        y = (R + r * np.cos(theta[i, :])) * np.sin(phi[i])
        z = r * np.sin(theta[i, :])
        circles.append((x, y, z))

    # Adiciona as arestas entre circunferências
    for i in range(len(phi)):
        for j in range(len(theta[0])):
            # Pontos nas circunferências
            p0 = np.array([circles[i][0][j], circles[i][1][j], circles[i][2][j]])
            p1 = np.array([circles[(i + 1) % len(phi)][0][j], circles[(i + 1) % len(phi)][1][j], circles[(i + 1) % len(phi)][2][j]])
            m0 = m1 = np.array([0, 0, 0])  # Vetores tangenciais (simplificados para arestas)

            # Curva de Hermite para as arestas
            t = np.linspace(0, 1, 2)
            curve = np.array([hermite_curve(p0, p1, m0, m1, ti) for ti in t])
            edges.append(curve)

            # Adiciona as arestas entre pontos adjacentes na mesma circunferência
            p0 = np.array([circles[i][0][j], circles[i][1][j], circles[i][2][j]])
            p1 = np.array([circles[i][0][(j + 1) % len(theta[0])], circles[i][1][(j + 1) % len(theta[0])], circles[i][2][(j + 1) % len(theta[0])]])
            curve = np.array([hermite_curve(p0, p1, m0, m1, ti) for ti in t])
            edges.append(curve)

    return edges


# Parâmetros do toróide
R = 1  # Raio maior
r = 0.3  # Raio menor

# Gera as arestas do toróide com um corte no meio
edges = generate_torus_edges(r, R, phi_range=(0, np.pi))

# Criação do gráfico com Plotly
fig = go.Figure()

# Adiciona as arestas ao gráfico
for edge in edges:
    fig.add_trace(
        go.Scatter3d(x=edge[:, 0], y=edge[:, 1], z=edge[:, 2], mode='lines', line=dict(width=2, color='blue'))
    )

# Configurações do layout
fig.update_layout(
    title='Toroide Cortado Horizontal com Curvas de Hermite',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        zaxis=dict(range=[-1.5, 1.5])
    ),
    autosize=False,
    width=800,
    height=800
)

# Exibe o gráfico
fig.show()
