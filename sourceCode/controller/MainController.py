import time;

from model.Estudante import Estudante;
from model.Item import Item
from model.Pedido import Pedido;
from model.Sala import Sala


class MainController:
    estudates = [];
    pedidos = [];
    itens = [];
    salas = [];
    salasDesocupadas = [];

    def __init__(self):
        self.estudates = [];
        self.pedidos = [];
        self.itens = [];
        self.salas = {};
        self.salasDesocupadas = [];

    def buscaEstudante(self, idEstudante):
        for (index, value) in enumerate(self.estudates):
            if (value.getIdEstudante() == idEstudante):
                return value;

    def buscaSala(self, idSala):
        for (index, value) in enumerate(self.salasDesocupadas):
            if (value.getIdSala() == idSala):
                return value;

    def novoPedido(self, idEstudante, listaNomesProdutos):
        foundedStudent = self.buscaEstudante(idEstudante);
        if (foundedStudent):
            turmaEncontrada = foundedStudent.getTurma();  # falta encontrar a turma
            if (self.podeComprar(self.salas[turmaEncontrada].getHorarioIntervalo())):
                novoPedido = Pedido(foundedStudent, listaNomesProdutos);
                self.pedidos.append(novoPedido);
                return True;
        return False;

    def novoRegistroEstudante(self, nome, id, turma):
        novoEstudante = Estudante(turma, id, nome);
        self.estudates.append(novoEstudante);

    def podeComprar(self, horarioNecessario):
        now = time.localtime();
        horarioAtual = "" + now['tm_hour'] + "-" + now['tm_min'];
        can = horarioAtual.split('-')[0] == horarioNecessario.split('-')[0];
        if (not can):
            return False;
        can = int(horarioAtual.split('-')[1]) - int(horarioNecessario.split('-')[1]);
        if (can <= 20 and can >= 10):
            return True;

    def carregarProdutosEmEstoque(self):
        arquivoProdutos = open("../produtos.csv", "r");
        while (True):
            linha = arquivoProdutos.readline().split(';');
            self.itens.append(Item(linha[0], float(linha[1]), int(linha[2])));

    def novoProduto(self, nome, preco, quantidade):
        self.itens.append(Item(nome, preco, quantidade));

    def alocarTurmasSalas(self, turma, idSala):
        salaEncontrada = self.buscaSala(idSala);
        if (salaEncontrada):
            self.salas[turma] = salaEncontrada;
            self.salasDesocupadas.remove(salaEncontrada);

    def carregarSalas(self):
        arquivoProdutos = open("../salas.csv", "r");
        while (True):
            linha = arquivoProdutos.readline().split(';');
            self.salasDesocupadas.append(Sala(linha[0], linha[1]));

