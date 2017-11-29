from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Administrador(DatabaseManipulator):
    def __init__(self, conexao):
        super(Administrador, self).__init__(conexao)

    def cadastrarEstudante(self, nome, id, id_turma, data_nascimento):  # metodo para instanciar um novo estudante
        dia, mes, ano = data_nascimento.split("-")  # separa a data de nascimento do estudante
        self.__cursor.execute('select * from Turma where id_turma = %d' % id_turma)
        turma = str(self.__cursor.fetchone())
        self.__cursor.execute(
            'insert into Estudante(matricula,nome,turma,data_nascimento) values("%d", "%s","%s","%s")' %
            (id, nome, turma, ano + "-" + mes + "-" + dia))  # insere o estudante no banco de dados
        self.__conexao.commit()

    def cadastrarSala(self, nome_sala, manha, noite, tarde):  # metodo para instanciar um novo estudante
        self.__cursor.execute('insert into sala_horario(nome_sala,manha,tarde,noite) values("%s","%s","%s","%s")' % (
            nome_sala, manha, tarde, noite))
        self.__conexao.commit()

    def alocarTurmasSalas(self, turma, nomeSala):  # metodo para alocar as turmas a uma sala
        try:
            self.__cursor.execute('select id_sala from Sala_Horario where nome_sala = "%s"' % nomeSala)
            id_sala = self.__cursor.fetchone()[0]  # retorna o id da sala que possui aquele nome
            self.__cursor.execute('update Estudante set id_sala = "%s" where turma = "%s"' % (id_sala, turma))
            self.__conexao.commit()  # adiciona a sala na tabela do estudante
            self.__cursor.execute('update Sala_Horario set ocupado = "%s" where id_sala = "%s"' % (turma, id_sala))
            self.__conexao.commit()  # adiciona na sala que ela esta ocupada por alguma turma
            return 0
        except:
            return -1
