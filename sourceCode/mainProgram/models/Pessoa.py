from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Pessoa(DatabaseManipulator):
    def __init__(self, conexao):
        super(Pessoa, self).__init__(conexao)

    def getPessoa(self, id_pessoa):
        self.getCursor().execute('select * from Pessoa where id_pessoa = "%d"' % id_pessoa)
        return self.getCursor().fetchone()

    def getCpfs(self):
        self.getCursor().execute('select cpf from Pessoa')
        return self.getCursor().fetchall()

    def getCpf(self, id_pessoa):
        self.getCursor().execute('select cpf from Pessoa where id_pessoa = "%d"' % id_pessoa)
        cpf = self.getCursor().fetchone()
        return cpf[0]

    def setCpf(self, id_pessoa, cpf):
        self.getCursor().execute('update Pessoa set cpf = "%d" where id_pessoa = "%d"' % cpf, id_pessoa)
        self.getConexao().commit()

    def getRg(self, id_pessoa):
        self.getCursor().execute('select rg from Pessoa where id_pessoa = "%d"' % id_pessoa)
        rg = self.getCursor().fetchone()
        return rg[0]

    def setRg(self, id_pessoa, rg):
        self.getCursor().execute('update Pessoa set rg = "%d" where id_pessoa = "%d"' % rg, id_pessoa)
        self.getConexao().commit()

    def getNome(self, id_pessoa):
        self.getCursor().execute('select nome from Pessoa where id_pessoa = "%d"' % id_pessoa)
        nome = self.getCursor().fetchone()
        return nome[0]

    def setNome(self, id_pessoa, nome):
        self.getCursor().execute('update Pessoa set nome = "%s" where id_pessoa = "%d"' % nome, id_pessoa)
        self.getConexao().commit()

    def getDataNascimento(self, id_pessoa):
        self.getCursor().execute('select data_nascimento from Pessoa where id_pessoa = "%d"' % id_pessoa)
        data_nascimento = self.getCursor().fetchone()
        return data_nascimento[0]

    def setDataNascimento(self, id_pessoa, data_nascimento):
        self.getCursor().execute('update Pessoa set data_nascimento = "%s" where id_pessoa = "%d"' % data_nascimento,
                              id_pessoa)
        self.getConexao().commit()

    def getPassword(self, id_pessoa):
        self.getCursor().execute('select password from Pessoa where id_pessoa = "%d"' % id_pessoa)
        password = self.getCursor().fetchone()
        return password[0]

    def getPassword(self):
        self.getCursor().execute('select password from Pessoa')
        password = self.getCursor().fetchall()
        return password

    def getConexao(self):
        return self.getConexao()
