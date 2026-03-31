import tkinter as tk
from tkinter import messagebox

# -----------------------
# Funzione che cambia colore
# -----------------------
def cambia_colore(label, colore):
    label.config(fg=colore)

# -----------------------
# Funzione che mostra popup
# -----------------------
def mostra_nome(nome):
    messagebox.showinfo("Nome selezionato", nome)

# -----------------------
# Finestra
# -----------------------
root = tk.Tk()
root.title("Esempio Lambda")
root.geometry("350x250")
root.configure(bg="#f1f5f9")

# -----------------------
# Label
# -----------------------
label = tk.Label(
    root,
    text="Cambia il mio colore!",
    font=("Arial", 14),
    bg="#f1f5f9"
)
label.pack(pady=20)

# -----------------------
# Bottoni colori (con lambda)
# -----------------------
tk.Button(root, text="Rosso",
          command=lambda: cambia_colore(label, "red")).pack(pady=5)

tk.Button(root, text="Verde",
          command=lambda: cambia_colore(label, "green")).pack(pady=5)

tk.Button(root, text="Blu",
          command=lambda: cambia_colore(label, "blue")).pack(pady=5)

# -----------------------
# Bottoni con parametri diversi
# -----------------------
tk.Button(root, text="Nome Mario",
          command=lambda: mostra_nome("Mario")).pack(pady=5)

tk.Button(root, text="Nome Luca",
          command=lambda: mostra_nome("Luca")).pack(pady=5)

root.mainloop()

