import tkinter as tk  # libreria per creare interfacce grafiche
from matplotlib.figure import Figure  # per creare il grafico
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # per integrare matplotlib in tkinter
import numpy as np  # libreria per calcoli numerici

# ---------------------------------------------------------
# Funzione che aggiorna il grafico quando muovi lo slider
# ---------------------------------------------------------
def update_hist(val):
    scale_factor = scale.get()  # prende il valore corrente dello slider

    # modifica i dati moltiplicandoli per il fattore dello slider
    eta_mod = eta_utenti * scale_factor

    # limita i valori tra 18 e 70 anni
    eta_mod = np.clip(eta_mod, 18, 70)

    ax.cla()  # cancella completamente il grafico precedente

    # -----------------------------
    # Creazione istogramma
    # -----------------------------
    counts, bins, patches = ax.hist(
        eta_mod,              # dati da visualizzare
        bins=30,              # numero di barre
        alpha=0.6,            # trasparenza
        edgecolor='white',    # colore bordo barre
        linewidth=0.5         # spessore bordo
    )

    # -----------------------------
    # Effetto gradiente sulle barre
    # -----------------------------
    for i, p in enumerate(patches):  # cicla tutte le barre
        color_intensity = i / len(patches)  # crea variazione colore
       
        # assegna colore RGBA (rosso, verde, blu, alpha)
        p.set_facecolor((0.2, 0.6, 1.0, 0.3 + 0.7 * color_intensity))

    # -----------------------------
    # Curva distribuzione (tipo gaussiana)
    # -----------------------------
    x = np.linspace(min(eta_mod), max(eta_mod), 200)  # crea asse X continuo
    mean = np.mean(eta_mod)  # calcola media
    std = np.std(eta_mod)    # calcola deviazione standard

    # formula distribuzione normale (gaussiana)
    y = (1/(std*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mean)/std)**2)

    # scala la curva per adattarla all’istogramma
    y = y * len(eta_mod) * (bins[1] - bins[0])

    # disegna la curva sopra l’istogramma
    ax.plot(x, y, color='#00f5d4', linewidth=2.5, label='Distribuzione')

    # -----------------------------
    # Linee statistiche
    # -----------------------------
    ax.axvline(mean, color='#ff4d6d', linestyle='--', linewidth=2,
               label=f'Media: {mean:.1f}')  # linea media

    ax.axvline(mean + std, color='#ffd166', linestyle=':', linewidth=2)  # +1 deviazione
    ax.axvline(mean - std, color='#ffd166', linestyle=':', linewidth=2)  # -1 deviazione

    # -----------------------------
    # Stile grafico moderno
    # -----------------------------
    ax.set_facecolor("#0f172a")  # sfondo area grafico
    fig.patch.set_facecolor("#0f172a")  # sfondo figura

    ax.set_title('Distribuzione Età Utenti', fontsize=18, color='white', pad=20)
    ax.set_xlabel('Età', color='white')
    ax.set_ylabel('Frequenza', color='white')

    ax.tick_params(colors='white')  # colore numeri assi

    ax.grid(alpha=0.2, linestyle='--', color='white')  # griglia

    # rimuove bordi classici
    for spine in ax.spines.values():
        spine.set_visible(False)

    # legenda
    ax.legend(facecolor="#0f172a", edgecolor="white", labelcolor='white')

    canvas.draw()  # aggiorna il grafico a schermo

# -----------------------------
# Creazione finestra principale
# -----------------------------
root = tk.Tk()  # crea finestra
root.title("Istogramma -  Distribuzione Età Utenti")  # titolo
root.geometry("1000x800")  # dimensioni
root.configure(bg="#0f172a")  # sfondo scuro

# -----------------------------
# Generazione dati
# -----------------------------
np.random.seed(42)  # per riproducibilitdà dei dati

# Genera età utenti secondo distribuzione normale con media=35 e dev. std=12
eta_utenti = np.random.normal(loc=35, scale=12, size=1000)

# limita i valori tra 18 e 70
eta_utenti = np.clip(eta_utenti, 18, 70)


# -----------------------------
# Creazione figura Matplotlib
# -----------------------------
# figsize = dimensioni, dpi = risoluzione, facecolor = colore sfondo figura
fig = Figure(figsize=(10, 6), dpi=100)  # crea figura

# aggiunge un subplot all'interno della figura, con sfondo scuro per l'area grafico
ax = fig.add_subplot(111)  # crea area grafico

# inserisce il grafico dentro Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# -----------------------------
# Slider interattivo
# -----------------------------
scale = tk.Scale(root,
                 from_=0.5, to=2.0,   # range valori
                 resolution=0.01,     # precisione
                 orient='horizontal', # orizzontale
                 length=400,          # lunghezza
                 label='Animazione',  # etichetta
                 bg="#0f172a",
                 fg="white",
                 troughcolor="#1e293b",
                 command=update_hist)  # funzione chiamata quando si muove

scale.set(1.0)  # valore iniziale
scale.pack(pady=20)  # posizionamento

# prima esecuzione del grafico
update_hist(1.0)

# avvia il programma
root.mainloop()