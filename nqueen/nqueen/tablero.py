import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def dibujar_tablero(reinas):
    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Dibujar el tablero
    for i in range(len(reinas)+1):
        for j in range(len(reinas)+1):
            ax.add_patch(patches.Rectangle((j, i), 1, 1, color='white'))

    for i,e in enumerate(reinas):
        # i == y , e == x
        ax.text(e + 0.5, i + 0.5, "Q", ha='center', va='center', fontsize=10)        
            
    # Configurar ejes y etiquetas
    ax.set_xticks(np.arange(0, len(reinas)+1))
    ax.set_yticks(np.arange(0, len(reinas)+1))
    ax.set_xticklabels([0,1,2,3,4])
    ax.set_yticklabels([0,1,2,3,4])
    ax.grid(which="both", linestyle='-', linewidth=2)
    plt.title(f"problema nqueen")
    plt.show()

