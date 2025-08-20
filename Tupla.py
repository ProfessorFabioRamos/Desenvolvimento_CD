# Tupla () com dados de um cliente
cliente = ("José",62, "Brasília")

print("Nome:",cliente[0])
print("Idade:",cliente[1])
print("Cidade:",cliente[2])

# A tupla não permite alterações
cliente[0] = "Maria"

cores = ("vermelho","verde","azul","violeta","carmim")
for cor in cores:
    print(cor)

print(len(cores))
print(cores.count("vermelho"))
print(cores.index("azul"))
