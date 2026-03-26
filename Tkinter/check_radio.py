import tkinter as tk

root = tk.Tk()

# Titolo 
root.title("Selezione Linguaggi")

# lable con la descrizione 
tk.Label(
    root,
    text="Seleziona un linguaggio e accetta i termini",
    fg="white",
    bg="black",
    font=("Arial", 12)
).pack(pady=10)

# Dimenzione della form (400x350)
root.geometry("400x350")

# bg = black
root.configure(bg="black")

# Chekbutton - variabile collegata al BooleanVar (boolean tipo variabile)
scelta = tk.BooleanVar()
valoreScelta = tk.Checkbutton(
    root,
    text="Accetto i termini",
    variable=scelta,
    fg="white",
    bg="black",
    selectcolor="black"
) 
valoreScelta.pack()


# Creare una lista dei liguaggi 

linguaggi = [
    ("Python", "python"),
    ("Java", "java"),
    ("C#", "csharp"),
    ("R", "r"),
    ("Delphi", "delphi"),
    ("C++", "cpp"),
    ("F#", "f#"),
    ("JavaScript", "js"),
    ("PHP", "php"),
    ("Pascal", "pascal")
]

# Rodiobutton - variabile collegata StringVar
mia_variabile_radio = tk.StringVar(value="Python")

# tk.Radiobutton(root, text="Python", variable=mia_variabile_radio, value="python").pack()
# tk.Radiobutton(root, text="Java", variable=mia_variabile_radio, value="java").pack()
# tk.Radiobutton(root, text="C#", variable=mia_variabile_radio, value="c#").pack()
# tk.Radiobutton(root, text="R", variable=mia_variabile_radio, value="r").pack()
# tk.Radiobutton(root, text="Delphi", variable=mia_variabile_radio, value="delphi").pack()
# tk.Radiobutton(root, text="C++", variable=mia_variabile_radio, value="cpp").pack()
# tk.Radiobutton(root, text="F#", variable=mia_variabile_radio, value="f#").pack()
# tk.Radiobutton(root, text="JavaScrit", variable=mia_variabile_radio, value="js").pack()
# tk.Radiobutton(root, text="Php", variable=mia_variabile_radio, value="php").pack()
# tk.Radiobutton(root, text="Pascal", variable=mia_variabile_radio, value="pascal").pack()


# fare il ciclo for per recuperare i liguaggi 
for nome, valore in linguaggi:
    tk.Radiobutton(
        root,
        text=nome,
        variable=mia_variabile_radio,
        value=valore,
        fg="white",
        bg="black",
        selectcolor="black"
    ).pack(anchor="w")

# Funzione
def mostra():
    print("Linguaggio:", mia_variabile_radio.get())
    print("Accettato:", scelta.get())
    

tk.Button(
    root,
    text="Mostra selezione ➡️",
    command=mostra,
    background="#4CAF50",
    foreground="white"
).pack()

root.mainloop()
