# Classe para armazenar dados do estudante

class Estudante:

    def __init__(self, turma, idEstudante, nomeAluno):  # metodo construtor da classe estudante
        self.turma = turma  # modifica a propria turma da instancia para receber a nova turma (STRING)
        self.idEstudante = idEstudante  # modifica o proprio id da instancia para receber o novo id (INT)
        self.nomeAluno = nomeAluno  # modifica o proprio nome da instancia para receber o novo nome (STRING)

    def getIdEstudante(self):  # metodo para recebimento do id do estudante
        return self.idEstudante

    def setIdEstudante(self, idEstudante):  # metodo para modificar o id do estudante
        self.idEstudante = idEstudante

    def getNome(self):  # metodo para retornar o nome do estudante
        return self.nomeAluno

    def setNome(self, nomeAluno):  # metodo para modificar o nome do estudante
        self.nomeAluno = nomeAluno

    def getTurma(self):  # metodo para retornar a turma do estudante
        return self.turma

    def setTurma(self, turma):  # metodo para modificar a turma do estudante
        self.turma = turma
