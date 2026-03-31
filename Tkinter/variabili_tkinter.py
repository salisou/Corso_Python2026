import tkinter as tk

root = tk.Tk()

root.title("APP_Variabili")
root.geometry("300x200")
root.configure(bg="#aad2f9")

tk.Label(
    root,
    text="yoooooo",
    bg="#aad2f9",
    font=("Roboto", 20, "bold")
    
).pack(pady=(15,5))

# StringVar collegata all'Entry
nome_var = tk.StringVar()


entry = tk.Entry(root, textvariable=nome_var, font=("Arial", 16))
entry.pack(pady=10)

# Label che mostra il valore automaticamente
lbl = tk.Label(root, textvariable=nome_var, fg="#2563eb", bg="#ffffef", font=("Arial", 16))
lbl.pack()

#Variabili
nome_var = tk.StringVar()
cognome_var = tk.StringVar()

# Modificare la variabile da codice
def imposta():
    nome_var.set("Mario Rossi")  # aggiorna entry e label!

def leggi():
    print(nome_var.get())         # legge il valore


tk.Button(root, text="Imposta", command=imposta).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(root, text="Leggi",   command=leggi).pack(side=tk.LEFT, padx=10, pady=10)


root.mainloop()