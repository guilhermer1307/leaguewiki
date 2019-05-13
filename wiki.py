from tkinter import *
from tkinter import messagebox

##Variaveis

##JANELA
root = Tk()
root.title('League Wiki')
root.resizable(False, False)

##FUNDO 
filebg = PhotoImage(file = "background.png")
w = filebg.width()
h = filebg.height()
root.geometry("%dx%d+50+30" % (w,h)) #JANELA

canvas = Canvas(height = h, width = w)
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, image=filebg, anchor='nw')

for x in range(4):
	bt = Button(canvas, width=20, text="Selecionar", fg="white", bg = "#004655")
	bt.pack(side = 'right', padx=10, pady=5, anchor ='sw')

root.mainloop()