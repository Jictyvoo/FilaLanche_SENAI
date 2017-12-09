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
        nomeEstudante = ""
        data_nascimento = "00-00-00"
        cpf = 0
        rg = 0
        senha = ""
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
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Digite o seu CPF:")
                cpf = int(input("__.> "))
                wrongInput = False
            except():
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Digite o seu RG:")
                rg = int(input("__.> "))
                wrongInput = False
            except():
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Digite a sua senha : ")
                senha = str(input("__.> "))
                wrongInput = False
            except():
                wrongInput = True

        id = self.controller.cadastrarPessoa(nomeEstudante, cpf, rg, data_nascimento, senha)
        a = self.controller.cadastrarEstudante(id, turmaEstudante)
        os.system("cls || clear")
        if a == 0:
            print("Turma não alocada na sala ou sala não existente")
            return -1
        elif a == 1:
            print("Cadastro realizado com sucesso!")
            return id
        elif a == -1:
            print("Turma não registrada no sistema!")
            return -2

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

    def valida(self, senha, cpf):
        senhas = self.controller.getPerson().getPassword()
        cpfs = self.controller.getPerson().getCpfs()
        for index, value in enumerate(cpfs):
            if int(value[0]) == cpf:
                for senhaIndex, senhaValue in enumerate(senhas):
                    if senhaValue[0] == senha:
                        return 0
                return 1
        return -1

    def cadastrarSala(self):
        nome = input("Digite o nome da sala")
        self.controller.cadastrarSala(nome)
        print("Sala cadastrada com sucesso!")

    def cadastrarTurma(self):
        nome = input("Digite o nome da turma")
        self.controller.cadastrarTurma(nome)
        print("Turma cadastrada com sucesso!")

    def cadastrarHorarioIntervalo(self):
        tipo = input("Você gostaria de adicionar o horário de intervalo para\n 1 - manhã\n2-tarde\n3 - noite")

    def mainLoop(self):
        print("Seja bem vindo ao sistema de lanches do senai\n")
        entrada = input("Digite o seu cpf para continuar!\n__.> ")
        if (entrada == ""):
            return False
        try:
            cpf = int(entrada)
        except:
            return True
        senha = input("Digite a sua senha para continuar!\n__.> ")
        retorno = self.valida(senha, cpf)
        if retorno == 0:
            id = int(self.controller.getId(cpf, senha))
            tipo = int(self.controller.getTipo(id))
            if (tipo == 0):
                print("Seja bem vindo estudante!")
                loopi = True
                while (loopi):
                    perg = input("Menu :\n1- Fazer Pedido\n2-Sair\n")
                    if perg == 1:
                        self.realizarPedido(id)
                    elif perg == 2:
                        loopi = False
            elif (tipo == 1):
                loopi = True
                while (loopi):
                    print("Seja bem vindo Administrador")
                    while (loopi):
                        opcao = int(input((
                            "Menu:\n1- Cadastrar Aluno\n2-Cadastrar Sala\n3-Cadastrar Turmas\n4-Cadastrar horários de intervalo\n"
                            "5-Atribuir horários de intervalo às turmas\n6- Sair\n")))
                        if (opcao == 1):
                            self.cadastrarEstudante()
                        elif (opcao == 2):
                            self.cadastrarSala()
                            #  elif(opcao==3):

                        elif (opcao == 6):
                            loopi = False
                        ''''#elif(opcao==4):'''

                    '''

            elif (tipo == 2):
                print("Seja bem vinda Atendente da Cantina")
                print("Menu:\n1- Cadastrar Produtos\nVerificar Lucro do dia")

        elif retorno == 1:
            print("Senha não corresponde com o CPF indicado")
        elif retorno == -1:
            print("Cpf não registrado no sistema!")

        
        
        '''
        return True
