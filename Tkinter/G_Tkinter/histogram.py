import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# -----------------------------
# Configurazione finestra Tkinter
# -----------------------------
root = tk.Tk()
root.title("Istogramma - Distribuzione Età Utenti")  # titolo finestra
root.geometry("1000x700")                            # dimensioni finestra
root.configure(bg="#1e1e2f")                       # colore sfondo della finestra

# -----------------------------
# Generazione dati di esempio
# -----------------------------
np.random.seed(42)  # per riproducibilitdà dei dati

# Genera età utenti secondo distribuzione normale con media=35 e dev. std=12
eta_utenti = np.random.normal(loc=35, scale=12, size=1000)

# Limita le età tra 18 e 70 anni
eta_utenti = np.clip(eta_utenti, 18, 70)

# -----------------------------
# Creazione figura Matplotlib
# -----------------------------
# figsize = dimensioni, dpi = risoluzione, facecolor = colore sfondo figura
fig = Figure(figsize=(10, 6), dpi=100, facecolor="#1e1e2f")  

# aggiunge un subplot all'interno della figura, con sfondo scuro per l'area grafico
ax = fig.add_subplot(111, facecolor="#2a2a3d")  

# -----------------------------
# Creazione istogramma
# -----------------------------
# bins = numero di barre, alpha = trasparenza, linewidth = spessore bordo a barra
n, bins, patches = ax.hist(
    eta_utenti,
    bins=30,
    color='#8b5cf6',      # colore barra
    edgecolor='#6d28d9',  # colore bordo barra
    alpha=0.8,
    linewidth=1.5
)

# -----------------------------
# Linea della media
# -----------------------------
media = np.mean(eta_utenti)  # calcola la media delle età
ax.axvline(media, color='#ef4444', linestyle='--', linewidth=2.5,
           label=f'Media: {media:.1f} anni')  # linea verticale per la media

# -----------------------------
# Linee deviazione standard
# -----------------------------
std_dev = np.std(eta_utenti)  # calcola la deviazione standard
# Linea +1 std
ax.axvline(media + std_dev, color='#facc15', linestyle=':', linewidth=2,
           label=f'+1 Std: {media + std_dev:.1f}')
# Linea -1 std
ax.axvline(media - std_dev, color='#facc15', linestyle=':', linewidth=2,
           label=f'-1 Std: {media - std_dev:.1f}')

# -----------------------------
# Personalizzazione grafico moderno
# -----------------------------
ax.set_title('Distribuzione Età Utenti', fontsize=20, fontweight='bold', pad=20, color='white')

ax.set_xlabel('Età (anni)', fontsize=14, fontweight='bold', color='white')

ax.set_ylabel('Frequenza', fontsize=14, fontweight='bold', color='white')

ax.tick_params(colors='white')  # colori dei numeri assi

# Legenda con sfondo scuro
ax.legend(fontsize=12, facecolor="#2a2a3d", edgecolor="white")

# Griglia tratteggiata bianca trasparente
ax.grid(alpha=0.3, linestyle='--', color='white')

# -----------------------------
# Statistiche aggiuntive con descrizione
# -----------------------------
# Mostra informazioni e descrizione all'interno del grafico
stats_text = (f'Questo grafico mostra la distribuzione delle età di 1000 utenti.\n'
              f'N = {len(eta_utenti)}\nMedia = {media:.1f}\nDeviazione Std = {std_dev:.1f}')

ax.text(0.02, 0.95, stats_text,
        transform=ax.transAxes,  # posizione relativa all'area grafico
        fontsize=11,
        verticalalignment='top',
        color='white',
        bbox=dict(boxstyle='round', facecolor='#3a3a5c', alpha=0.8))  # box sfondo

# Ottimizza layout
fig.tight_layout()

# -----------------------------
# Incorpora grafico in Tkinter
# -----------------------------
canvas = FigureCanvasTkAgg(fig, master=root)  # crea canvas Tkinter per matplotlib
canvas.draw()                                 # disegna il grafico
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # mostra il canvas

# Avvia finestra Tkinter
root.mainloop()