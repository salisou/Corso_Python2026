import tkinter as tk

root = tk.Tk()

# Titolo finestra
root.title("Entry Forms")

# Dimensione
root.geometry("350x250")

# Colore sfondo
root.configure(bg="#6392a7") 

# Creazione Entry
entry = tk.Entry(
    root,
    width=30,
    font=("Roboto", 14)
)

entry.insert(0, "Inserisci qualcosa...")
entry.pack(pady=20)  # 👈 IMPORTANTISSIMO 

# Metodo che legge i valori
def leggi_testo():
    testo = entry.get()
    print(f"Hai scritto: {testo}")

# Cancella tutto
def svuota_entry():
    entry.delete(0, tk.END)

# Bottoni
tk.Button(root, text="Leggi", command=leggi_testo).pack(pady=10)
tk.Button(root, text="Svuota", command=svuota_entry).pack(pady=10)

# Avvio app
root.mainloop()