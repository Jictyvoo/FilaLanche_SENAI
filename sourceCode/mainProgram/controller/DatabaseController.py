import MySQLdb
from datetime import datetime


class DatabaseController:
    def __init__(self):
        self.conexao = MySQLdb.connect('localhost', 'root', '')
        self.cursor = self.conexao.cursor()
        try:
            self.conexao.select_db('Fila_Lanche_SENAI')
        except MySQLdb.DatabaseError:
            self.executarSQL("../../../database/FilaLanche_SENAI_database.sql")
            self.carregarProdutosEmEstoque()
            self.carregarSalas()
            self.cursor.close()
            self.cursor = self.conexao.cursor()

    def getTodosProdutos(self):
        self.cursor.execute('select * from Produto')
        return self.cursor.fetchall()

    def cadastrarEstudante(self, nome, id, turma, data_nascimento):  # metodo para instanciar um novo estudante
        dia, mes, ano = data_nascimento.split("-")
        self.cursor.execute(
            'insert into Estudante(matricula,nome,turma,data_nascimento) values("%d", "%s","%s","%s")' % (
                id, nome, turma, ano + "-" + mes + "-" + dia))
        self.conexao.commit()

    def getEstudante(self, idEstudante):
        self.cursor.execute('select * from Estudante where matricula = "%d"' % idEstudante)
        return self.cursor.fetchone()

    def cadastrarSala(self, nome_sala, ocupado, noite, manha,
                      tarde):  # metodo para instanciar um novo estudante
        self.cursor.execute(
            'insert into Sala_Horario(nome_sala, ocupado, noite, manha, tarde) values("%s", "%s", "%s", "%s", "%s")' % (
                nome_sala,
                ocupado, noite, manha, tarde))
        self.conexao.commit()

    def getSala(self, idSala):  # metodo que busca as salas nas listas do controller
        self.cursor.execute('select * from Sala_Horario where id_sala = "%d" and ocupado = NULL' % idSala)
        return self.cursor.fetchone()

    def cadastrarProduto(self, nome, preco, quantidade):  # metodo para adicionar um novo produto a venda
        self.cursor.execute(
            'insert into Produto(nome, preco, quantidade) values("%s", "%f", "%d")' % nome, preco, quantidade)
        self.conexao.commit()

    def getProduto(self, id_produto):  # metodo que busca os itens nas listas do controller
        self.cursor.execute('select * from Produto where id_produto = "%d"' % id_produto)
        return self.cursor.fetchone()

    def modificarEstudante(self, id, nome, turma):  # metodo para modificar os estudantes
        self.cursor.execute('update Estudante set nome = "%s", turma = "%s" where matricula = "%d"' % nome, turma,
                            id)
        self.conexao.commit()

    def modificarSala(self, id_sala, nome_sala, ocupado, noite, manha, tarde):  # metodo para modificar as salas
        self.cursor.execute(
            'update Sala_Horario set nome_sala = "%s", ocupado = "%s", noite = "%s", manha = "%s", tarde = "%s" where id_sala = "%s"' %
            nome_sala, ocupado, noite, manha, tarde, id_sala)
        self.conexao.commit()

    def modificarProduto(self, id_produto, nome, preco, quantidade):  # metodo para modificar os itens
        self.cursor.execute(
            'update Produto set nome = "%s", preco = "%f", quantidade where matricula = "%d"' % nome, preco,
            quantidade, id_produto)
        self.conexao.commit()

    def vendeProduto(self, listaDeProdutos):  # metodo para remover itens existentes
        for (index, value) in enumerate(listaDeProdutos):
            informacao = value.split(";")
            self.cursor.execute('select quantidade from Produto where id_produto = "%d"' % int(informacao[0]))
            quantidadeAnterior = self.cursor.fetchone()[0]
            self.cursor.execute('update Produto set quantidade = "%d" where id_produto = "%d"' %
                                (int(quantidadeAnterior) - int(informacao[1]), int(informacao[0])))
            self.conexao.commit()

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
        foundedStudent = self.getEstudante(idEstudante)  # busca o estudante no banco de dados
        if len(foundedStudent) > 0:  # se encontrar algum estudante

            horarioAtual = datetime.now().hour
            turno = 3
            if horarioAtual < 12 and horarioAtual > 6:
                turno = 4
            elif horarioAtual < 18 and horarioAtual > 12:
                turno = 5
            else:
                turno = 3

            turmaEncontrada = foundedStudent[4]  # pega a turma do estudante
            self.cursor.execute('select * from Sala_Horario where ocupado = "%s"' % turmaEncontrada)
            horarioTurno = self.cursor.fetchone()
            if not horarioTurno:
                return -1  # retorna o codigo referente ao fato da turma nao estar em sala alguma
            horarioSala = str(horarioTurno[turno])

            if self.podeComprar(horarioSala):  # verifica se o horario permite compra de item
                for index, value in enumerate(listaProdutos):
                    produto = value.split(";")
                    self.cursor.execute(
                        'insert into Pedido values("%s", "%d", curdate(), "%s")' % (produto[0], idEstudante,
                                                                                    produto[1]))
                    self.conexao.commit()
                self.vendeProduto(listaProdutos)  # utiliza o metodo de venda para remover os produtos disponiveis
                return 1  # retorna 1 se houver sucesso
            else:
                return -2  # retorna -2 se nao estiver no horario de compra da sala
        else:  # caso encontre uma excessao de acesso ao dicionario atraves de uma chave inexistente
            return 0

    def registrarLucro(self):
        self.cursor.execute('select id_produto, quantidade from Pedido where date(data_horario) = date(curdate())')
        pedidos = self.cursor.fetchall()
        lucroTotal = 0
        dicionarioLucrosPorProduto = {}
        for linhas in pedidos:
            self.cursor.execute('select preco from Produto where id_produto = "%d" ' % linhas[0])
            preco = self.cursor.fetchone()
            lucro = float(preco[0]) * int(linhas[1])
            dicionarioLucrosPorProduto[str(linhas[0])] = lucro
            lucroTotal += lucro

        dicionarioLucrosPorProduto['total'] = lucroTotal
        return dicionarioLucrosPorProduto

    def alocarTurmasSalas(self, turma, nomeSala):  # metodo para alocar as turmas a uma sala
        try:
            self.cursor.execute('select id_sala from Sala_Horario where nome_sala = "%s"' % nomeSala)
            id_sala = self.cursor.fetchone()[0]
            self.cursor.execute('update Estudante set id_sala = "%s" where turma = "%s"' % (id_sala, turma))
            self.conexao.commit()
            self.cursor.execute('update Sala_Horario set ocupado = "%s" where id_sala = "%s"' % (turma, id_sala))
            self.conexao.commit()
            return 0
        except:
            return -1

    def analisaLinhaPedidos(self, entrada):  # metodo que analisa a linha de pedidos feitos
        if entrada == "":  # verifica se a entrada eh vazia, caso o seja, retorna lista vazia
            return []
        analisa = str(entrada).split("-")  # divide a entrada para separar item de cada pedido
        pedido = []  # cria lista de pedidos
        for index, value in enumerate(analisa):  # percorre o vetor com cada item individualmente
            divide = value.split("*")
            # pedido.append(divide)
            if divide[0] != '':
                if int(divide[0]) < len(self.getTodosProdutos()):  # veirifica se o id esta dentro do padrao:
                    produtoAdicionado = self.getProduto(int(divide[0]))
                    if produtoAdicionado[3] > 0:
                        if len(value.split("*")) > 1:
                            pedido.append(value.replace("*", ";"))  # caso so tenha um item, adiciona apenas 1 item
                        else:
                            pedido.append(value + ";1")  # caso so tenha um item, adiciona apenas 1 item
        return pedido  # retorna o pedido realizado

    def carregarSQL(self, arquivo_sql):
        ref_arquivo = open(arquivo_sql, "r")
        linhasCriacao = []
        for linha in ref_arquivo:  # um laco eterno de um python sem do while
            linha = linha.replace("\n", "")  # apaga o '\n' do final da linha
            linhasCriacao.append(linha)

        comandos = []
        tempComando = ""
        for index, value in enumerate(linhasCriacao):
            tempComando = tempComando + value + " "
            tamanho = len(value) - 1
            if tamanho > 0:
                if value[tamanho] == ";":
                    comandos.append(tempComando)
                    tempComando = ""

        return comandos

    def executarSQL(self, arquivo_sql):
        comandos = self.carregarSQL(arquivo_sql)
        for i, value in enumerate(comandos):
            self.cursor.execute(value)

    def carregarSalas(self):
        ref_arquivo = open("../../entradas/salas.csv", "r")  # abre o arquivo em modo leitura
        while True:  # um laco eterno de um python sem do while
            linha = ref_arquivo.readline().split(';')  # divide a linha pelos ';'
            if len(linha) == 4:  # verifica se a linha contem apenas os 2 itens necessarios
                linha[1] = linha[1].replace("\n", "")  # apaga o '\n' do final da linha
                self.cursor.execute(
                    'insert into Sala_Horario(nome_sala, manha, tarde, noite) values("%s", "%s", "%s", "%s")' % (linha[0], linha[1], linha[2], linha[3]))
                self.conexao.commit()
            else:
                return

    def carregarProdutosEmEstoque(self):  # le o arquivo de entrada para armazenar os dados do produto
        arquivoProdutos = open("../../entradas/produtos.csv", "r")  # abre o arquivo para leitura
        while True:  # um laco eterno de um python sem do while
            linha = arquivoProdutos.readline().split(';')  # separa cada linha por ';'
            if len(linha) == 3:  # verifica se a linha possui 3 itens, nome, preco e quantidade
                linha[2] = linha[2].replace("\n", "")  # apaga os '\n' lidos no final da linha
                self.cursor.execute('insert into Produto(nome, preco, quantidade) values("%s", "%f", "%d")' % (
                    linha[0], float(linha[1]), int(linha[2])))
            else:
                return

    def listarPedidos(self):
        self.cursor.execute('select * from estudante inner join pedido on estudante.matricula = pedido.matricula')
        lista = []
        for linha in self.cursor.fetchall():
            lista.append((linha[2], linha[5], linha[6], linha[7], linha[8]))
        return lista
