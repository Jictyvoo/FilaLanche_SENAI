import MySQLdb
from datetime import datetime


class DatabaseController:
    def __init__(self):
        self.conexao = MySQLdb.connect('localhost', 'root', 'sqlpassword')
        self.conexao.select_db('Fila_Lanche_SENAI')
        self.cursor = self.conexao.cursor()

    def getTodosProdutos(self):
        self.cursor.execute('select * from Produto')
        return self.cursor.dictfetchall()

    def cadastrarEstudante(self, nome, id, turma, data_nascimento):  # metodo para instanciar um novo estudante
        self.cursor.execute('insert into table Estudante values(?, ?, ?, ?)', id, nome, turma, data_nascimento)
        self.cursor.commit()

    def getEstudante(self, idEstudante):
        self.cursor.execute('select * from Estudante where matricula = ?', idEstudante)
        return self.cursor.dictfetchall()

    def cadastrarSala(self, id_sala, nome_sala, ocupado, noite, manha,
                      tarde):  # metodo para instanciar um novo estudante
        self.cursor.execute(
            'insert into table Sala_Horario(nome_sala, ocupado, noite, manha, tarde) values(?, ?, ?, ?, ?)', nome_sala,
            ocupado, noite, manha, tarde)
        self.cursor.commit()

    def getSala(self, idSala):  # metodo que busca as salas nas listas do controller
        self.cursor.execute('select * from Sala_Horario where id_sala = ? and ocupado = NULL', idSala)

    def cadastrarProduto(self, nome, preco, quantidade):  # metodo para adicionar um novo produto a venda
        self.cursor.execute(
            'insert into table Produto(nome, preco, quantidade) values(?, ?, ?)', nome, preco, quantidade)
        self.cursor.commit()

    def getProduto(self, id_produto):  # metodo que busca os itens nas listas do controller
        self.cursor.execute('select * from Produto where id_produto = ?', id_produto)

    def vendeProduto(self, listaDeProdutos):  # metodo para remover itens existentes
        for (index, value) in enumerate(listaDeProdutos):
            informacao = value.split(";")
            self.cursor.execute('select quantidade from Produto where id_produto = ?', informacao[0])
            quantidadeAnterior = self.cursor.fetchone()[0]
            self.cursor.execute('update table Produto set quantidade = ? where id_produto = ?',
                                int(quantidadeAnterior) - int(informacao[1]), informacao[0])
            self.cursor.commit()

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

            turmaEncontrada = foundedStudent['turma']  # pega a turma do estudante
            self.cursor.execute('select * from Sala_Horario where ocupado = ?', turmaEncontrada)
            horarioTurno = self.cursor.fetchone()
            if len(horarioTurno) == 0:
                return -1  # retorna o codigo referente ao fato da turma nao estar em sala alguma
            horarioSala = horarioTurno[turno]

            if self.podeComprar(horarioSala):  # verifica se o horario permite compra de item
                for index, value in enumerate(listaProdutos):
                    produto = value.split[";"]
                    self.cursor.execute('insert into table Pedido values(?, ?, curdate(), ?)', produto[0], idEstudante,
                                        produto[1])
                    self.cursor.commit()
                self.vendeProduto(listaProdutos)  # utiliza o metodo de venda para remover os produtos disponiveis
                return 1  # retorna 1 se houver sucesso
            else:
                return -2  # retorna -2 se nao estiver no horario de compra da sala
        else:  # caso encontre uma excessao de acesso ao dicionario atraves de uma chave inexistente
            return 0
