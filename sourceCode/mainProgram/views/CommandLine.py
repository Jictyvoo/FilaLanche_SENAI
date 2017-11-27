import os

from sourceCode.mainProgram.controllers.DatabaseController import DatabaseController


class Interface:
    def __init__(self):
        self.controller = DatabaseController()

    def inserirIdEstudante(self):
        print("Insira o ID do Estudante:")
        idEstudante = str(input("__.> "))
        return idEstudante

    def cadastrarEstudante(self):
        turmaEstudante = ""
        idEstudante = 0
        nomeEstudante = ""
        data_nascimento = "00-00-00"
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Insira o ID do Estudante")
                idEstudante = int(input("__.> "))
                wrongInput = False
            except(ValueError):
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Insira a turma do Estudante")
                turmaEstudante = str(input("__.> "))
                wrongInput = False
            except():
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Insira o nome do Estudante")
                nomeEstudante = str(input("__.> "))
                wrongInput = False
            except():
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Digite a sua data de nascimento! Exemplo : DD-MM-YYYY")
                data_nascimento = str(input("__.> "))
                wrongInput = False
            except():
                wrongInput = True
        self.controller.cadastrarEstudante(nomeEstudante, idEstudante, turmaEstudante, data_nascimento)
        os.system("cls || clear")
        print("Cadastro realizado com sucesso!")
        return idEstudante

    def realizarPedido(self, idEstudante):
        for index, value in enumerate(self.controller.getProdutos()):
            if value[3] > 0:
                print("[" + str(value[0]) + "] - " + value[1] + " -- R$" + str(value[2]))
        print("[] - Sair\nOBS: INSIRA OS PRODUTOS QUE DESEJA COMPRAR DA SEGUINTE FORMA: id*qtd-id*qtd")
        entrada = input("__.> ")

        pedido = self.controller.analisaLinhaPedidos(entrada)
        if len(pedido) >= 1:
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
        estudante = self.controller.getEstudante(int(idEstudante))
        if not estudante:
            print("Estudante nao encontrado!")
            print("[1] - Inserir novo estudante\n[] - Buscar novamente")
            selecao = input("__.> ")
            if selecao == "1":
                idEstudante = self.cadastrarEstudante()
                self.realizarPedido(idEstudante)
        else:
            print(
                "[1] - Modificar Estudante\n[2] - Realizar Pedido\n[3] - Alocar Salas\n[4] - Listar Pedidos\n[5] - Cadastrar Sala\n[6] - Cadastrar Produtos\n[] - Sair")
            entrada = input("__.> ")
            if entrada == "1":
                idEstudante = int(input("Digite o id "))
                nome = str(input("Digite o nome "))
                turma = str(input("Digite a turma "))
                self.controller.modificarEstudante(turma, int(idEstudante), nome)
            elif entrada == "2":
                self.realizarPedido(int(idEstudante))
            elif entrada == "3":
                turma = str(input("Digite a turma: "))
                sala = str(input("Digite a sala alocada: "))
                if self.controller.alocarTurmasSalas(turma, sala) == 0:
                    print("Turma Alocada com sucesso!")
                else:
                    print("Nao foi possivel alocar a turma na sala " + sala)
            elif entrada == "4":
                lista = self.controller.listarPedidos()
                print("####### Pedidos realizados #######\n\n")
                for value in lista:
                    print("Nome do estudante:", value[0], "\nID do produto:", value[1], "\nMatricula: ", value[2],
                          "\nData e Horario:", value[3], "\nQuantidade:", value[4], "\n\n")
            elif entrada == "5":
                self.cadastrarSala()
            elif entrada == "6":
                self.cadastrarProduto()
        return True

    def getController(self):
        return self.controller

    def cadastrarSala(self):
        nome = str(input("Digite o nome da sala\n"))
        horariomanha = str(input("Digite o horário do intervalo da manhã | Formato - hh:mm:ss\n"))
        horariotarde = str(input("Digite o horário do intervalo da tarde: | Formato - hh:mm:ss\n"))
        horarionoite = str(input("Digite o horário do intervalo da noite | Formato - hh:mm:ss\n"))
        self.controller.cadastrarSala(nome, horariomanha, horariotarde, horarionoite)

    def cadastrarProduto(self):
        nomeProduto = input("Qual o nome do produto? ")
        precoProduto = input("Qual o preço do produto? ")
        qntProduto = input("Qual a quantidade do produto? ")
        self.controller.cadastrarProduto(nomeProduto, precoProduto, qntProduto)

    def apresentarLucro(self):
        lucros = self.controller.registrarLucro()
        listaProdutos = self.controller.getTodosProdutos()
        for index, value in enumerate(listaProdutos):
            try:
                print(value[1] + ": " + str(lucros[str(index + 1)]))
            except KeyError:
                print(value[1] + ": SEM COMPRA")

        print("\nTOTAL: " + str(lucros['total']))
