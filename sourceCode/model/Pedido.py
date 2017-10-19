class Pedido:  # classe para armazenar o pedido da pessoa
    descricao = [];  # atributo que contem uma lista de itens que foram pedidos para compra
    idEstudante = "";  # id do estudante que realizou a compra

    def __init__(self, idEstudante, descricao):  # metodo construtor da classe Pedido
        self.idEstudante = idEstudante;
        self.descricao = descricao;

    def getIdEstudante(self):  # metodo para retornar o id do estudante que comprou o item
        return self.idEstudante;

    def getDescricao(self):  # metodo que retorna todos os itens comprados pelo estudante
        return self.descricao;

    def setDescricao(self, descricao):  # metodo para modificar a lista de itens comprados pelo estudante
        self.descricao = descricao;
