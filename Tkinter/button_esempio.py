import tkinter as tk

# Metodo che saluta
def saluta():
     print("Ciao Come stai?")

root = tk.Tk()

# Dimenzione dell'applicazione 
root.geometry("350x250")

# Definizione del bottone 
btn = tk.Button(
    root,
    text="Clicca qui!",
    command=saluta,
    foreground="#E5DAF7",
    background="#B095F5",
    font=("Arial", 13),
    border=20,
    borderwidth=5,
    padx=20,
    pady=8,
    relief="raised",
    cursor="hand2"
)

# Padding del bottone
btn.pack(pady=60)

root.mainloop()