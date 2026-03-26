import tkinter as tk

root = tk.Tk()

root.title("Gestione Corso")

root.geometry("600x350")

lable = tk.Label(
    root,
    text="Ciao Moussa!👋",
    font=("roboto", 20, "italic"),
    foreground="#9C9A9A",
    background="#EFF6FF"
)

lable.pack(padx=50)

root.mainloop()
