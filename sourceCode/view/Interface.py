from sourceCode.controller.MainController import MainController
import os


class Interface:

    def __init__(self):
        self.controller = MainController()
        self.controller.carregarProdutosEmEstoque()
        self.controller.carregarSalas()

    def inserirIdEstudante(self):
        print("Insira o ID do Estudante:")
        idEstudante = str(input())
        return idEstudante

    def cadastrarEstudante(self):
        turmaEstudante = ""
        idEstudante = 0
        nomeEstudante = ""
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Insira o ID do Estudante")
                idEstudante = int(input())
                wrongInput = False
            except(ValueError):
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Insira a turma do Estudante")
                turmaEstudante = str(input())
                wrongInput = False
            except():
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Insira o nome do Estudante")
                nomeEstudante = str(input())
                wrongInput = False
            except():
                wrongInput = True
        self.controller.novoEstudante(nomeEstudante, idEstudante, turmaEstudante)
        os.system("cls || clear")
        print("Cadastro realizado com sucesso!")
        return idEstudante

    def realizarPedido(self, idEstudante):
        for index, value in enumerate(self.controller.getTodosProdutos()):
            print("[" + str(index) + "] - " + value.getNome() + " -- R$" + str(value.getPreco()))
        print("[] - Sair\nOBS: INSIRA OS PRODUTOS QUE DESEJA COMPRAR DA SEGUINTE FORMA: id*qtd-id*qtd")
        entrada = input()

        analisa = str(entrada).split("-")
        pedido = []
        for index, value in enumerate(analisa):
            divide = value.split("*")
            for position in range(0, int(divide[1])):
                pedido.append(self.controller.getTodosProdutos()[int(divide[0])])
        if(not self.controller.novoPedido(idEstudante, pedido)):
            print("Erro! Turma nao alocada em sala")

    def mainLoop(self):
        idEstudante = self.inserirIdEstudante()
        if (idEstudante == ""):
            return False
        estudante = self.controller.buscaEstudante(idEstudante)
        if (not estudante):
            print("Estudante nao encontrado!")
            print("[1] - Inserir novo estudante\n[] - Buscar novamente")
            selecao = input()
            if (selecao == "1"):
                idEstudante = self.cadastrarEstudante()
                self.realizarPedido(idEstudante)
            else:
                self.mainLoop()
        else:
            print("[1] - Modificar Estudante\n[2] - Realizar Pedido\n[] - Sair")
            entrada = input()
            if (entrada == "1"):
                self.controller.modificarEstudante("chp12345", 321, "Francis")
            elif (entrada == "2"):
                self.realizarPedido(idEstudante)
            else:
                self.mainLoop()
        return True

    def realizarCadastros(self):
        self.controller.alocarTurmasSalas("chp54125", "Microsoft")
        self.controller.modificarItens("Pastel de Catupiri", 2.50, 10)
        self.controller.modificarSala(456, "20:10")
        self.controller.novoProduto("Abel", 1.55, 20)

    def getController(self):
        return self.controller

