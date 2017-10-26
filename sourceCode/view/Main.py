# arquivo da view do programa para criar a visualizacao do sistema em si
from tkinter import *
from sourceCode.controller.MainController import MainController;
from sourceCode.view.Graphics import Application;

controller = MainController();

root = Tk()
Application(root)
root.mainloop()
