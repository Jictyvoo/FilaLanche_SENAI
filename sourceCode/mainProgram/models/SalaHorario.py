from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class SalaHorario(DatabaseManipulator):
    def __init__(self, conexao):
        super(SalaHorario, self).__init__(conexao)

    def getSalaHorario(self, id_sala):
        self.getCursor().execute('select * from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.getCursor().fetchone()

    def getSala(self, idSala):  # metodo que busca as salas nas listas do controllers
        self.getCursor().execute('select * from Sala_Horario where id_sala = "%d" and ocupado = NULL' % idSala)
        return self.getCursor().fetchone()

    def getIdSala(self, turma):
        self.getCursor().execute('select id_sala from Sala_Horario where ocupado = "%s"' % (turma))
        return int(self.getCursor().fetchone()[0])

    def getNomeSala(self, id_sala):
        self.getCursor().execute('select nome_sala from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.getCursor().fetchone()[0]

    def setNomeSala(self, id_sala, nome_sala):
        self.getCursor().execute('update Sala_Horario set nome_sala = "%s" where id_sala = "%d"' % (nome_sala, id_sala))
        self.getConexao().commit()

    def getOcupado(self, id_sala):
        self.getCursor().execute('select ocupado from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.getCursor().fetchone()[0]

    def setOcupado(self, id_sala, ocupado):
        self.getCursor().execute('update Sala_Horario set ocupado = "%s" where id_sala = "%d"' % (ocupado, id_sala))
        self.getConexao().commit()

    def getNoite(self, id_sala):
        self.getCursor().execute('select noite from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.getCursor().fetchone()[0]

    def setNoite(self, id_sala, noite):
        self.getCursor().execute('update Sala_Horario set noite = "%s" where id_sala = "%d"' % (noite, id_sala))
        self.getConexao().commit()

    def getManha(self, id_sala):
        self.getCursor().execute('select manha from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.getCursor().fetchone()[0]

    def setManha(self, id_sala, manha):
        self.getCursor().execute('update Sala_Horario set manha = "%s" where id_sala = "%d"' % (manha, id_sala))
        self.getConexao().commit()

    def getTarde(self, id_sala):
        self.getCursor().execute('select tarde from Sala_Horario where id_sala = "%d"' % id_sala)
        return self.getCursor().fetchone()[0]

    def setTarde(self, id_sala, tarde):
        self.getCursor().execute('update Sala_Horario set tarde = "%s" where id_sala = "%d"' % (tarde, id_sala))
        self.getConexao().commit()

    def carregarSalas(self):
        ref_arquivo = open("../../entradas/salas.csv", "r")  # abre o arquivo em modo leitura
        while True:  # um laco eterno de um python sem do while
            linha = ref_arquivo.readline().split(';')  # divide a linha pelos ';'
            if len(linha) == 4:  # verifica se a linha contem apenas os 2 itens necessarios
                linha[1] = linha[1].replace("\n", "")  # apaga o '\n' do final da linha
                self.getCursor().execute(
                    'insert into Sala_Horario(nome_sala, manha, tarde, noite) values("%s", "%s", "%s", "%s")' % (
                        linha[0], linha[1], linha[2], linha[3]))
                self.getConexao().commit()
            else:
                return
