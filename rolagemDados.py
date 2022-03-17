import random
from subprocess import DETACHED_PROCESS

class Dado:
    #construtor e atributos
    def __init__(self,tipoDado):
        self.tipoDado = tipoDado

    #gets e sets
    def getDado(self):
        return self.tipoDado
    
    def setDado(self,tipoDado):
        self.tipoDado = tipoDado

    #demias métodos

    def rolarDado(self):
        resultadoDado = 0
        if(self.tipoDado == 1):
            resultadoDado  = random.randrange(1, 21)
        elif(self.tipoDado == 2):
            resultadoDado  = random.randrange(1, 13)
        return resultadoDado

def iniciar():
    opicao = int(input("Deseja inciair o jogo?\n\t[1] - Sim\n\t[2] - Não\n"))
    retorno = False
    if(opicao == 1):
        retorno = True
    else:
        retorno = False

    return retorno
#=====================================================================================#
if(iniciar() == True):
    while True:
    
        dado = Dado(1)

        tipoDado = int(input("Qual dado deseja rolar?\n\t[1] - D20\n\t[2] - D12\n"))
        if(tipoDado == 1):
            dado.setDado(1)
            print(f"D20: {dado.rolarDado()}")
        else:
            dado.setDado(2)
            print(f"D12: {dado.rolarDado()}")

        status = int(input("Deseja continuar jogando?\n\t[1] - Sim\n\t[2] - Não\n"))
        if(status == 2):
            break





        