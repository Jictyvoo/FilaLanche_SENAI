from tkinter import *
from tkinter import font as tkfont

class FazerPedido():

    def __init__(self,master=None):
        self.title_font = tkfont.Font(family='Comic Sans', size=18, weight="bold", slant="italic")
        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1["padx"] = 20
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["pady"] = 20
        self.container2["padx"] = 20
        self.boxvalue = 
        self.titulo = Label(self.container1,text="Faça o seu pedido aqui!")
        self.titulo.pack()

    def combobox(self):
        self.boxvalue =
root = Tk()
FazerPedido(root)
root.mainloop()

