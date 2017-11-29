from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator

class Produto(DatabaseManipulator):
    def __init__(self, conexao):
        super(Produto, self).__init__(conexao)

    def getConexao(self):
        return self.__conexao

    def getNome(self, id_produto):
        self.__cursor.execute('select nome from Produto where id_pessoa = "%d"' % id_produto)
        nome = self.__cursor.fetchone()
        return nome[0]

    def setNome(self, id_produto, nome):
        self.__cursor.execute('update Produto set nome = "%s" where id_pessoa = "%d"' % nome, id_produto)
        self.__conexao.commit()

    def getPreco(self, id_produto):
        self.__cursor.execute('select preco from Produto where id_produto = "%d"' % id_produto)
        preco = self.__cursor.fetchone()
        return preco[0]

    def setPreco(self, id_produto, preco):
        self.__cursor.execute('update Produto set preco = "%f" where id_pessoa = "%d"' % preco, id_produto)
        self.__conexao.commit()

    def getQuantidade(self, id_produto):
        self.__cursor.execute('select quantidade from Produto where id_produto = "%d"' % id_produto)
        quantidade = self.__cursor.fetchone()
        return quantidade[0]

    def setQuantidade(self, id_produto, quantidade):
        self.__cursor.execute('update Produto set quantidade = "%d" where id_pessoa = "%d"' % quantidade, id_produto)
        self.__conexao.commit()