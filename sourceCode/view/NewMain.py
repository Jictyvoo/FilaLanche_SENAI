from tkinter import *
from tkinter import ttk
from sourceCode.controller.MainController import MainController;


main = MainController()

class Main:
    def __init__(self, master=None):
        self.master = master
        master.title("Cantina SENAI")
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


        self.listMenu = Label(self.c3, text="Menu", font=self.fontePadrao)
        self.listMenu.pack(side=LEFT)

        self.listMenu = Label(self.c2, text="      ID", font=self.fontePadrao)
        self.listMenu.pack(side=LEFT)

        objetos = main.getTodosProdutos()
        main.carregarProdutosEmEstoque()
        nomes = []
        for i in objetos:
            nomes.append(i.getNome())
        combo = ttk.Combobox(root)
        combo.place(x=50, y=100)
        combo['values'] = nomes
        combo.pack()

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