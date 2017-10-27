# arquivo da view do programa para criar a visualizacao do sistema em si


from tkinter import *
from sourceCode.view.Interface import Interface
from sourceCode.view.Graphics import Application
import datetime

def mensagem():
    currentTime = datetime.datetime.now()
    if (currentTime.hour < 12):
        print("Bom dia!")
    elif 12 <= currentTime.hour < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")


mensagem()
print("Seja bem vindo ao sistema de cantina do SENAI!")
print("Para iniciar coloque a sua matrícula!")




