from tkinter import *
import dictlol as d


def open_details(name, index):
	detail = Tk()
	detail.title(name)
	detail.resizable(False, False)
	detail.iconbitmap(d.champico[index])

	filebg_det = PhotoImage(file = r'detback.png')
	w_det = filebg_det.width()
	h_det = filebg_det.height()

	detail.geometry("%dx%d+50+30" % (w_det,h_det)) #JANELA

	canvas_det = Canvas(height = h_det, width = w_det)
	canvas_det.pack(side='top', fill='both', expand='yes')
	canvas_det.create_image(0, 0, image=filebg_det, anchor='nw')

	detail.mainloop()