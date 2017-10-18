class Sala:
	idSala = ""
	horarioIntervalo = ""

	def __init__(self, idSala, horarioIntervalo):
		self.idSala = idSala;
		self.horarioIntervalo = horarioIntervalo;

	def getIdSala(self):
		return self.idSala;

	def setIdSala(self, idSala):
		self.idSala = idSala;

	def getHorarioIntervalo(self):
		return self.horarioIntervalo;

	def setHorarioIntervalo(self, horarioIntervalo):
		self.horarioIntervalo = horarioIntervalo;