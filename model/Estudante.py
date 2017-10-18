class Estudante:
	turma = "";
	idEstudante = "";
	nomeAluno = "";

	def __init__(self, turma, idEstudante, nomeAluno):
		self.turma = turma;
		self.idEstudante = idEstudante;
		self.nomeAluno = nomeAluno;

	def getIdEstudante(self):
		return self.idEstudante;

	def setIdEstudante(self, idEstudante):
		self.idEstudante = idEstudante;

	def getNome(self):
		return self.nomeAluno;

	def setNome(self, nomeAluno):
		self.nomeAluno = nomeAluno;

	def getTurma(self):
		return self.turma;

	def setTurma(self, turma):
		self.turma = turma;