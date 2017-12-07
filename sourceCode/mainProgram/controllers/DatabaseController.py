import MySQLdb
from datetime import datetime
from sourceCode.mainProgram.models.Administrador import Administrador
from sourceCode.mainProgram.models.Pessoa import Pessoa
from sourceCode.mainProgram.models.Pedido import Pedido
from sourceCode.mainProgram.models.Produto import Produto
from sourceCode.mainProgram.models.Estudante import Estudante
from sourceCode.mainProgram.models.Turma import Turma
from sourceCode.mainProgram.models.SalaHorario import SalaHorario


class DatabaseController:
    def __init__(self):
        self.__conexao = MySQLdb.connect('localhost', 'root', '')  # se conecta com o banco de dados
        self.__cursor = self.__conexao.cursor()  # cria um cursor para o banco de dados
        firstConnection = False
        try:  # tenta acessar o banco de dados
            self.__conexao.select_db('Fila_Lanche_SENAI')
        except MySQLdb.DatabaseError:  # caso nao consiga, significa que ele nao existe
            self.executarSQL("../../../database/FilaLanche_SENAI_database.sql")  # executa o sql de criacao do banco
            self.__cursor.close()  # fecha o __cursor para evitar erro
            self.__cursor = self.__conexao.__cursor()  # cria um novo __cursor
            firstConnection = True

        self.__pessoas = Pessoa(self.__conexao)
        self.__administradores = Administrador(self.__conexao)
        self.__estudantes = Estudante(self.__conexao)
        self.__turma = Turma(self.__conexao)
        self.__salas_horarios = SalaHorario(self.__conexao)
        self.__pedidos = Pedido(self.__conexao)
        self.__produtos = Produto(self.__conexao)
        if firstConnection:
            self.__produtos.carregarProdutosEmEstoque()  # le o arquivo csv e carrega no banco
            self.__salas_horarios.carregarSalas()  # le o arquivo csv e carrega no banco

    def getPerson(self):
        return Pessoa(self.__conexao)

    def getAdmin(self):
        return Administrador(self.__conexao)

    def getId(self, cpf, senha):
        self.__cursor.execute('select id_pessoa from Pessoa where cpf = "%d" and password ="%s"' % (cpf, senha))
        return self.__cursor.fetchone()[0]

    def getTipo(self, id_pessoa):
        self.__cursor.execute('select id_pessoa from Estudante')
        ids = self.__cursor.fetchall()
        for i in ids:
            if int(i[0]) == id_pessoa:
                return 0
        self.__cursor.execute('select id_pessoa from Administrador')
        ids = self.__cursor.fecthall()
        for i in ids:
            if int(i[0]) == id_pessoa:
                return 1
        return 2

    def getTodosProdutos(self):  # retorna todos os produtos existentes no banco
        return self.__produtos.getTodosProdutos()

    def getProdutos(self):  # retorna todos os produtos do banco que possuam disponibilidade de venda
        return self.__produtos.getProdutos()

    '''def cadastrarEstudante(self, nome, id, turma, data_nascimento):  # metodo para instanciar um novo estudante
        dia, mes, ano = data_nascimento.split("-")  # separa a data de nascimento do estudante
        self.__cursor.execute(
            'insert into Estudante(matricula,nome,turma,data_nascimento) values("%d", "%s","%s","%s")' % (
                id, nome, turma, ano + "-" + mes + "-" + dia))  # insere o estudante no banco de dados
        self.__conexao.commit()'''

    def getEstudante(self, idEstudante):  # retorna um estudante existente no banco caso exista
        return self.__estudantes.getEstudante(idEstudante)

    '''def cadastrarSala(self, nome_sala, manha, noite, tarde):  # metodo para instanciar um novo estudante
        self.__cursor.execute('insert into sala_horario(nome_sala,manha,tarde,noite) values("%s","%s","%s","%s")' % (
            nome_sala, manha, tarde, noite))
        self.__conexao.commit()'''

    def getSala(self, idSala):  # metodo que busca as salas nas listas do controllers
        self.__salas_horarios.getSala(idSala)

    def cadastrarProduto(self, nome, preco, quantidade):  # metodo para adicionar um novo produto a venda
        self.__cursor.execute(
            'insert into Produto(nome, preco, quantidade) values("%s", "%f", "%d")' % (
                nome, float(preco), int(quantidade)))  # insere o produto no banco de dados
        self.__conexao.commit()

    '''def vendeProduto(self, listaDeProdutos):  # metodo para remover itens existentes
        for (index, value) in enumerate(listaDeProdutos):  # procura o produto na lista de pedidos
            informacao = value.split(";")
            self.__cursor.execute('select quantidade from Produto where id_produto = "%d"' % int(
                informacao[0]))  # busca o produto que existe na lista de pedido e pega a quantidade disponivel de itens
            quantidadeAnterior = self.__cursor.fetchone()[0]
            self.__cursor.execute('update Produto set quantidade = "%d" where id_produto = "%d"' %
                                  (int(quantidadeAnterior) - int(informacao[1]),
                                   int(informacao[0])))  # retira a quantidade comprada de produtos do banco de dados
            self.__conexao.commit()'''

    def podeComprar(self, horarioSala):  # metodo que verifica o horario para saber se pode ou nao fazer o pedido
        now = str(datetime.now().hour) + ":" + str(datetime.now().minute)

        horarioAtual = now.split(":")  # separa novamente em um vetor selecionando o que quer
        horarioNecessario = horarioSala.split(':')  # separa o horario necessario no vetor pelo que se quer

        minutoAtual = (int(horarioAtual[1]) + (int(horarioAtual[0]) * 60))  # converte as horas e minutos para minutos
        minutoNecessario = (int(horarioNecessario[1]) + (int(horarioNecessario[0]) * 60))  # idem linha anterior

        pode = minutoNecessario - minutoAtual  # subtrai os minutos para verificar a diferenca de horario
        if pode <= 20 and pode >= 10:  # verifica se esta dentro do horario permitido
            return True
        return False

    def novoPedido(self, idEstudante, listaProdutos):  # funcao que realiza um novo pedido
        return self.__pedidos.novoPedido(idEstudante, listaProdutos, self.__estudantes.getEstudante, self.podeComprar, self.__turma.getNome)

    def registrarLucro(self):
        self.__cursor.execute('select id_produto, quantidade from Pedido where date(data_horario) = date(curdate())')
        pedidos = self.__cursor.fetchall()  # pega todos os pedidos da data atual
        lucroTotal = 0  # seta um lucro total do dia
        dicionarioLucrosPorProduto = {}  # cria um dicionario para armazenar os lucros
        for linhas in pedidos:  # abre todas as linhas de pedidos
            self.__cursor.execute('select preco from Produto where id_produto = "%d" ' % linhas[0])
            preco = self.__cursor.fetchone()  # pega o preco dos produtos que realizaram pedido
            lucro = float(preco[0]) * int(
                linhas[1])  # pega o valor do produto e multiplica pela quantidade de produtos comprados
            jaArmazenado = False
            for chaves in dicionarioLucrosPorProduto.keys():  # verifica se ja armazenou o lucro daquele item
                if (chaves == str(linhas[0])):
                    jaArmazenado = True
                    break
            if jaArmazenado:
                dicionarioLucrosPorProduto[str(linhas[0])] += lucro  # adiciona o lucro no dicionario
            else:
                dicionarioLucrosPorProduto[str(linhas[0])] = lucro  # adiciona o lucro no dicionario
            lucroTotal += lucro  # adiciona o lucro do produto ao lucro total

        dicionarioLucrosPorProduto['total'] = lucroTotal  # adiciona o lucro total no dicionario
        return dicionarioLucrosPorProduto

    def alocarTurmasSalas(self, turma, nomeSala):  # metodo para alocar as turmas a uma sala
        return self.__administradores.alocarTurmasSalas(turma, nomeSala)

    def analisaLinhaPedidos(self, entrada):  # metodo que analisa a linha de pedidos feitos
        return self.__pedidos.analisaLinhaPedidos(entrada, self.__produtos.analisaMaxIdProduto,
                                                  self.__produtos.getProduto)

    def carregarSQL(self, arquivo_sql):  # carrega o arquivo sql e cortar os camandos em itens de uma lista
        ref_arquivo = open(arquivo_sql, "r")
        linhasCriacao = []
        for linha in ref_arquivo:  # um laco eterno de um python sem do while
            linha = linha.replace("\n", "")  # apaga o '\n' do final da linha
            linhasCriacao.append(linha)

        comandos = []  # cria a lista que ira armazenar os comandos
        tempComando = ""  # string temporaria para armazenar o comando
        for index, value in enumerate(linhasCriacao):  # varre todas as linhas
            tempComando = tempComando + value + " "  # vai adicionando o conteudo de cada uma das linhas na string temporaria
            tamanho = len(value) - 1
            if tamanho > 0:  # verifica se naquela linha existe algum comando
                if value[tamanho] == ";":  # se possuir um ';' no final da linha, adiciona o comando na lista
                    comandos.append(tempComando)
                    tempComando = ""

        return comandos

    def executarSQL(self, arquivo_sql):  # pega a lista de comandos sql e executa
        comandos = self.carregarSQL(arquivo_sql)
        for i, value in enumerate(comandos):
            self.__cursor.execute(value)
