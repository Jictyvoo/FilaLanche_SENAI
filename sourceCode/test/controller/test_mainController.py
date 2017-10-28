from unittest import TestCase
from sourceCode.model.Estudante import Estudante;
import time;


class TestMainController(TestCase):
    def test_buscaEstudante(self, idEstudante, expected):
        if idEstudante == expected:
            prefix = ' OK '
        else:
            prefix = '  X '
        print("%s idEstudante: %s expected: %s" % (prefix, repr(idEstudante), repr(expected)))

    def test_buscaSala(self, idSala, expected):
        if idSala == expected:
            prefix = ' OK '
        else:
            prefix = '  X '
        print("%s idSalae: %s expected: %s" % (prefix, repr(idSala), repr(expected)))


    def test_buscaItem(self, nome, expected):
        if nome == expected:
            prefix = ' OK '
        else:
            prefix = '  X '
        print("%s nome: %s expected: %s" % (prefix, repr(nome), repr(expected)))

    def test_novoPedido(self, idEstudante):
        self.test_novoRegistroEstudante(nome = "Irineu", id = 1234, turma = "chp54125")
        self.alocarTurmasSalas("chp54125", "Microsoft")
        estudante = self.buscaEstudante(1234);
        if (estudante):
            encontrou = estudante.getTurma();
            if (self.podeComprar(self.salas[encontrou].getHorarioIntervalo())):
                return 'Pass'
            else:
                return 'Fail'

    def test_vendeProduto(self, listaDeProdutos):
        for (index, value) in enumerate(listaDeProdutos):
            if (value.setQuantidade(value.getQuantidade() - 1) == True):
                return 'Pass'
            else:
                return 'Fail'

    def test_novoRegistroEstudante(self,  nome, id, turma):
        nome = "Irineu"
        id = 123
        turma = "chp54125"
        novoEstudante = Estudante(turma, id, nome)
        if(self.estudates.append(novoEstudante)):
            return 'Pass'
        else:
            return 'Fail'

    def test_podeComprar(self, horarioNecessario):
        t = time.localtime()
        tempo = str(time.asctime(t)).split(" ")
        atual = tempo[3].replace(":", "-")[0:5]
        c = (int(atual.split('-')[1]) + (int(atual.split('-')[0]) * 60)) - (
            int(horarioNecessario.split('-')[1]) + (int(horarioNecessario.split('-')[0]) * 60));
        if(c <= 20 and c >= 10):
            return 'Pass'
        else:
            return 'Fail'

    def test_carregarProdutosEmEstoque(self):
        self.fail()

    def test_novoProduto(self):
        self.fail()

    def test_alocarTurmasSalas(self):
        self.fail()

    def test_carregarSalas(self):
        self.fail()

    def test_getTodosProdutos(self):
        self.fail()

    def test_registrarLucro(self):
        self.fail()

    def test_modificarEstudante(self):
        self.fail()

    def test_modificarSala(self):
        self.fail()

    def test_modificarItens(self):
        self.fail()
