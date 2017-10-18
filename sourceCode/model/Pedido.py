class Pedido:
	descricao = [];
	idEstudante = "";

	def __init__(self, idEstudante, descricao):
		self.idEstudante = idEstudante;
		self.descricao = descricao;

	def getIdEstudante(self):
		return self.idEstudante;

	def getDescricao(self):
		return self.descricao;

	def setDescricao(self, descricao):
		self.descricao = descricao;