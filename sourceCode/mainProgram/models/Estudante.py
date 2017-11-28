from sourceCode.mainProgram.models.Pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, conexao, id_estudante):
        self.__conexao = conexao
        self.__cursor = self.__conexao.cursor()
        self.__cursor.execute('select id_pessoa from Pessoa where id_estudante = "%d"' % id_estudante)
        super(Estudante, self).__init__(conexao, id_estudante)

        self.__cursor.execute('select * from Estudante where id_estudante = "%d"' % id_estudante)
        atributos = self.__cursor.fetchone()
        self.__id_estudante = atributos[0]
        self.__id_pessoa = atributos[1]
        self.__id_sala = atributos[2]
        self.__matricula = atributos[3]
        self.__turma = atributos[4]

    def __init__(self, conexao, id_estudante, id_pessoa, id_sala, matricula, turma):
        print("algo")
