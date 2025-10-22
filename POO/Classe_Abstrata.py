from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):      #Método a ser implementado na subclasse
        pass

    @abstractmethod
    def calcular_perimetro(self): #Método a ser implementado na subclasse
        pass

class Retangulo(Forma):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura

    def calcular_perimetro(self):
        return 2*(self.base+self.altura)

    def mostrar_calculos(self):
        print(f"Retângulo - Area: {self.calcular_area()}, Perímetro: {self.calcular_perimetro()}")

class Triangulo(Forma):
    def __init__(self,base,altura,ladoA,ladoB,ladoC):
        self.base = base
        self.altura = altura
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_area(self):
        return (self.base*self.altura)/2

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def mostrar_calculos(self):
        print(f"Triângulo - Area: {self.calcular_area()}, Perímetro: {self.calcular_perimetro()}")

#forma_1 = Forma()  #ERRO: Não pode instaciar classe abstrata
retangulo_1 = Retangulo(20,30)
retangulo_1.mostrar_calculos()
triangulo_1 = Triangulo(10,15,10,12,13)
triangulo_1.mostrar_calculos()
