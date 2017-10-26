# arquivo da view do programa para criar a visualizacao do sistema em si


from tkinter import *
from sourceCode.controller.MainController import MainController;
from sourceCode.view.Graphics import Application;
import unittest

controller = MainController();
controller.carregarProdutosEmEstoque();
controller.carregarSalas();

#test

controller.alocarTurmasSalas("chp54125", "Microsoft");
controller.buscaItem("Croquete");
controller.buscaSala("1");
controller.buscaEstudante(123);
controller.modificarEstudante("chp12345",321,"Francis");
controller.modificarItens("Pastel de Catupiri",2.50,10);
controller.modificarSala(456,"20:10");
controller.novoPedido(1,"Croquete");
controller.novoRegistroEstudante("joao",123,"chp54125");
controller.podeComprar("20:00");
controller.novoProduto("Abel",1.55,20);

root = Tk()
Application(root)
root.mainloop()

controller.registrarLucro();