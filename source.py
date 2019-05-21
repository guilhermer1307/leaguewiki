from tkinter import *
import dictlol as d

def open_details(name, index):
	detail = Tk()
	detail.title(name)
	detail.resizable(False, False)
	detail.iconbitmap(d.champico[index])

	filebg = PhotoImage(file = 'paper.png', master = detail)
	w = filebg.width()
	h = filebg.height()

	detail.geometry("%dx%d+50+30" % (w,h)) #JANELA

	canvas = Canvas(detail, bg = 'white', height = h, width = w)
	canvas.pack(side='top', fill='both', expand='yes')
	canvas.create_image(0, 0, image=filebg, anchor='nw')

	canvas.create_text(50, 50, fill="black", font="arial 30", text=name)
	detail.mainloop()