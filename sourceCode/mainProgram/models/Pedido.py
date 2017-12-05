from datetime import datetime
from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Pedido(DatabaseManipulator):
    def __init__(self, conexao):
        super(Pedido, self).__init__(conexao)

    def novoPedido(self, idEstudante, listaProdutos):  # funcao que realiza um novo pedido
        foundedStudent = self.getEstudante(idEstudante)  # busca o estudante no banco de dados
        if len(foundedStudent) > 0:  # se encontrar algum estudante

            horarioAtual = datetime.now().hour
            turno = 3
            if horarioAtual < 12 and horarioAtual > 6:  # verifica se esta no turno da manha
                turno = 4
            elif horarioAtual < 18 and horarioAtual > 12:  # verifica se esta no turno da tarde
                turno = 5
            else:  # considera que esta no turno da noite
                turno = 3

            turmaEncontrada = foundedStudent[4]  # pega a turma do estudante
            self.__cursor.execute(
                'select * from Sala_Horario where ocupado = "%s"' % turmaEncontrada)  # busca a sala em que a turma esta alocada
            horarioTurno = self.__cursor.fetchone()
            if not horarioTurno:  # se nao existe a turma alocada em sala
                return -1  # retorna o codigo referente ao fato da turma nao estar em sala alguma
            horarioSala = str(horarioTurno[turno])

            if self.podeComprar(horarioSala):  # verifica se o horario permite compra de item
                for index, value in enumerate(listaProdutos):
                    produto = value.split(";")
                    self.__cursor.execute(
                        'insert into Pedido values("%s", "%d", now(), "%s")' % (produto[0], idEstudante,
                                                                                produto[1]))
                    self.conexao.commit()
                self.vendeProduto(listaProdutos)  # utiliza o metodo de venda para remover os produtos disponiveis
                return 1  # retorna 1 se houver sucesso
            else:
                return -2  # retorna -2 se nao estiver no horario de compra da sala
        else:  # caso encontre uma excessao de acesso ao dicionario atraves de uma chave inexistente
            return 0

    def analisaLinhaPedidos(self, entrada):  # metodo que analisa a linha de pedidos feitos
        if entrada == "":  # verifica se a entrada eh vazia, caso o seja, retorna lista vazia
            return []
        analisa = str(entrada).split("-")  # divide a entrada para separar item de cada pedido
        pedido = []  # cria lista de pedidos
        for index, value in enumerate(analisa):  # percorre o vetor com cada item individualmente
            divide = value.split("*")
            # pedido.append(divide)
            if divide[0] != '':
                if int(divide[0]) <= self.analisaMaxIdProduto():  # veirifica se o id esta dentro do padrao:
                    produtoAdicionado = self.getProduto(int(divide[0]))
                    if produtoAdicionado[3] > 0:
                        if len(value.split("*")) > 1:
                            pedido.append(value.replace("*", ";"))  # caso so tenha um item, adiciona apenas 1 item
                        else:
                            pedido.append(value + ";1")  # caso so tenha um item, adiciona apenas 1 item
        return pedido  # retorna o pedido realizado

    def listarPedidos(self):  # metodo para listar todos os pedidos do banco de dados
        self.__cursor.execute('select * from estudante inner join pedido on estudante.matricula = pedido.matricula')
        lista = []
        for linha in self.__cursor.fetchall():  # adiciona varias tuplas na lista de pedidos
            lista.append((linha[2], linha[5], linha[6], linha[7], linha[8]))
        return lista
