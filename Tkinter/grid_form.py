import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Modulo Scolastico")
root.configure(bg="#e5e7eb")
root.geometry("700x300")

# Funzione placeholder
"""
    Questa funzione serve per creare un placeholder (testo di esempio dentro l’Entry).
    entry.insert(0, testo) inserisce il testo iniziale.
    entry.config(fg="gray") rende il testo grigio, così sembra un suggerimento.    
"""
def set_placeholder(entry, testo):
    entry.insert(0, testo)
    entry.config(fg="gray")

    """
    Quando l’utente clicca dentro il campo (FocusIn), 
    se il testo è ancora il placeholder, viene cancellato e il colore diventa nero.
    """
    def on_focus_in(event):
        if entry.get() == testo:
            entry.delete(0, tk.END)
            entry.config(fg="black")

        """
        Quando l’utente esce dal campo (FocusOut) 
        e non ha scritto nulla, il placeholder ritorna.
        """
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, testo)
            entry.config(fg="gray")


        """
        Collega le funzioni agli eventi della Entry.
        <FocusIn> = quando il cursore entra nel campo.
        <FocusOut> = quando il cursore esce dal campo.
        """ 
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Funzione campo
"""
    Crea una Label sopra l’Entry per descrivere il campo.
    grid posiziona il widget nella finestra usando righe e colonne.
    sticky="w" allinea a sinistra, padx e pady aggiungono spazio.
"""
def crea_campo(testo, placeholder, riga, colonna):
    label = tk.Label(root, text=testo, bg="#e5e7eb", font=("Arial", 11))
    label.grid(row=riga, column=colonna, sticky="w", padx=20, pady=(10, 2))

    """
    Crea il campo dove l’utente scriverà.
    relief="flat" fa un bordo piatto.
    ipady=8 aumenta l’altezza interna del campo.
    """
    entry = tk.Entry(
        root,
        font=("Arial", 12),
        bg="#cbd5e1",
        relief="flat",
        width=25
    )
    entry.grid(row=riga+1, column=colonna, padx=20, pady=(0, 10), ipady=8)

    """
    Imposta il placeholder con la funzione precedente.
    Ritorna l’Entry per poterlo usare dopo (ad esempio per leggere il valore).
    """
    set_placeholder(entry, placeholder)

    return entry

# Campi
    """
    Crea 4 campi: Nome, Cognome, Email, Data di nascita.
    Ogni campo ha una label e un Entry con placeholder.
    I campi sono disposti in griglia: 2 colonne, 2 righe.
    """
nome = crea_campo("Nome", "Inserisci il Nome", 0, 0)
cognome = crea_campo("Cognome", "Inserisci il Cognome", 0, 1)

email = crea_campo("Email", "Inserisci la mail", 2, 0)
data = crea_campo("Data di Nascita", "Inserisci la data di nascita", 2, 1)


def salva_dati():
    campi = [nome, cognome, email, data]
    valori = []
    
    for campo in campi:
        testo = campo.get()
        
        #Se il testo è il placeholder, vonsidera vuoto
        if campo.cget("fg") == "gray":
            testo = ""
        valori.append(testo)
        
        # Creazione del messaggio da mostrare 
        messaggio = (
            f"Nome: {valori[0]}\n",
            f"Cognome: {valori[1]}\n",
            f"Email: {valori[2]}\n",
            f"Data di nascita: {valori[3]}"
        )
        
        # Mostra il messaggio in Popup
        messagebox.showinfo("Dati inserti", messaggio)
    
# Bottone
"""
    Crea un pulsante con testo “Salva”.
    columnspan=2 fa sì che il pulsante occupi entrambe le colonne.
    Non ha ancora funzione associata, quindi al click non succede nulla.
"""
btn = tk.Button(
    root,
    text="Salva",
    bg="#94a3b8",
    font=("Arial", 11),
    command=salva_dati, #associa la funzione al clic
    width=20,
    height=2
)
btn.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="w")

root.mainloop()