from tkinter import *
import os

creds = 'tempfile.temp'

def signUp():
    global pwordE
    global nameE
    global roots

    roots = Tk()

    roots.title('Signup')

    instruction = Label(roots,text='Seja bem vindo ao sistema de cantina do SENAI! \n')
    instruction.grid(row=0,column=0,sticky=E)
    nameL =  Label(roots,text='Digite a sua matrícula:')
    nameL.grid(row=1,column=0,sticky=W)
    nameE = Entry(roots)
    nameE.grid(row=1, column=1)
    
    signupButton = Button(roots,text='Cadastro',command = FSSignup)
    signupButton.grid(columnspan=2,sticky=W)
    signupButton = Button(roots, text='Login', command=FSSignup)
    signupButton.grid(columnspan=2, sticky=W)


    roots.mainloop()


def FSSignup():
    with open(creds,'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

        roots.destroy()

signUp()





