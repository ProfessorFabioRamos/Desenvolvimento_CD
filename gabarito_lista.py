# Exercício 1
# turma = ("André","Fernanda","Luiz")
#
# nome = input("Digite o nome de um aluno: ")
#
# if nome in turma:
#     print("Aluno está matriculado")
# else:
#     print("Aluno NÃO matriculado")

# Exercício 2

# a,b = 0,1
#
# n = 10
#
# for _ in range(n):
#     print(a)
#     a,b = b, a + b

#Exercício 3

# notas = [6.3, 7.5, 9.2, 5.1, 6.8]
#
# media_turma = sum(notas)/len(notas)
# print(f"A média da turma foi {media_turma}")
#
# acima_media = 0
#
# for n in notas:
#     if n > 6:
#         acima_media +=1
#
# print(f"Notas acima da media: {acima_media}")

#Exercício 4
# import random
#
# def jogar():
#     opcoes = ["pedra","papel","tesoura"]
#     vitorias = 0
#     derrotas = 0
#     empates = 0
#
#     print("-- PEDRA, PAPEL E TESOURA --")
#
#     while True:
#         jogada = input(""" Escolha a sua jogada: pedra, papel ou tesoura.
#     Digite sair para abandonar o jogo: """).lower()
#         if jogada == "sair":
#             break
#         elif jogada not in opcoes:
#             print("Opção inválida!")
#             continue
#
#         ia = random.choice(opcoes)
#         print(f"Você escolheu: {jogada}")
#         print(f"A IA escolheu: {ia}")
#
#         if jogada == ia:
#             print("Empate")
#             empates +=1
#         elif (jogada == "pedra" and ia == "tesoura" or \
#                 jogada == "papel" and ia == "pedra" or \
#                 jogada == "tesoura" and ia == "papel"):
#             print("Você venceu =) !")
#             vitorias+=1
#         else:
#             print("Você perdeu =( !")
#             derrotas+=1
#
#     print("Resultado final:")
#     print(f"Vitórias: {vitorias}")
#     print(f"Derrotas: {derrotas}")
#     print(f"Empates: {empates}")
#
# jogar()

# Exercício 5

biblioteca = []

def adicionar_livro(titulo, autor, ano):
    livro = [titulo, autor, ano]
    biblioteca.append(livro)
    print(f"Livro {titulo} adicionado com sucesso!")

def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado")
    else:
        print("Lista de de livros:")
        for l in biblioteca:
            print(f"Título: {l[0]} | Autor: {l[1]} | Ano: {l[2]}")

def buscar_livro(titulo_busca):
    encontrados = [livro for livro in biblioteca if titulo_busca.lower() in \
                   livro[0].lower()]
    if encontrados:
        print("Encontrados:")
        for l in encontrados:
            print(f"Título: {l[0]} | Autor: {l[1]} | Ano: {l[2]}")
    else: 
        print("Nenhum livro com este título foi encontrado")
    
while True:
    print("--Biblioteca App--")
    print("1 - Adicionar Livro")
    print("2 - Listar Livros")
    print("3 - Buscar Livro por titulo")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção >"))

    if opcao == 1:
        titulo = input("Digite a titulo: ")
        autor = input("Digite a autor: ")
        ano = input("Digite a ano de publicação: ")
        adicionar_livro(titulo, autor, ano)
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        busca = input("Digite o titulo a buscar")
        buscar_livro(busca)
    elif opcao == 4:
        print("Saindo do app...")
        break
    else:
        print("Opção inválida")
