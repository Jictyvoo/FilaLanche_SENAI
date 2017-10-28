# arquivo da view do programa para criar a visualizacao do sistema em si

from sourceCode.view.CommandLine import Interface
import os

interface = Interface()

print(interface.getController().alocarTurmasSalas("chp", "Microsoft"))
while (interface.mainLoop()):
    os.system("cls")

interface.getController().registrarLucro()
