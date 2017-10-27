from sourceCode.controller.MainController import MainController

class Interface:

    def __init__(self):
        self.controller = MainController()
        self.controller.carregarProdutosEmEstoque()
        self.controller.carregarSalas()

    def inserirIdEstudante(self):
        print("Insira o ID do Estudante:")
        idEstudante = str(input())
        return idEstudante

    def mainLoop(self):
        idEstudante = self.inserirIdEstudante()
        estudante = self.controller.buscaEstudante(idEstudante)
        if(not estudante):
            print("Estudante nao encontrado!")
            print("[1] - Inserir novo estudante")
            selecao = input()
            if(selecao == "1"):
                print("ola")
            else:
                self.mainLoop()

    def realizarCadastros(self):
        self.controller.alocarTurmasSalas("chp54125", "Microsoft")
        self.controller.buscaItem("Croquete")
        self.controller.buscaSala("1")
        self.controller.buscaEstudante(123)
        self.controller.modificarEstudante("chp12345", 321, "Francis")
        self.controller.modificarItens("Pastel de Catupiri", 2.50, 10)
        self.controller.modificarSala(456, "20:10")
        self.controller.novoPedido(1, "Croquete")
        self.controller.novoRegistroEstudante("joao", 123, "chp54125")
        self.controller.podeComprar("20:00")
        self.controller.novoProduto("Abel", 1.55, 20)

    def getController(self):
        return self.controller

