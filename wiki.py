from tkinter import *
from tkinter import messagebox
import dictlol as d
import source as s

##Variaveis
cpimg = []

##JANELA
root = Tk()
root.title('League Wiki')
root.resizable(False, False)

##FUNDO 
filebg = PhotoImage(file = "background1.png")
w = filebg.width()
h = filebg.height()
root.geometry("%dx%d+50+30" % (w,h)) #JANELA

canvas = Canvas(height = h, width = w)
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, image=filebg, anchor='nw')



##ARRAY IMAGENS
for x in range(len(d.champimage)):
       imgtemp = PhotoImage(file = d.champimage[x])
       cpimg.append(imgtemp)

##DRAW BUTTONS
for x in range(7):
       bt = Button(canvas, image = cpimg[x], width = 118, height = 118, bd = 0, highlightthicknes=0, command=s.open_details)
       bt.grid(row = 0, column = x, padx=13, pady=18)

for x in range(4):
       if x < 2:
              bt = Button(canvas, image = cpimg[x+7], width = 118, height = 118, bd = 0, highlightthicknes=0, command=s.open_details)
              bt.grid(row = 1, column = x, padx=13, pady=10)
       else:
              bt = Button(canvas, image = cpimg[x+7], width = 118, height = 118, bd = 0, highlightthicknes=0, command=s.open_details)
              bt.grid(row = 1, column = x+3, padx=13, pady=10)

for x in range(4):
       if x < 2:
              bt = Button(canvas, image = cpimg[x+11], width = 118, height = 118, bd = 0, highlightthicknes=0, command=s.open_details)
              bt.grid(row = 2, column = x, padx=13, pady=10)
       else:
              bt = Button(canvas, image = cpimg[x+11], width = 118, height = 118, bd = 0, highlightthicknes=0, command=s.open_details)
              bt.grid(row = 2, column = x+3, padx=13, pady=10)

for x in range(7):
       bt = Button(canvas, image = cpimg[x+15], width = 118, height = 118, bd = 0, highlightthicknes=0, command=s.open_details)
       bt.grid(row = 3, column = x, padx=13, pady=10)


##MAIN
root.mainloop()