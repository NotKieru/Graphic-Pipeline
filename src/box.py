import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Parâmetros 
lado = 10
altura = 15
espessura = 1

# Teste de vertices da caixa
v0 = [0, 0, 0]
v1 = [lado, 0, 0]
v2 = [lado, lado, 0]
v3 = [0, lado, 0]
v4 = [0, 0, altura]
v5 = [lado, 0, altura]
v6 = [lado, lado, altura]
v7 = [0, lado, altura]

#  vértices da caixa sem a face superior CORRIGIR depois, a face inferior é que está sendo retirada, pq? não sei, 
vertices = np.array([v0, v1, v2, v3, v4, v5, v6, v7])

# Lista as faces (sem a face superior) 
faces = [
    [v0, v1, v5, v4],  # Face inferior
    [v1, v2, v6, v5],  # Face lateral
    [v2, v3, v7, v6],  # Face lateral
    [v3, v0, v4, v7],  # Face lateral
    [v4, v5, v6, v7]   # Face lateral
]

# figura e o eixo 3D - TO DO colocar pro grid estar fora da caixa.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adiciona as faces à plotagem
poly3d = Poly3DCollection(faces, alpha=.25, linewidths=1, edgecolors='r', facecolors='gray')
ax.add_collection3d(poly3d)

# Define os limites dos eixos
ax.set_xlim([0, lado])
ax.set_ylim([0, lado])
ax.set_zlim([altura, 0])

# Define os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('LA Caixa de Papel')

plt.show()
