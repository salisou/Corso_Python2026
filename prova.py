from tkinter import filedialog, messagebox

def salva_grafico(fig):
    """Apre dialog per salvare il grafico in vari formati"""
    percorso = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG Image",     "*.png"),
            ("PDF Document",  "*.pdf"),
            ("SVG Vector",    "*.svg"),
            ("JPEG Image",    "*.jpg *.jpeg"),
            ("All Files",     "*.*")
        ],
        initialfile="grafico",
        title="Salva Grafico"
    )
    
    if percorso:
        try:
            fig.savefig(
                percorso,
                dpi=300,                  # alta risoluzione
                bbox_inches="tight",       # taglia bordi bianchi
                facecolor=fig.get_facecolor(),
                edgecolor='none',
                transparent=False
            )
            messagebox.showinfo(
                "Successo", 
                f"✅ Grafico salvato con successo:\n{percorso}"
            )
        except Exception as e:
            messagebox.showerror("Errore", f"❌ Errore nel salvataggio:\n{str(e)}")

# Esempio di uso in una GUI
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Salva Grafico")

fig = Figure(figsize=(8, 5), dpi=100)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], 'o-', linewidth=2)
ax.set_title('Esempio Grafico', fontsize=14, fontweight='bold')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Bottone salva
tk.Button(root, text="💾 Salva Grafico",
         command=lambda: salva_grafico(fig),
         bg='#3b82f6', fg='white',
         font=('Arial', 12, 'bold'),
         padx=25, pady=10,
         relief='flat').pack(pady=15)

root.mainloop()