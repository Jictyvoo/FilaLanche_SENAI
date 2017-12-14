from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Turma(DatabaseManipulator):
    def __init__(self, conexao):
        super(Turma, self).__init__(conexao)

    def getIdTurma(self, turma):
        self.getCursor().execute('select id_turma from Turma where nome = "%s"' % turma)
        a = self.getCursor().fetchone()
        if a:
            return int(a[0])
        return -1

    def getNome(self, id_turma):
        self.getCursor().execute('select nome from Turma where id_turma = "%d"' % id_turma)
        nome = self.getCursor().fetchone()
        return nome[0]

    def setNome(self, id_turma, nome):
        self.getCursor().execute('update Produto set nome = "%s" where id_pessoa = "%d"' % nome, id_turma)
        self.getConexao().commit()
