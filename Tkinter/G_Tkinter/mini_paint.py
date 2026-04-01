import tkinter as tk

root = tk.Tk()
root.title("Mini Paint")

colore_attuale = ["#7c6af7"]
spessore = [4]
prev_x = prev_y = [None]

canvas = tk.Canvas(root, width=600, height=400, bg="white", cursor="crosshair")
canvas.pack()

def disegna(event):
    if prev_x[0] is not None:
        canvas.create_line(
            prev_x[0], prev_y[0], event.x, event.y,
            fill=colore_attuale[0], width=spessore[0],
            capstyle=tk.ROUND, smooth=True
        )
    prev_x[0], prev_y[0] = event.x, event.y

def reset_prev(event):
    prev_x[0] = prev_y[0] = None

canvas.bind("<B1-Motion>", disegna)
canvas.bind("<ButtonRelease-1>", reset_prev)

# Barra strumenti colori
barra = tk.Frame(root, bg="#f0f0f0")
barra.pack(fill="x")

colori = ["#7c6af7", "#f38ba8", "#a6e3a1", "#f7a26a", "black", "white"]
for c in colori:
    tk.Button(barra, bg=c, width=3,
             command=lambda x=c: colore_attuale.__setitem__(0, x)).pack(side="left", padx=2, pady=4)

tk.Button(barra, text="🗑 Pulisci",
         command=lambda: canvas.delete("all")).pack(side="right", padx=8)

root.mainloop()