class Item:
    nome = "";
    preco = 0.0;
    quantidade = 0;

    def __init__(self, nome, preco, quantidade):
        self.nome = nome;
        self.preco = preco;
        self.quantidade = quantidade;

    def getNome(self):
        return self.nome;

    def setNome(self, nome):
        self.nome = nome;

    def getPreco(self):
        return self.preco;

    def setPreco(self, preco):
        self.preco = preco;

    def getQuantidade(self):
        return self.quantidade;

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade;
