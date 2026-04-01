from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title("Corso Slider su python")
root.iconbitmap("Tkinter\icons\slider.ico") # imposta il percorso relativo all'ico

root.geometry('400x400')



# Slider verticale 
verticale = Scale(root, from_=0, to=200)
verticale.pack()


def slide():
    my_lable = Label(root, text=horisontale.get()).pack()
    root.geometry(str(text=horisontale.get()) + "x400")

horisontale = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horisontale.pack()

my_lable = Label(
    root, 
    text= horisontale.get()
).pack()

    
btnSalva = Button(root, text="Clicca qui!", command= slide).pack()

root.mainloop()