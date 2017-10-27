# arquivo da view do programa para criar a visualizacao do sistema em si


from tkinter import *
from sourceCode.view.Interface import Interface
from sourceCode.view.Graphics import Application

interface = Interface()
interface.mainLoop()

root = Tk()
Application(root)
root.mainloop()

interface.getController().registrarLucro()
