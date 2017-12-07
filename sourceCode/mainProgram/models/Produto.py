from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Produto(DatabaseManipulator):
    def __init__(self, conexao):
        super(Produto, self).__init__(conexao)

    def getProduto(self, id_produto):  # metodo que busca os itens nas listas do controllers
        self.getCursor().execute('select * from Produto where id_produto = "%d"' % id_produto)
        return self.getCursor().fetchone()

    def getNome(self, id_produto):
        self.getCursor().execute('select nome from Produto where id_pessoa = "%d"' % id_produto)
        nome = self.getCursor().fetchone()
        return nome[0]

    def setNome(self, id_produto, nome):
        self.getCursor().execute('update Produto set nome = "%s" where id_pessoa = "%d"' % nome, id_produto)
        self.getConexao().commit()

    def getPreco(self, id_produto):
        self.getCursor().execute('select preco from Produto where id_produto = "%d"' % id_produto)
        preco = self.getCursor().fetchone()
        return preco[0]

    def setPreco(self, id_produto, preco):
        self.getCursor().execute('update Produto set preco = "%f" where id_pessoa = "%d"' % preco, id_produto)
        self.getConexao().commit()

    def getQuantidade(self, id_produto):
        self.getCursor().execute('select quantidade from Produto where id_produto = "%d"' % id_produto)
        quantidade = self.getCursor().fetchone()
        return quantidade[0]

    def setQuantidade(self, id_produto, quantidade):
        self.getCursor().execute('update Produto set quantidade = "%d" where id_pessoa = "%d"' % quantidade, id_produto)
        self.getConexao().commit()

    def getTodosProdutos(self):  # retorna todos os produtos existentes no banco
        self.getCursor().execute('select * from Produto')
        return self.getCursor().fetchall()

    def getProdutos(self):  # retorna todos os produtos do banco que possuam disponibilidade de venda
        self.getCursor().execute('select * from Produto where quantidade > 0')
        return self.getCursor().fetchall()

    def analisaMaxIdProduto(self):  # verifica qual o id maximo do produto disponivel para compra
        self.getCursor().execute('select max(id_produto) from produto where quantidade > 0')
        max = self.getCursor().fetchone()
        return int(max[0])

    def carregarProdutosEmEstoque(self):  # le o arquivo de entrada para armazenar os dados do produto
        arquivoProdutos = open("../../entradas/produtos.csv", "r")  # abre o arquivo para leitura
        while True:  # um laco eterno de um python sem do while
            linha = arquivoProdutos.readline().split(';')  # separa cada linha por ';'
            if len(linha) == 3:  # verifica se a linha possui 3 itens, nome, preco e quantidade
                linha[2] = linha[2].replace("\n", "")  # apaga os '\n' lidos no final da linha
                self.getCursor().execute('insert into Produto(nome, preco, quantidade) values("%s", "%f", "%d")' % (
                    linha[0], float(linha[1]), int(linha[2])))
                self.getConexao().commit()
            else:
                return
