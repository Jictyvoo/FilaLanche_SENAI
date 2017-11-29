from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Estudante(DatabaseManipulator):
    def __init__(self, conexao):
        super(Estudante, self).__init__(conexao)

    def getEstudante(self, idEstudante):  # retorna um estudante existente no banco caso exista
        self.__cursor.execute('select * from Estudante where matricula = "%d"' % idEstudante)
        return self.__cursor.fetchone()

    def getIdPessoa(self, id_estudante):
        self.__cursor.execute('select id_pessoa from Estudante where id_estudante = "%d"' % id_estudante)
        id_pessoa = self.__cursor.fetchone()
        return id_pessoa[0]

    def getIdSala(self, id_estudante):
        self.__cursor.execute('select id_sala from Estudante where id_estudante = "%d"' % id_estudante)
        id_sala = self.__cursor.fetchone()
        return id_sala[0]

    def setIdSala(self, id_estudante, id_sala):
        self.__cursor.execute('update Estudante set id_sala = "%d" where id_estudante = "%d"' % id_sala, id_estudante)
        self.__conexao.commit()

    def getIdTurma(self, id_estudante):
        self.__cursor.execute('select id_turma from Estudante where id_estudante = "%d"' % id_estudante)
        id_turma = self.__cursor.fetchone()
        return id_turma[0]

    def setIdTurma(self, id_estudante, id_turma):
        self.__cursor.execute('update Estudante set id_turma = "%d" where id_estudante = "%d"' % id_turma, id_estudante)
        self.__conexao.commit()
