import os

from sourceCode.mainProgram.controllers.DatabaseController import DatabaseController


class Interface:
    def __init__(self):
        self.controller = DatabaseController()

    def inserirIdEstudante(self):
        print("Insira o ID do Estudante:")
        idEstudante = str(input("__.> "))
        return idEstudante

    def cadastrarPessoa(self):
        data_nascimento = "00-00-00"
        cpf = 0
        rg = 0
        senha = ""
        nome = ""
        wrongInput = True
        while wrongInput:
            try:
                os.system("cls || clear")
                print("Insira o seu nome")
                nome = str(input("__.> "))
                wrongInput = False
            except:
                wrongInput = True
        wrongInput = True
        while wrongInput:
            try:
                os.system("cls || clear")
                print("Digite a sua data de nascimento! Exemplo : DD-MM-YYYY")
                data_nascimento = str(input("__.> "))
                splitDate = data_nascimento.split("-")
                if len(splitDate) == 3 and len(splitDate[2]) == 4:
                    wrongInput = False
            except:
                wrongInput = True
        wrongInput = True
        while wrongInput:
            try:
                os.system("cls || clear")
                print("Digite o seu CPF:")
                cpf = int(input("__.> "))
                wrongInput = False
            except(ValueError):
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Digite o seu RG:")
                rg = int(input("__.> "))
                wrongInput = False
            except:
                wrongInput = True
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Digite a sua senha : ")
                senha = str(input("__.> "))
                wrongInput = False
            except:
                wrongInput = True

            return self.controller.cadastrarPessoa(nome, cpf, rg, data_nascimento, senha)

    def cadastrarEstudante(self):
        turmaEstudante = ""
        wrongInput = True
        while (wrongInput):
            try:
                os.system("cls || clear")
                print("Insira a turma do Estudante")
                turmaEstudante = str(input("__.> "))
                wrongInput = False
            except:
                wrongInput = True

        id = int(self.cadastrarPessoa())
        a = self.controller.cadastrarEstudante(id, turmaEstudante)
        os.system("cls || clear")
        if a == 0:
            print("Turma não alocada na sala ou sala não existente rs ")
            return -1
        elif a == 1:
            print("Cadastro realizado com sucesso!")
            return id
        elif a == -1:
            print("Turma não registrada no sistema! rs")
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
                print("Estudante não encontrado rs")
            elif codigoRetorno == -1:
                print("Erro! Turma nao alocada em sala rs")
            elif codigoRetorno == -2:
                print("Impossivel fazer pedido, fora do horário permitido rssss")
            elif codigoRetorno == 1:
                print("Pedido Realizado com sucesso!")

    def valida(self, senha, cpf):
        return self.controller.validatePerson(cpf, senha)

    def cadastraproduto(self):
        nome = input("Digite o nome do produto\n__.> ")
        preco = float(input("Digite o preço do produto\n__.> "))

        wrongInput = True
        while wrongInput:
            try:
                quantidade = int(input("Digite a quantidade disponível do produto\n__.> "))
                wrongInput = False
            except:
                print("Digite corretamente rssssssssssssss")
        self.controller.cadastrarProduto(nome, preco, quantidade)

    def apresentarLucro(self):
        lucros = self.controller.registrarLucro()
        listaProdutos = self.controller.getTodosProdutos()
        for index, value in enumerate(listaProdutos):
            try:
                print(value[1] + ": " + str(lucros[str(index + 1)]))
            except KeyError:
                print(value[1] + ": SEM COMPRA")

        print("\nTOTAL: " + str(lucros['total']))

    def cadastrarSala(self):
        nome = input("Digite o nome da sala\n__.> ")
        self.controller.cadastrarSala(nome)
        print("Sala cadastrada com sucesso!")

    def cadastrarTurma(self):
        nome = input("Digite o nome da turma\n__.> ")
        self.controller.cadastrarTurma(nome)
        print("Turma cadastrada com sucesso!")

    def alocarTurmaSala(self):
        nome = input("Digite o nome da turma\n__.> ")
        sala = input("Digite o nome da sala\n__.> ")
        if self.controller.alocarTurmasSalas(nome, sala) == 0:
            print("Turma alocada com sucesso!")
        else:
            print("Turma não alocada com sucesso! rs ")

    def cadastrarHorarioIntervalo(self):
        wrongInput = True
        while wrongInput:
            try:
                hora = int(
                    input(
                        "Você gostaria de adicionar o horário de intervalo para\n[1] - manhã\n[2]-tarde\n[3] - noite\n__.> "))
                wrongInput = False
            except:
                print("Informação inválida rs")

        sala = input("Qual o nome da sala que você gostaria de instalar o intervalo?\n__.> ")
        wrongInput = True
        while (wrongInput):
            horario = input("Qual o horário que você gostaria de instalar? EXEMPLO : HH:MM:SS\n__.> ")
            separado = horario.split(":")
            if (len(separado) >= 2):
                canDoIt = (0 < len(separado[0]) <= 2) and (0 < len(separado[1]) <= 2)
                if len(separado) == 3:
                    canDoIt = canDoIt and len(separado[2]) <= 2
                if canDoIt:
                    wrongInput = False

        if self.controller.cadastrarIntervalo(hora, sala, horario) == 0:
            print("Horário cadastrado com sucesso!")
        else:
            print("Horário não cadastrado com successo! rs")

    def mainLoop(self):
        print("Seja bem vindo ao sistema de lanches do senai\n")
        entrada = input("Digite o seu cpf para continuar!\n__.> ")
        if entrada == "":
            return False
        try:
            cpf = int(entrada)
        except:
            return True
        senha = input("Digite a sua senha para continuar!\n__.> ")
        retorno = self.valida(senha, cpf)
        if retorno == 0:
            id = int(self.controller.getId(cpf, senha))
            if not id:
                return True
            tipo = int(self.controller.getTipo(id))
            if (tipo == 0):
                print("Seja bem vindo estudante!")
                loopi = True
                while (loopi):
                    perg = input("Menu :\n[1]- Fazer Pedido\n[2]-Sair\n__.> ")
                    if perg == "1":
                        self.realizarPedido(self.controller.getIdEstudante(id))
                    elif perg == "2":
                        loopi = False
            elif (tipo == 1):
                loopi = True
                while (loopi):
                    print("Seja bem vindo Administrador")
                    while (loopi):
                        opcao = input(
                            "Menu:\n[0] - Cadastrar Pessoa\n[1]- Cadastrar Aluno\n[2]-Cadastrar Sala\n[3]-Cadastrar Turmas\n[4]-Cadastrar horários de intervalo\n[5] - Alocar Turma na sala\n"
                            "[]- Sair\n__.> ")
                        if (opcao == "0"):
                            self.cadastrarPessoa()
                        elif (opcao == "1"):
                            self.cadastrarEstudante()
                        elif (opcao == "2"):
                            self.cadastrarSala()
                        elif (opcao == "3"):
                            self.cadastrarTurma()
                        elif (opcao == "4"):
                            self.cadastrarHorarioIntervalo()
                        elif opcao == "5":
                            self.alocarTurmaSala()
                        elif (opcao == ""):
                            loopi = False
            elif (tipo == 2):
                loopi = True
                while (loopi):
                    print("Seja bem vind@!")
                    menu = input("MENU\n [1] - Cadastrar produto\n [2] - Verificar lucro do dia!\n [] - Sair\n__.> ")
                    if menu == "1":
                        self.cadastraproduto()
                    elif menu == "2":
                        self.apresentarLucro()
                    elif menu == "":
                        loopi = False

        elif retorno == 1:
            print("Senha não bate com o cpf")
        else:
            print("Usuário não encontrado! r$$$")
        return True
