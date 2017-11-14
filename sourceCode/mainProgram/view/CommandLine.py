import os

from sourceCode.mainProgram.controller.DatabaseController import DatabaseController


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
        while(wrongInput):
            try:
                os.system("cls || clear")
                print("Digite a sua data de nascimento! Exemplo : DD-MM-YYYY")
                data_nascimento = str(input("__.> "))
                wrongInput = False
            except():
                wrongInput= True
        self.controller.cadastrarEstudante(nomeEstudante, idEstudante, turmaEstudante, data_nascimento)
        os.system("cls || clear")
        print("Cadastro realizado com sucesso!")
        return idEstudante

    def realizarPedido(self, idEstudante):
        for index, value in enumerate(self.controller.getTodosProdutos()):
            if value[3] > 0:
                print("[" + str(index) + "] - " + value[1] + " -- R$" + str(value[2]))
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
            print("[1] - Modificar Estudante\n[2] - Realizar Pedido\n[3] - Alocar Salas\n[4] - Listar Pedidos\n[] - Sair")
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
                    print("Nome do estudante:", value[0], "\nID do produto:", value[1], "\nMatricula: ",value[2],
                          "\nData e Horario:", value[3], "\nQuantidade:",value[4], "\n\n")
        return True

    def getController(self):
        return self.controller

