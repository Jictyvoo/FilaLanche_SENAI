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

    def valida(self,senha,cpf):
        senhas = self.controller.getPerson().getPassword()
        cpfs = self.controller.getPerson().getCpfs()
        for i in cpfs:
            if int(i)==cpf:
                for m in senhas:
                    if m == senha:
                        return 0
                return 1
        return -1

    def mainLoop(self):
        print("Seja bem vindo ao sistema de lanches do senai")
        cpf = int(input("Digite o seu cpf para continuar!"))
        senha = input("Digite a sua senha para continuar!")
        if self.valida(senha,cpf)== 0:
            id = int(self.controller.getid(cpf,senha))
            tipo = int(self.controller.getTipo(id))
            if(tipo == 0):
                print("Seja bem vindo estudante!")
                print("Menu :\n1- Fazer Pedido")
                self.realizarPedido(id)
            elif(tipo ==1):
                print("Seja bem vindo Administrador")
                print("Menu:\n1- Cadastrar Aluno\n2-Cadastrar Sala\n3-Cadastrar Turmas\n4-Cadastrar horários de intervalo\n"
                      "5-Atribuir horários de intervalo às turmas")
            elif(tipo==2):
                print("Seja bem vinda Atendente da Cantina")
                print("Menu:\n1- Cadastrar Produtos\nVerificar Lucro do dia")

        elif self.valida(senha,cpf)== 1:
            print("Senha não corresponde com o CPF indicado")
        elif self.valida(senha,cpf)==-1:
            print("Cpf não registrado no sistema!")
