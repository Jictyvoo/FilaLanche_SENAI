class Sala:  # classe que armazena a sala pelo seu id e qual o horario de intervalo da mesma
    idSala = "";  # atributo que armazena o id da sala
    horarioIntervalo = "";  # atributo que define o horario de intervalo daquela sala

    def __init__(self, idSala, horarioIntervalo):  # metodo construtor da classe Sala
        self.idSala = idSala;
        self.horarioIntervalo = horarioIntervalo;

    def getIdSala(self):  # metodo que retorna o id da sala
        return self.idSala;

    def setIdSala(self, idSala):  # metodo que modifica o id da sala
        self.idSala = idSala;

    def getHorarioIntervalo(self):  # metodo que retorna o horario de intervalo daquela sala
        return self.horarioIntervalo;

    def setHorarioIntervalo(self, horarioIntervalo):  # metoodo para modificar o horario de intervalo atribuido a sala
        self.horarioIntervalo = horarioIntervalo;
