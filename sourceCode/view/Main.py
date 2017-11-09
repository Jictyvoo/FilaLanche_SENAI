# arquivo da view do programa para criar a visualizacao do sistema em si

from sourceCode.view.CommandLine import Interface
import mysql.connector
import os

interface = Interface()

while (interface.mainLoop()):
    os.system("cls")

interface.getController().registrarLucro()
interface.getController().registrarPedidos()
