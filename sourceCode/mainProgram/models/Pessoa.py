from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Pessoa(DatabaseManipulator):
    def __init__(self, conexao):
        super(Pessoa, self).__init__(conexao)
        self.__cursor = conexao.cursor()

    def getCpfs(self):
        self.__cursor.execute('select cpf from Pessoa')
        return self.__cursor.fetchall()

    def getPessoa(self, id_pessoa):
        self.__cursor.execute('select * from Pessoa where id_pessoa = "%d"' % id_pessoa)
        return self.__cursor.fetchone()

    def getCpf(self, id_pessoa):
        self.__cursor.execute('select cpf from Pessoa where id_pessoa = "%d"' % id_pessoa)
        cpf = self.__cursor.fetchone()
        return cpf[0]

    def setCpf(self, id_pessoa, cpf):
        self.__cursor.execute('update Pessoa set cpf = "%d" where id_pessoa = "%d"' % cpf, id_pessoa)
        self.__conexao.commit()

    def getRg(self, id_pessoa):
        self.__cursor.execute('select rg from Pessoa where id_pessoa = "%d"' % id_pessoa)
        rg = self.__cursor.fetchone()
        return rg[0]

    def setRg(self, id_pessoa, rg):
        self.__cursor.execute('update Pessoa set rg = "%d" where id_pessoa = "%d"' % rg, id_pessoa)
        self.__conexao.commit()

    def getNome(self, id_pessoa):
        self.__cursor.execute('select nome from Pessoa where id_pessoa = "%d"' % id_pessoa)
        nome = self.__cursor.fetchone()
        return nome[0]

    def setNome(self, id_pessoa, nome):
        self.__cursor.execute('update Pessoa set nome = "%s" where id_pessoa = "%d"' % nome, id_pessoa)
        self.__conexao.commit()

    def getDataNascimento(self, id_pessoa):
        self.__cursor.execute('select data_nascimento from Pessoa where id_pessoa = "%d"' % id_pessoa)
        data_nascimento = self.__cursor.fetchone()
        return data_nascimento[0]

    def setDataNascimento(self, id_pessoa, data_nascimento):
        self.__cursor.execute('update Pessoa set data_nascimento = "%s" where id_pessoa = "%d"' % data_nascimento,
                              id_pessoa)
        self.__conexao.commit()

    def getPassword(self, id_pessoa):
        self.__cursor.execute('select password from Pessoa where id_pessoa = "%d"' % id_pessoa)
        password = self.__cursor.fetchone()
        return password[0]

    def getPassword(self):
        self.__cursor.execute('select password from Pessoa')
        password = self.__cursor.fetchall()
        return password

    def getConexao(self):
        return self.__conexao
