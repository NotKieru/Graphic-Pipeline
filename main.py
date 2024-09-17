from src.objects.mug import create_mug
import matplotlib.pyplot as plt

from src.objects.mug import create_mug
from src.world2D import *
from src.world3D import plot_image

octante = 3
def main():
    box_params = (5, 0.5)  # Parâmetros da caixa
    cone_params = (1, 0, 3)  # Parâmetros do cone
    cano_params = (np.array([1, 1, 1]), np.array([2, 2, 2]), np.array([2, 1, 1]), np.array([1, 2, 1]), 0.5)
    tronco_params = (1, 0.5, 2)  # Parâmetros do tronco do cone
    mug_params = create_mug(height=2, radius=1, num_points_mug=20, handle_radius=0.1, num_points_handle=35, num_points_handle_circle=20)

    octante # Defina o octante desejado (de 1 a 8)
    plot_image(octante, box_params=box_params, cone_params=cone_params, cano_params=cano_params, tronco_params=tronco_params, mug_params=mug_params)

if __name__ == "__main__":
    main()

def world2d(octant):
    plane = get_plane_for_octant(octant)
    xlim, ylim = get_plane_limits(octant)[:2], get_plane_limits(octant)[2:]

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')

    if plane in ['xy', 'yx']:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    elif plane in ['xz', 'zx']:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_xlabel('X')
        ax.set_ylabel('Z')
    elif plane in ['yz', 'zy']:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_xlabel('Y')
        ax.set_ylabel('Z')
    else:
        raise ValueError("Plano inválido. Use 'xy', 'xz', 'yx', 'yz', 'zx' ou 'zy'.")

    base_vectors = np.eye(3)
    box_params = (5, 0.5)
    cano_params = (np.array([1, 1, 1]), np.array([2, 2, 2]), np.array([2, 1, 1]), np.array([1, 2, 1]), 0.5)
    cone_params = (1, 0, 2)
    tronco_params = (2, 1, 2)
    mug_params = create_mug()

    plot_solid_box(ax, base_vectors, *box_params, plane=plane)
    plot_solid_cano(ax, base_vectors, *cano_params, plane=plane)
    plot_solid_cone(ax, base_vectors, *cone_params, plane=plane)
    plot_solid_tronco(ax, base_vectors, *tronco_params, plane=plane)
    plot_solid_mug(ax, base_vectors, mug_params, plane=plane)

    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    plt.title(f'Projeção 2D dos Sólidos no plano {plane.upper()}')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Escolha o octante desejado para visualização
    octant = 3  # ou qualquer valor de 1 a 8
    world2d(octant)