"""
Ordine di pack() (IMPORTANTISSIMO)

pack() lavora in sequenza, quindi l’ordine in cui aggiungi i widget cambia completamente il risultato.

Nel tuo caso:
    "In alto" => occupa tutta la riga sopra (side="top", fill="x")
    "In Basso" => occupa tutta la riga sotto (side="bottom", fill="x", pady=5)
    "Sinistra" => si attacca a sinistra
    "Destra" => si attacca a destra
    "Centro" => prende tutto lo spazio rimasto (expand=True)
    ___________________________________________________________________________
    
    Significato dei parametri
        side
            "top" => dall’alto verso il basso
            "left" => da sinistra verso destra
            "bottom" ----|Vale anche per questo|---
        filll
            "x" => si allarga orizzontalmente
            "y" => si allarga verticalmente
            "both" => entrambe
        expand=True
            il widget occupa lo spazio extra disponibile
"""
# Dimenzione della form
import tkinter as tk

root = tk.Tk()
root.title("Esempio Layout con Pack")

root.geometry("600x350")

# Background finestra
root.configure(bg="#1e293b")

# Titolo
titolo = tk.Label(
    root,
    text="Layout con Pack",
    font=("Arial", 16, "bold"),
    bg="#1e293b",
    fg="white"
)
titolo.pack(pady=(10, 5))

# Descrizione
descrizione = tk.Label(
    root,
    text="Esempio di utilizzo di side, fill ed expand",
    font=("Arial", 11),
    bg="#1e293b",
    fg="#cbd5f5"
)
descrizione.pack(pady=(0, 10))

color1 = "#fca5a5"
color2 = "#f87171"

# Label in alto (top)
tk.Button(root, text="In alto", bg=color1).pack(side="top", fill="x", pady=5)

# Label in basso (footer)
tk.Button(root, text="In basso", bg=color2).pack(side="bottom", fill="x", pady=5)

# Sinistra (left) e destra (right)
tk.Label(root, text="Sinistra", bg="#86efac").pack(side="left", fill="y", padx=5)
tk.Label(root, text="Destra", bg="#93c5fd").pack(side="right", fill="y", padx=5)

# Centro (expend=true)
tk.Label(root, text="Ciao Developers", bg="#76ea64").pack(expand=True, fill="both")

root.mainloop()
