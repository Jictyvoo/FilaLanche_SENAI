# arquivo da view do programa para criar a visualizacao do sistema em si

import os

from sourceCode.mainProgram.view.CommandLine import Interface

interface = Interface()

while (interface.mainLoop()):
    os.system("cls")

interface.apresentarLucro()
