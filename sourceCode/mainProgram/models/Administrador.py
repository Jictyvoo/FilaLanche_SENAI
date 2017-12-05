from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator

class Administrador(DatabaseManipulator):
    def __init__(self, conexao):
        super(Administrador, self).__init__(conexao)

    def cadastrarPessoa(self,nome,cpf,rg,data_nascimento,senha):
        dia, mes, ano = data_nascimento.split("-")  # separa a data de nascimento do estudante
        self.__cursor.execute('insert into Pessoa(nome,cpf,rg,data_nascimento,password) values ("%s","%d","%d","%s","%s")' %(nome,cpf,rg,ano + "-" + mes + "-" + dia,senha))
        self.__cursor.execute('select id_pessoa from Pessoa where cpf = %d' %cpf)
        self.__conexao.commit()
        return int(self.__cursor.fetchone[0])

    def cadastrarAdministrador(self,id,cargo,matricula):
        self.__cursor.execute('insert into Administrador(id_pessoa,cargo,matricula) values ("%d","%s","%d")' %(id,cargo,matricula))
        self.__conexao.commit()

    def getidsala(self,turma):
        self.__cursor.execute('select id_sala from Sala_Horario where nome_sala = "%s"' %(turma))
        return int(self.__cursor.fetchone()[0])
    def getidturma(self,turma):
        self.__cursor.execute('select id_turma from Turma where nome = "%s"' %turma)
        return int(self.__cursor.fetchone()[0])

    def cadastrarEstudante(self,id,turma):  # metodo para instanciar um novo estudante
        idsala = self.getidsala(turma)
        idturma = self.getidturma(turma)
        self.__cursor.execute('insert into Estudante(id_pessoa,id_sala,id_turma) values ("%d","%d","%d")' %(id,idsala,idturma))

    def cadastrarSala(self, nome_sala, manha, noite, tarde):  # metodo para instanciar um novo estudante
        self.__cursor.execute('insert into sala_horario(nome_sala,manha,tarde,noite) values("%s","%s","%s","%s")' % (
            nome_sala, manha, tarde, noite))
        self.__conexao.commit()

    def getSala(self, idSala):  # metodo que busca as salas nas listas do controllers
        self.cursor.execute('select * from Sala_Horario where id_sala = "%d" and ocupado = NULL' % idSala)
        return self.cursor.fetchone()

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
