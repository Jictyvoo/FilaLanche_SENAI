from sourceCode.mainProgram.models.DatabaseManipulator import DatabaseManipulator


class SalaHorario(DatabaseManipulator):
    def __init__(self, conexao):
        super(SalaHorario, self).__init__(conexao)
