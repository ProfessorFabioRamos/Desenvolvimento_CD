# Listas []
frutas = ["maça","banana","uva","laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[-1])
#
print(len(frutas))
print(frutas.count("banana"))
print(frutas.index("uva"))

for fruta in frutas:
     print(fruta)

# Modificando listas
frutas[0] = "abacaxi"
print(frutas)

# Adicionar
frutas.append("maça")
print(frutas)
# Adicionar no índice específico
frutas.insert(2,"pera")
print(frutas)

#Remover itens
frutas.remove("uva")
print(frutas)

print(frutas.pop())
print(frutas)

del frutas[0]
print(frutas)

# Ordenar de forma crescente
frutas.sort()
print(frutas)
#Inverter a ordem
frutas.reverse()
print(frutas)

idades = [23,45,12,2,98,56]
print(idades)
idades.sort()
idades.sort(reverse = True)
print(idades)
idades.reverse()
print(idades)

# Erro, tipos diferentes
#misto = [1,"oi", 3.1415,True]
#misto.sort()
#print(misto)

#Soma de todos os elementos
soma =sum(idades)
quantidade = len(idades)
print(soma)
media = soma /quantidade
media = sum(idades)/len(idades)

alunos = [
    ["Ana", 8.0],
    ["Bruno", 5.5],
    ["Carla", 6.6]
]

print(alunos[1])
print(alunos[1][1])

for aluno in alunos:
    print(f"{aluno[0]}: {aluno[1]}")
