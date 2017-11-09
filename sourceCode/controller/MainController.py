import time

from sourceCode.model.Estudante import Estudante
from sourceCode.model.Item import Item
from sourceCode.model.Pedido import Pedido
from sourceCode.model.Sala import Sala


class MainController:
    def __init__(self):
        self.estudates = []
        self.pedidos = []
        self.itens = []
        self.salas = {}  # dicionario que armazena as salas ocupadas
        self.salasDesocupadas = []  # lista com todas as salas desocupadas
        self.itensPreVenda = []  # atributo usado para comparar itens vendidos com itens existentes inicialmente

    def buscaEstudante(self, idEstudante):  # metodo que busca os estudantes nas listas do controller
        for (index, value) in enumerate(self.estudates):
            if value.getIdEstudante() == idEstudante:
                return value

    def buscaSala(self, idSala):  # metodo que busca as salas nas listas do controller
        for (index, value) in enumerate(self.salasDesocupadas):
            if value.getIdSala() == idSala:
                return value

    def buscaItem(self, nome):  # metodo que busca os itens nas listas do controller
        for (index, value) in enumerate(self.itensPreVenda):
            if value.getNome() == nome:
                return value

    def analisaLinhaPedidos(self, entrada):  # metodo que analisa a linha de pedidos feitos
        if entrada == "":  # verifica se a entrada eh vazia, caso o seja, retorna lista vazia
            return []
        analisa = str(entrada).split("-")  # divide a entrada para separar item de cada pedido
        pedido = []  # cria lista de pedidos
        for index, value in enumerate(analisa):  # percorre o vetor com cada item individualmente
            divide = value.split("*")  # divide a linha de cada item para saber o nome do item e a quantidade
            if divide[0] != '':  # evitar erros
                if int(divide[0]) < len(self.getTodosProdutos()):  # veirifica se o id esta dentro do padrao:
                    produtoAdicionado = self.getTodosProdutos()[int(divide[0])]
                    if produtoAdicionado.getQuantidade() > 0:
                        if len(divide) > 1:  # verifica se existe mais de um item na linha
                            for position in range(0, int(
                                    divide[1])):  # adiciona na lista de pedidos o nome do produto varias vezes
                                pedido.append(produtoAdicionado)
                        else:
                            pedido.append(produtoAdicionado)  # caso so tenha um item, adiciona apenas 1 item
        return pedido  # retorna o pedido realizado

    def novoPedido(self, idEstudante, listaProdutos):  # funcao que realiza um novo pedido
        try:  # tenta executar o codigo abaixo
            foundedStudent = self.buscaEstudante(idEstudante)  # busca o estudante na lista
            if foundedStudent:  # se encontrar algum estudante
                turmaEncontrada = foundedStudent.getTurma()  # pega a turma do estudante
                horarioSala = self.salas[
                    turmaEncontrada].getHorarioIntervalo()  # retorna o horario de intervalo da turma
                if self.podeComprar(horarioSala):  # verifica se o horario permite compra de item
                    novoPedido = Pedido(foundedStudent, listaProdutos,
                                        str(time.asctime(time.localtime())).split(" ")[3][
                                        0:5])  # instancia um novo pedido
                    self.pedidos.append(novoPedido)  # adiciona o novo pedido no final da lista de pedidos
                    self.vendeProduto(
                        listaProdutos)  # utiliza o metodo de venda para remover os produtos disponiveis
                    return 1  # retorna 1 se houver sucesso
                else:
                    return -2  # retorna -2 se nao estiver no horario de compra da sala
            return 0
        except KeyError:  # caso encontre uma excessao de acesso ao dicionario atraves de uma chave inexistente
            return -1  # retorna o codigo referente ao fato da turma nao estar em sala alguma

    def vendeProduto(self, listaDeProdutos):  # metodo para remover itens existentes
        for (index, value) in enumerate(listaDeProdutos):
            value.setQuantidade(value.getQuantidade() - 1)

    def novoEstudante(self, nome, id, turma):  # metodo para instanciar um novo estudante
        novoEstudante = Estudante(turma, id, nome)
        self.estudates.append(novoEstudante)

    def podeComprar(self, horarioSala):  # metodo que verifica o horario para saber se pode ou nao fazer o pedido
        now = time.localtime()  # pega o tempo atual
        tempo = str(time.asctime(now)).split(" ")  # converte o tempo atual para uma string e separa em um vetor

        horarioAtual = tempo[3].replace(":", "-")[0:5].split(
            "-")  # separa novamente em um vetor selecionando o que quer
        horarioNecessario = horarioSala.split('-')  # separa o horario necessario no vetor pelo que se quer

        minutoAtual = (int(horarioAtual[1]) + (int(horarioAtual[0]) * 60))  # converte as horas e minutos para minutos
        minutoNecessario = (int(horarioNecessario[1]) + (int(horarioNecessario[0]) * 60))  # idem linha anterior

        pode = minutoNecessario - minutoAtual  # subtrai os minutos para verificar a diferenca de horario
        if pode <= 20 and pode >= 10:  # verifica se esta dentro do horario permitido
            return True
        return False

    def carregarProdutosEmEstoque(self):  # le o arquivo de entrada para armazenar os dados do produto
        arquivoProdutos = open("../entradas/produtos.csv", "r")  # abre o arquivo para leitura
        while True:  # um laco eterno de um python sem do while
            linha = arquivoProdutos.readline().split(';')  # separa cada linha por ';'
            if len(linha) == 3:  # verifica se a linha possui 3 itens, nome, preco e quantidade
                linha[2] = linha[2].replace("\n", "")  # apaga os '\n' lidos no final da linha
                self.itens.append(Item(linha[0], float(linha[1]), int(linha[2])))  # adiciona o item no final da lista
                self.itensPreVenda.append(
                    Item(linha[0], float(linha[1]), int(linha[2])))  # adiciona o item no final da lista
            else:
                return

    def novoProduto(self, nome, preco, quantidade):  # metodo para adicionar um novo produto a venda
        self.itens.append(Item(nome, preco, quantidade))

    def alocarTurmasSalas(self, turma, idSala):  # metodo para alocar as turmas a uma sala
        salaEncontrada = self.buscaSala(idSala)
        if (salaEncontrada):  # verifica se encontrou a sala buscada
            self.salas[turma] = salaEncontrada  # adiciona a sala no dicionario pela chave 'nomeTurma'
            self.salasDesocupadas.remove(salaEncontrada)  # remove a sala das salas desocupadas
            return True
        else:
            return False

    def carregarSalas(self):  # metodo que carrega todas as salas do arquivo de .csv
        arquivoProdutos = open("../entradas/salas.csv", "r")  # abre o arquivo em modo leitura
        while True:  # um laco eterno de um python sem do while
            linha = arquivoProdutos.readline().split(';')  # divide a linha pelos ';'
            if len(linha) == 2:  # verifica se a linha contem apenas os 2 itens necessarios
                linha[1] = linha[1].replace("\n", "")  # apaga o '\n' do final da linha
                self.salasDesocupadas.append(Sala(linha[0], linha[1]))  # adiciona a sala na lista de salas desocupadas
            else:
                return

    def getTodosProdutos(self):  # retorna a lista contendo todos os produtos existentes para venda
        return self.itens

    def getTodasSala(self):  # retorna todas as salas disponiveis
        return self.salasDesocupadas

    def registrarLucro(self):  # metodo para registar o lucro obtido no dia
        arquivoLucro = open(
            "../../lucros/lucroCantina---" + time.asctime(time.localtime()).replace(" ", "-").replace(":", "-")[
                                             0:10] + ".csv", "w")  # cria o arquivo com o nome baseado no tempo
        arquivoLucro.write("Nome Produto; Valor Arreacadado\n")
        for index in range(0, len(self.itens)):  # percorre a lista de itens para armazenar os dados
            arquivoLucro.write(self.itens[index].getNome() + ";" + str(self.itens[index].getPreco() * (
                self.itensPreVenda[index].getQuantidade() - self.itens[
                    index].getQuantidade())) + "\n")  # calcula a diferenca dos itens existentes com os vendidos e armazena o valor arrecadado
        arquivoLucro.close()



    def registrarPedidos(self):  # metodo que registra os produtos para a venda - assemelha-se ao registrarLucro()
        arquivoPedidos = open(
            "../../lucros/pedidosCantina---" + time.asctime(time.localtime()).replace(" ", "-").replace(":", "-")[
                                               0:10] + ".csv", "w")
        arquivoPedidos.write("ID Comprador; Horario de Compra; Produtos Comprados\n")
        for index in range(0, len(self.pedidos)):
            itensPedidos = ""
            for position, value in enumerate(self.pedidos[index].getDescricao()):
                itensPedidos += value.getNome() + "--"
            arquivoPedidos.write(
                str(self.pedidos[index].getIdEstudante().getIdEstudante()) + ";" + self.pedidos[
                    index].getHorarioPedido() + ";" + itensPedidos[0: len(
                    itensPedidos) - 2] + "\n")
        arquivoPedidos.close()

    def modificarEstudante(self, turma, id, nome):  # metodo para modificar os estudantes
        estudante = self.buscaEstudante(id)
        if estudante:  # se achar um estudante modifica os atributos
            estudante.setNome(nome)
            estudante.setTurma(turma)

    def modificarSala(self, id, horarioIntervalo):  # metodo para modificar as salas
        sala = self.buscaSala(id)
        if sala:  # se achar uma sala modifica os atributos
            sala.setHorarioIntervalo(horarioIntervalo)

    def modificarItens(self, nome, preco, quantidade):  # metodo para modificar os itens
        itens = self.buscaItem(nome)
        if itens:  # se achar um item modifica os atributos
            itens.setPreco(preco)
            itens.setQuantidade(quantidade)
