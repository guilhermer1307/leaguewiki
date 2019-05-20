from tkinter import *
import dictlol as d

def open_details(name, index):
	detail = Tk()
	detail.title(name)

	filebg = PhotoImage(file = "paper.png")
    w = filebg.width()
    h = filebg.height()
    root.geometry("%dx%d+50+30" % (w,h)) #JANELA

	canvas = Canvas(height = h, width = w)
	canvas.pack(side='top', fill='both', expand='yes')
	canvas.create_image(0, 0, image=filebg, anchor='nw')

	detail.mainloop()