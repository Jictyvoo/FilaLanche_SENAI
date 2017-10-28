class Item:  # Classe que armazena os dados dos produtos a serem vendidos

    def __init__(self, nome, preco, quantidade):  # metodo construtor da classe Item
        self.nome = nome  # atributo de nome do produto a ser vendido na cantina (STRING)
        self.preco = preco  # atributo que indica o preco do produto (FLOAT)
        self.quantidade = quantidade  # atributo que indica a quantidade (INT)

    def getNome(self):  # metodo para retorno do nome do produto
        return self.nome

    def setNome(self, nome):  # metodo para modificar o nome do produto
        self.nome = nome

    def getPreco(self):  # metodo para retornar o preco do item
        return self.preco

    def setPreco(self, preco):  # metodo para modificar o preco do produto
        self.preco = preco

    def getQuantidade(self):  # metodo para retornar a quantidade de itens disponiveis
        return self.quantidade

    def setQuantidade(self, quantidade):  # metodo para modificar a quantidade de itens disponiveis
        self.quantidade = quantidade
