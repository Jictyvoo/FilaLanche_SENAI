class Pessoa:
    def __init__(self, conexao, cpf, rg, nome, data_nascimento):
        self.__cpf = cpf
        self.__rg = rg
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__conexao = conexao
        self.__cursor = self.__conexao.cursor()
        self.__cursor.execute('replace Pessoa(cpf, rg, nome, data_nascimento) values ("%d", "%d", "%s", "%s")' % (
        cpf, rg, nome, data_nascimento))
        self.__cursor.execute(
            'select id_pessoa from Pessoa where cpf = "%d" and rg = "%d" and nome = "%s" and data_nascimento = "%s"' % (
            cpf, rg, nome, data_nascimento))
        self.__id_pessoa = self.__cursor.fetchone[0]

    def __init__(self, conexao, id_pessoa):
        self.__conexao = conexao
        self.__cursor = self.__conexao.cursor()
        self.__cursor.execute('select * from Pessoa where id_pessoa = "%d"' % id_pessoa)
        atributos = self.__cursor.fetchone()
        self.__id_pessoa = atributos[0]
        self.__cpf = atributos[1]
        self.__rg = atributos[2]
        self.__nome = atributos[3]
        self.__data_nascimento = atributos[4]

    def getId_pessoa(self):
        return self.__id_pessoa

    def getCpf(self):
        return self.__cpf

    def setCpf(self, value):
        self.__cursor.execute('update Pessoa set cpf = "%d"' % value)
        self.__conexao.commit()
        self.__cpf = value

    def getRg(self):
        return self.__rg

    def setRg(self, value):
        self.__cursor.execute('update Pessoa set rg = "%d"' % value)
        self.__conexao.commit()
        self.__rg = value

    def getNome(self):
        return self.__nome

    def setNome(self, value):
        self.__cursor.execute('update Pessoa set nome = "%s"' % value)
        self.__conexao.commit()
        self.__nome = value

    def getData_nascimento(self):
        return self.__data_nascimento

    def setData_nascimento(self, value):
        self.__cursor.execute('update Pessoa set data_nascimento = "%s"' % value)
        self.__conexao.commit()
        self.__data_nascimento = value

    def getConexao(self):
        return self.__conexao
