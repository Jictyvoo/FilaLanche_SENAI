from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Administrador(DatabaseManipulator):
    def __init__(self, conexao):
        super(Administrador, self).__init__(conexao)

    def cadastrarPessoa(self, nome, cpf, rg, data_nascimento, senha):
        dia, mes, ano = data_nascimento.split("-")  # separa a data de nascimento do estudante
        self.getCursor().execute(
            'insert into Pessoa(nome,cpf,rg,data_nascimento,password) values ("%s","%d","%d","%s","%s")' % (
                nome, cpf, rg, ano + "-" + mes + "-" + dia, senha))
        self.getCursor().execute('select id_pessoa from Pessoa where cpf = %d' % cpf)
        self.getConexao().commit()
        return int(self.getCursor().fetchone[0])

    def cadastrarAdministrador(self, id, cargo, matricula):
        self.getCursor().execute(
            'insert into Administrador(id_pessoa,cargo,matricula) values ("%d","%s","%d")' % (id, cargo, matricula))
        self.getConexao().commit()

    def cadastrarEstudante(self, id, turma, getIdSala, getIdTurma):  # metodo para instanciar um novo estudante
        idsala = getIdSala(turma)
        idturma = getIdTurma(turma)
        self.getCursor().execute(
            'insert into Estudante(id_pessoa,id_sala,id_turma) values ("%d","%d","%d")' % (id, idsala, idturma))

    def cadastrarSala(self, nome_sala, manha, noite, tarde):  # metodo para instanciar um novo estudante
        self.getCursor().execute('insert into sala_horario(nome_sala,manha,tarde,noite) values("%s","%s","%s","%s")' % (
            nome_sala, manha, tarde, noite))
        self.getConexao().commit()

    def alocarTurmasSalas(self, turma, nomeSala):  # metodo para alocar as turmas a uma sala
        try:
            self.getCursor().execute('select id_sala from Sala_Horario where nome_sala = "%s"' % nomeSala)
            id_sala = self.getCursor().fetchone()[0]  # retorna o id da sala que possui aquele nome
            self.getCursor().execute('update Estudante set id_sala = "%s" where turma = "%s"' % (id_sala, turma))
            self.getConexao().commit()  # adiciona a sala na tabela do estudante
            self.getCursor().execute('update Sala_Horario set ocupado = "%s" where id_sala = "%s"' % (turma, id_sala))
            self.getConexao().commit()  # adiciona na sala que ela esta ocupada por alguma turma
            return 0
        except:
            return -1
