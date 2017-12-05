from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class Turma(DatabaseManipulator):
    def __init__(self, conexao):
        super(Turma, self).__init__(conexao)
