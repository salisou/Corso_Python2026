import tkinter as tk

class Text_widget:
    def __init__(self, master):
        self.master = master
        master.title("Esempio Text Tkinter")

        # Crea il Text
        self.txt = tk.Text(master, width=40, height=8, font=("Consolas", 12))
        self.txt.pack(padx=10, pady=10)

        # Inserisci testo iniziale
        self.txt.insert(tk.END, "Prima riga\nSeconda riga\n")

        # Bottone per leggere tutto il contenuto
        self.btn_leggi = tk.Button(master, text="Leggi contenuto", command=self.leggi_contenuto)
        self.btn_leggi.pack(pady=5)

        # Bottone per cancellare tutto
        self.btn_cancella = tk.Button(master, text="Cancella tutto", command=self.cancella_testo)
        self.btn_cancella.pack(pady=5)

        # Bottone per rendere il Text di sola lettura
        self.btn_readonly = tk.Button(master, text="Sola lettura", command=self.sola_lettura)
        self.btn_readonly.pack(pady=5)

    def leggi_contenuto(self):
        contenuto = self.txt.get("1.0", tk.END)
        print("Contenuto completo:")
        print(contenuto)

        # Leggi una riga specifica (riga 2)
        riga2 = self.txt.get("2.0", "2.end")
        print("Riga 2:")
        print(riga2)

    def cancella_testo(self):
        self.txt.delete("1.0", tk.END)

    def sola_lettura(self):
        self.txt.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = Text_widget(root)
    root.mainloop()