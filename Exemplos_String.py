nome = "Mariana"
frase = 'Olá \nBem-vinda!'
texto_muti_linha = """
Nome: Mariana
Idade: 24
Estado: DF
"""

# Control + / para comentar diversas linhas
print(nome)
print(frase)
print(texto_muti_linha)

# Fatiamento de string
texto = "Programação"
print(texto)        #Programação
print(texto[0])     #P
print(texto[1])     #o
print(texto[0:4])   #Prog
print(texto[4:])    #ramação
print(texto[:5])    #Progr
print(texto[::2])   #Pormço

# Alteração de Caixa
frase = "Ciência de Dados é o futuro"
print(frase.lower())
print(frase.upper())
print(frase.capitalize())
print(frase.title())
print(frase.swapcase())

#Remoção de espaços
frase_2 = " Olá, mundo!  "

print(frase_2)
print(frase_2.strip())  #Remove espaços nas pontas
print(frase_2.lstrip()) #Remove espaços no início
print(frase_2.rstrip()) #Remove espaços no final

frase_3 = "#Exemplo#"
print(frase_3.strip("#")) #Remove caractere específico nas pontas

# Substitui conteúdo de substring (pedaço da string)
mensagem = "Olá Marcos!"
print(mensagem)
nova_mensagem = mensagem.replace("Marcos", "Maria")
print(nova_mensagem)

# Verifica se existe o conteúdo dentro da string
frase_4 = "A IA irá dominar o mundo"
print("IA" in frase_4)
print("AI" in frase_4)
print(frase_4.startswith("A"))      # Verifica se string inicia com valor
print(frase_4.endswith("mundo"))    # Verifica se string termina com valor

#Verifica comprimento da string
palavra = "computador"
print(len(palavra))







