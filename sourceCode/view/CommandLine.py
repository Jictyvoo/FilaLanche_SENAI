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
        codigoRetorno = self.controller.novoPedido(idEstudante, pedido)
        if codigoRetorno == 0:
            print("Estudante não encontrado")
        elif codigoRetorno == -1:
            print("Erro! Turma nao alocada em sala")
        elif codigoRetorno == -2:
            print("Impossivel fazer pedido, fora do horário permitido")
        elif codigoRetorno == 1:
            print("Pedido Realizado com sucesso!")

    def mainLoop(self):
        idEstudante = self.inserirIdEstudante()
        if idEstudante == "":
            return False
        estudante = self.controller.buscaEstudante(int(idEstudante))
        if not estudante:
            print("Estudante nao encontrado!")
            print("[1] - Inserir novo estudante\n[] - Buscar novamente")
            selecao = input()
            if selecao == "1":
                idEstudante = self.cadastrarEstudante()
                self.realizarPedido(idEstudante)
        else:
            print("[1] - Modificar Estudante\n[2] - Realizar Pedido\n[] - Sair")
            entrada = input()
            if (entrada == "1"):
                id = int(input("Digite o id "))
                nome = str(input("Digite o nome "))
                turma = str(input("Digite a turma "))
                sala = str(input("Digite a sala alocada : "))
                self.controller.modificarEstudante(turma, int(id), nome)
                self.controller.alocarTurmasSalas(turma,sala)
            elif (entrada == "2"):
                self.realizarPedido(idEstudante)
            else:
                self.mainLoop()
        return True

    def getController(self):
        return self.controller
