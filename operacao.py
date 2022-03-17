from tkinter import Y


class Operacao:
    #construtor e atributos
    def __init__(self, x,y):

        self.x = x
        self.y = y

    #gets e sets
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    #demais métodos
    def soma(self):
        return  self.x + self.y
    
    def subtrair(self):
        return self.x - self.y

    def multiplicar(self):
        return self.x * self.y
    
    def __str__(self):
        return f"X = {self.x}\nY = {self.y}"
#============================================#

objeto1 = Operacao(10,2)
print(objeto1)

print(objeto1.getX())

objeto1.setX(14)

print(objeto1.getX())

print(objeto1.soma())