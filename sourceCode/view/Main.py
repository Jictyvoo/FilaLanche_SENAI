# arquivo da view do programa para criar a visualizacao do sistema em si


from tkinter import *
<<<<<<< HEAD
from sourceCode.controller.MainController import MainController;
from sourceCode.view.Graphics import Application;

main = MainController()

class Main:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.c1 = Frame(master)
        self.c1["pady"] = 10
        self.c1.pack()

        self.c2 = Frame(master)
        self.c2["padx"] = 20
        self.c2.pack()

        self.c3 = Frame(master)
        self.c3["padx"] = 20
        self.c3.pack()

        self.c4 = Frame(master)
        self.c4["pady"] = 20
        self.c4.pack()

        self.titulo = Label(self.c1, text="Cantina SENAI")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.idAluno = Label(self.c2, text="      ID", font=self.fontePadrao)
        self.idAluno.pack(side=LEFT)

        self.turma = Entry(self.c2)
        self.turma["width"] = 30
        self.turma["font"] = self.fontePadrao
        self.turma.pack(side=LEFT)


        self.autenticar = Button(self.c4)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaAluno
        self.autenticar.pack()

        self.mensagem = Label(self.c4, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def verificaAluno(self):
        idAluno = self.turma.get()
        if idAluno == main.buscaEstudante(idAluno):
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


root = Tk()
Main(root)
root.mainloop()
=======
from sourceCode.view.Interface import Interface
import os
import datetime

interface = Interface()
while (interface.mainLoop()):
    os.system("cls")


# root = Tk()
# Application(root)
# root.mainloop()


def mensagem():
    currentTime = datetime.datetime.now()
    if (currentTime.hour < 12):
        print("Bom dia!")
    elif 12 <= currentTime.hour < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")


mensagem()
print("Seja bem vindo ao sistema de cantina do SENAI!")
print("Para iniciar coloque a sua matrícula!")
>>>>>>> b9be4afa2b602367bdc8a9bb6853217f2bc80028
