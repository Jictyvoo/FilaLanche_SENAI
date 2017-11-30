from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class SalaHorario(DatabaseManipulator):
    def __init__(self, conexao):
        super(SalaHorario, self).__init__(conexao)

    def getSalaHorario(self, id_sala):
        self.__cursor.execute('select * from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.__cursor.fetchone()

    def getNomeSala(self, id_sala):
        self.__cursor.execute('select nome_sala from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.__cursor.fetchone()[0]

    def setNomeSala(self, id_sala, nome_sala):
        self.__cursor.execute('update Sala_Horario set nome_sala = "%s" where id_sala = "%d"' % (nome_sala, id_sala))
        self.__conexao.commit()

    def getOcupado(self, id_sala):
        self.__cursor.execute('select ocupado from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.__cursor.fetchone()[0]

    def setOcupado(self, id_sala, ocupado):
        self.__cursor.execute('update Sala_Horario set ocupado = "%s" where id_sala = "%d"' % (ocupado, id_sala))
        self.__conexao.commit()

    def getNoite(self, id_sala):
        self.__cursor.execute('select noite from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.__cursor.fetchone()[0]

    def setNoite(self, id_sala, noite):
        self.__cursor.execute('update Sala_Horario set noite = "%s" where id_sala = "%d"' % (noite, id_sala))
        self.__conexao.commit()

    def getManha(self, id_sala):
        self.__cursor.execute('select manha from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.__cursor.fetchone()[0]

    def setManha(self, id_sala, manha):
        self.__cursor.execute('update Sala_Horario set manha = "%s" where id_sala = "%d"' % (manha, id_sala))
        self.__conexao.commit()

    def getTarde(self, id_sala):
        self.__cursor.execute('select tarde from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.__cursor.fetchone()[0]

    def setTarde(self, id_sala, tarde):
        self.__cursor.execute('update Sala_Horario set tarde = "%s" where id_sala = "%d"' % (tarde, id_sala))
        self.__conexao.commit()
