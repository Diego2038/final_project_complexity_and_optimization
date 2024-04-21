import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_head_map(parent, production, delivered):
    """
    Function to create a button where it is clicked, appear a head map of the table
    """
    # Función para abrir la ventana emergente con los mapas de calor
    def show_heatmap():
        heatmap_window = tk.Toplevel()
        heatmap_window.title("Heatmap")

        # Obtener los valores máximos y mínimos para cada conjunto de datos
        vmin1, vmax1 = min(map(min, production)), max(map(max, production))
        vmin2, vmax2 = min(map(min, delivered)), max(map(max, delivered))

        # Crear los gráficos de mapa de calor
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        im1 = axes[0].imshow(production, cmap='viridis', aspect='auto', vmin=vmin1, vmax=vmax1)
        im2 = axes[1].imshow(delivered, cmap='plasma', aspect='auto', vmin=vmin2, vmax=vmax2)
        
        # Configurar las etiquetas de los ejes x e y
        axes[0].set_xlabel('Days')
        axes[0].set_ylabel('Plants')
        axes[1].set_xlabel('Days')
        axes[1].set_ylabel('Customers')

        

        # Añadir colorbars
        axes[0].set_title('Power plant production')
        axes[1].set_title('Quantity delivered to customers')
        fig.colorbar(im1, ax=axes[0], orientation='vertical', label='Megawatts')
        fig.colorbar(im2, ax=axes[1], orientation='vertical', label='Megawatts')

        # Crear el lienzo de Matplotlib para Tkinter
        canvas = FigureCanvasTkAgg(fig, master=heatmap_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Botón para abrir la ventana emergente con los mapas de calor
    heatmap_button = tk.Button(parent, text="Show Heatmaps", command=show_heatmap)
    return heatmap_button

