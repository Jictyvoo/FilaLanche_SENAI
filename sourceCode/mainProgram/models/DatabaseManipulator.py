class DatabaseManipulator:
    def __init__(self, conexao):
        self.__conexao = conexao
        self.__cursor = self.__conexao.cursor()

    def getConexao(self):
        return self.__conexao

    def setConexao(self, conexao):
        self.__conexao = conexao

    def getCursor(self):
        return self.__cursor
