class Pedido:  # classe para armazenar o pedido da pessoa

    def __init__(self, idEstudante, descricao):  # metodo construtor da classe Pedido
        self.idEstudante = idEstudante  # atributo que contem uma lista de itens que foram pedidos para compra
        self.descricao = descricao  # id do estudante que realizou a compra

    def getIdEstudante(self):  # metodo para retornar o id do estudante que comprou o item
        return self.idEstudante

    def getDescricao(self):  # metodo que retorna todos os itens comprados pelo estudante
        return self.descricao

    def setDescricao(self, descricao):  # metodo para modificar a lista de itens comprados pelo estudante
        self.descricao = descricao
