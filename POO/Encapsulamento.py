class Carro:
    def __init__(self,marca, modelo,ano):
        self.marca =  marca     # public
        self._modelo =  modelo  # private fraco
        self.__ano =  ano       # private forte

    def showInfo(self):
        print(f"{self.marca} {self._modelo} do ano {self.__ano}")

    def GetMarca(self):
        return self.marca
    
    def SetMarca(self,novaMarca):
        if novaMarca != "":
            self.marca = novaMarca

    def GetModelo(self):
        return self._modelo

    def SetModelo(self,novoModelo):
        if novoModelo != "":
            self._modelo = novoModelo

    def GetAno(self):
        return self.__ano

    def SetAno(self,novoAno):
        if novoAno >= 2015:
            self.__ano = novoAno

carro_1 = Carro("Toyota", "Corolla", 2016)
carro_1.showInfo()
carro_1.SetMarca("BYD")
carro_1.SetModelo("Seal")
carro_1.SetAno(2023)
print(carro_1.GetMarca())
print(carro_1.GetModelo())
print(carro_1.GetAno())

# Más práticas - ignorar o encapsulamento
#print(carro_1._modelo)          # Acessar private GET
#print(carro_1._Carro__ano)      # Acessar private forte GET
#carro_1._modelo = "Lamborgini"  #Modificar private SET

