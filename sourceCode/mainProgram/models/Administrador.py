from sourceCode.mainProgram.models.Pessoa import Pessoa
class Administrador(Pessoa):


    def __init__(self,id,conexao):

    def __init__(self,conexao,id_pessoa,cpf,rg,nome,data_nascimento,id_admin,cargo,matricula):
        super.__init__(conexao,id_pessoa,cpf,rg,nome,data_nascimento)
        self.__id_admin= id_admin
        self.__cargo = cargo
        self.__matricula = matricula
        self.__cursor = self.getConexao().cursor()

    def cadastrarEstudante(self, nome, id,id_turma, data_nascimento):  # metodo para instanciar um novo estudante
        dia, mes, ano = data_nascimento.split("-")  # separa a data de nascimento do estudante
        self.__cursor.execute('select * from Turma where id_turma = %d' %id_turma)
        turma=str(self.__cursor.fetchone())
        self.__cursor.execute('insert into Estudante(matricula,nome,turma,data_nascimento) values("%d", "%s","%s","%s")' %
                            (id, nome, turma, ano + "-" + mes + "-" + dia))  # insere o estudante no banco de dados
        self.__conexao.commit()

    def getEstudante(self, idEstudante):  # retorna um estudante existente no banco caso exista
        self.__cursor.execute('select * from Estudante where matricula = "%d"' % idEstudante)
        return self.__cursor.fetchone()

    def cadastrarSala(self, nome_sala, manha, noite, tarde):  # metodo para instanciar um novo estudante
        self.__cursor.execute('insert into sala_horario(nome_sala,manha,tarde,noite) values("%s","%s","%s","%s")' % (
            nome_sala, manha, tarde, noite))
        self.__conexao.commit()

    def getSala(self, idSala):  # metodo que busca as salas nas listas do controllers
        self.__cursor.execute('select * from Sala_Horario where id_sala = "%d" and ocupado = NULL' % idSala)
        return self.__cursor.fetchone()

    def modificarEstudante(self, id, nome, turma):  # metodo para modificar os estudantes
        self.__cursor.execute('update Estudante set nome = "%s", turma = "%s" where matricula = "%d"' % nome, turma,
                            id)
        self.__conexao.commit()

    def modificarSala(self, id_sala, nome_sala, ocupado, noite, manha, tarde):  # metodo para modificar as salas
        self.__cursor.execute(
            'update Sala_Horario set nome_sala = "%s", ocupado = "%s", noite = "%s", manha = "%s", tarde = "%s" where id_sala = "%s"' %
            nome_sala, ocupado, noite, manha, tarde, id_sala)
        self.__conexao.commit()

    def modificarProduto(self, id_produto, nome, preco, quantidade):  # metodo para modificar os itens
        self.__cursor.execute(
            'update Produto set nome = "%s", preco = "%f", quantidade where matricula = "%d"' % nome, preco,
            quantidade, id_produto)
        self.__conexao.commit()

    def alocarTurmasSalas(self, turma, nomeSala):  # metodo para alocar as turmas a uma sala
        try:
            self.__cursor.execute('select id_sala from Sala_Horario where nome_sala = "%s"' % nomeSala)
            id_sala = self.cursor.fetchone()[0]  # retorna o id da sala que possui aquele nome
            self.__cursor.execute('update Estudante set id_sala = "%s" where turma = "%s"' % (id_sala, turma))
            self.__conexao.commit()  # adiciona a sala na tabela do estudante
            self.__cursor.execute('update Sala_Horario set ocupado = "%s" where id_sala = "%s"' % (turma, id_sala))
            self.__conexao.commit()  # adiciona na sala que ela esta ocupada por alguma turma
            return 0
        except:
            return -1
