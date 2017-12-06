from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Turma(DatabaseManipulator):
    def __init__(self, conexao):
        super(Turma, self).__init__(conexao)

    def getConexao(self):
        return self.__conexao

    def getNome(self, id_turma):
        self.__cursor.execute('select nome from Produto where id_pessoa = "%d"' % id_turma)
        nome = self.__cursor.fetchone()
        return nome[0]

    def setNome(self, id_turma, nome):
        self.__cursor.execute('update Produto set nome = "%s" where id_pessoa = "%d"' % nome, id_turma)
        self.__conexao.commit()
