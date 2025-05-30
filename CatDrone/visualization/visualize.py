# visualize.py
import matplotlib.pyplot as plt
import numpy as np

class Zone:
    def __init__(self, grid_size=100, dpi=100, pixel_size=8):
        self.grid_size = grid_size
        self.dpi = dpi
        self.pixel_size = pixel_size  # her hücrenin kaç piksel olacağı
        self.fig = None
        self.ax = None
        self.grid_data = np.zeros((grid_size, grid_size))  # veri matrisimiz
        self.im = None

        self.create_window()

    def create_window(self):
        size_in_inches = (self.grid_size * self.pixel_size) / self.dpi
        self.fig, self.ax = plt.subplots(figsize=(size_in_inches, size_in_inches), dpi=self.dpi)

        # Izgara çizimi
        self.im = self.ax.imshow(self.grid_data, cmap="Greys", vmin=0, vmax=1)

        # Grid çizgileri
        self.ax.set_xticks(np.arange(-0.5, self.grid_size, 1), minor=True)
        self.ax.set_yticks(np.arange(-0.5, self.grid_size, 1), minor=True)
        self.ax.grid(which="minor", color="darkgrey", linestyle='-', linewidth=0.5)

        self.ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
        
        plt.tight_layout()
        plt.show()

    # Daha sonra animasyon veya hücre güncelleme için kullanılabilir
    def update_cell(self, x, y, value):
        self.grid_data[y][x] = value
        self.im.set_data(self.grid_data)
        plt.draw()
