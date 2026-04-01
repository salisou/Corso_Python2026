import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.title("Line Plot - Temperatura Mensile")
root.geometry("1000x700")
root.configure(bg="#f5f5f5")

# Dati esempio: temperatura media mensile
mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 
        'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
temp_2023 = [5, 7, 12, 15, 20, 25, 28, 27, 22, 16, 10, 6]
temp_2024 = [4, 6, 11, 16, 21, 26, 30, 29, 24, 17, 11, 7]
temp_2026 = [0, 35, -8, 23, 17, -12, 27, 31, 30, 22, 18, 12]


# Crea figura
fig = Figure(figsize=(10, 6), dpi=100)
ax = fig.add_subplot(111)

# Plot di due linee con stili diversi
ax.plot(mesi, temp_2023, 
         marker='o',            # marcatori cerchio
         linestyle='-',          # linea continua
         linewidth=2.5,         # spessore linea
         color="#0ef6a5",       # verde acqua
         label='2023',
         markersize=8)

ax.plot(mesi, temp_2024,
         marker='s',            # marcatori quadrati
         linestyle='--',         # linea tratteggiata
         linewidth=2.5,
         color='#ef4444',       # rosso
         label='2024',
         markersize=8)

ax.plot(mesi, temp_2026,
         marker='^',            # marcatori triangolo
         linestyle='-.',         # linea tratteggiata-punto
         linewidth=2.5,
         color='#3b82f6',       # blu
         label='2026',
         markersize=8)

# Personalizzazione grafico
ax.set_title('Temperatura Media Mensile', 
              fontsize=18, 
              fontweight='bold',
              pad=20)
ax.set_xlabel('Mese', fontsize=14, fontweight='bold')
ax.set_ylabel('Temperatura (°C)', fontsize=14, fontweight='bold')
ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle='--')

# Migliora l'aspetto
fig.tight_layout()

# Incorpora in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()