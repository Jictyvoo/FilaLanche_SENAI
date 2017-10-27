from tkinter import *
from tkinter import font as tkfont
from sourceCode.controller.MainController import MainController
from tkinter import Tk,ttk

class FazerPedido():
    nomes = []
    pedidos = []
    controller = MainController()
    controller.carregarProdutosEmEstoque();
    pedidos = controller.getitens()


    def __init__(self,Master=None):
        for nnomes in self.pedidos:
            self.nomes.append(nnomes.getNome())
        self.ventana = Tk()

        self.combo = ttk.Combobox(self.ventana)
        self.combo.place(x=50,y=100)
        self.combo['values'] = self.nomes
        self.ventana.geometry("300x300")
        self.ventana.mainloop()

root = Tk()
FazerPedido(root)
root.mainloop()



