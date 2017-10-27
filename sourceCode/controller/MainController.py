import time;

from sourceCode.model.Estudante import Estudante;
from sourceCode.model.Item import Item;
from sourceCode.model.Pedido import Pedido;
from sourceCode.model.Sala import Sala;


class MainController:
    estudates = [];
    pedidos = [];
    itens = [];
    salas = [];
    salasDesocupadas = [];
    itensPreVenda = [];

    def __init__(self):
        self.estudates = [];
        self.pedidos = [];
        self.itens = [];
        self.salas = {};
        self.salasDesocupadas = [];
        self.itensPreVenda = [];

    def getitens(self):
        return self.itens


    def buscaEstudante(self, idEstudante):
        for (index, value) in enumerate(self.estudates):
            if (value.getIdEstudante() == idEstudante):
                return value;

    def buscaSala(self, idSala):
        for (index, value) in enumerate(self.salasDesocupadas):
            if (value.getIdSala() == idSala):
                return value;

    def buscaItem(self, nome):
        for (index, value) in enumerate(self.itensPreVenda):
            if (value.getNome() == nome):
                return value;

    def novoPedido(self, idEstudante, listaNomesProdutos):
        foundedStudent = self.buscaEstudante(idEstudante);
        if (foundedStudent):
            turmaEncontrada = foundedStudent.getTurma();
            if (self.podeComprar(self.salas[turmaEncontrada].getHorarioIntervalo())):
                novoPedido = Pedido(foundedStudent, listaNomesProdutos);
                self.pedidos.append(novoPedido);
                self.vendeProduto(listaNomesProdutos);
                return True;
        return False;

    def vendeProduto(self, listaDeProdutos):
        for (index, value) in enumerate(listaDeProdutos):
            value.setQuantidade(value.getQuantidade() - 1);

    def novoRegistroEstudante(self, nome, id, turma):
        novoEstudante = Estudante(turma, id, nome);
        self.estudates.append(novoEstudante);

    def podeComprar(self, horarioNecessario):
        now = time.localtime();
        tempo = str(time.asctime([now])).split(" ");

        #horarioAtual = "" + now['tm_hour'] + "-" + now['tm_min'];
        horarioAtual = tempo[4].replace(":", "-")
        can = horarioAtual.split('-')[0] == horarioNecessario.split('-')[0];
        if (not can):
            return False;
        can = (int(horarioAtual.split('-')[1]) + (int(horarioAtual.split('-')[0]) * 60)) - (
            int(horarioNecessario.split('-')[1]) + (int(horarioNecessario.split('-')[0]) * 60));
        if (can <= 20 and can >= 10):
            return True;

    def carregarProdutosEmEstoque(self):
        arquivoProdutos = open("../entradas/produtos.csv", "r");
        while (True):
            linha = arquivoProdutos.readline().split(';');
            if(len(linha) == 3):
                linha[2] = linha[2].replace("\n", "");
                self.itens.append(Item(linha[0], float(linha[1]), int(linha[2])));
                self.itensPreVenda.append(Item(linha[0], float(linha[1]), int(linha[2])));
            else:
                return;

    def novoProduto(self, nome, preco, quantidade):
        self.itens.append(Item(nome, preco, quantidade));

    def alocarTurmasSalas(self, turma, idSala):
        salaEncontrada = self.buscaSala(idSala);
        if (salaEncontrada):
            self.salas[turma] = salaEncontrada;
            self.salasDesocupadas.remove(salaEncontrada);
            return True;
        else:
            return False;

    def carregarSalas(self):
        arquivoProdutos = open("../entradas/salas.csv", "r");
        while (True):
            linha = arquivoProdutos.readline().split(';');
            if(len(linha) == 3):
                linha[1] = linha[1].replace("\n", "");
                self.salasDesocupadas.append(Sala(linha[0], linha[1]));
            else:
                return;

    def getTodosProdutos(self):
        return self.itens;

    def registrarLucro(self):
        arquivoLucro = open("../lucros/lucroCantina.csv" + time.strftime('%X %x %Z'), "w");
        for index in range(0, len(self.itens.getDescricao())):
            arquivoLucro.write(self.itens[index].getNome() + ";" + self.itens[index].getPreco() * (
                self.itensPreVenda[index].getQuantidade() - self.itens[index].getQuantidade()));

    def modificarEstudante(self, turma, id, nome):
        estudante = self.buscaEstudante(id);
        if(estudante):
            estudante.setIdEstudante(id);
            estudante.setNome(nome);
            estudante.setTurma(turma);

    def modificarSala(self, id, horarioIntervalo):
        sala = self.buscaSala(id);
        if(sala):
            sala.setIdSala(id);
            sala.setHorarioIntervalo(horarioIntervalo);

    def modificarItens(self, nome, preco, quantidade):
        itens = self.buscaItem(nome);
        if(itens):
            itens.setNome(nome);
            itens.setPreco(preco);
            itens.setQuantidade(quantidade);

