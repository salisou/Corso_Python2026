import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Finestra principale
root = tk.Tk()
root.title("Matplotlib in Tkinter")
root.geometry("900x600")

# Crea figura Matplotlib (non usare plt.figure)
fig = Figure(
    figsize=(8, 5),         # larghezza x altezza in pollici
    dpi=100,                # risoluzione
    facecolor='white'      # colore sfondo
)

# Aggiungi subplot (area per grafico)
ax = fig.add_subplot(111)  # 1 riga, 1 colonna, grafico #1

# Incorpora la figura in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()