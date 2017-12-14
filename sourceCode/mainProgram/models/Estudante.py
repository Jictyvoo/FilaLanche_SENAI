from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Estudante(DatabaseManipulator):
    def __init__(self, conexao):
        super(Estudante, self).__init__(conexao)

    def getEstudante(self, idEstudante):  # retorna um estudante existente no banco caso exista
        self.getCursor().execute('select * from Estudante where id_estudante = "%d"' % idEstudante)
        return self.getCursor().fetchone()

    def getIdEstudante(self, id_pessoa):
        self.getCursor().execute('select id_estudante from Estudante where id_pessoa = "%d"' % id_pessoa)
        return self.getCursor().fetchone()[0]

    def getIdPessoa(self, id_estudante):
        self.getCursor().execute('select id_pessoa from Estudante where id_estudante = "%d"' % id_estudante)
        id_pessoa = self.getCursor().fetchone()
        return id_pessoa[0]

    def getIdSala(self, id_estudante):
        self.getCursor().execute('select id_sala from Estudante where id_estudante = "%d"' % id_estudante)
        id_sala = self.getCursor().fetchone()
        return id_sala[0]

    def setIdSala(self, id_estudante, id_sala):
        self.getCursor().execute('update Estudante set id_sala = "%d" where id_estudante = "%d"' % id_sala, id_estudante)
        self.getConexao().commit()

    def getIdTurma(self, id_estudante):
        self.getCursor().execute('select id_turma from Estudante where id_estudante = "%d"' % id_estudante)
        id_turma = self.getCursor().fetchone()
        return id_turma[0]

    def setIdTurma(self, id_estudante, id_turma):
        self.getCursor().execute('update Estudante set id_turma = "%d" where id_estudante = "%d"' % id_turma, id_estudante)
        self.getConexao().commit()
