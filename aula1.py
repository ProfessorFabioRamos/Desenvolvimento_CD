import math

'''
# OPERADORES ARITMETICOS
#print(a+b) - Adição
#print(a-b) - Subtração
#print(a*b) - Multiplicação
#print(a/b) - Divisão
#print(3**2) - Potenciação
#print(10//4) - Divisão que retorna parte inteira
#print(5%2) - Divisão que retorna resto (usado para para e impar %2)
#print(9**0.5) - Raiz quadrada
#print(math.sqrt(9))

#OPERADORES LÓGICOS
>
>=
<
<=
and
or
== 
!=
'''
while(True):
    idade = int(input("Digite a sua idade:"))

    if idade < 0 or idade >1000:
        print("Encerrando o programa!")
        break
    if idade <=3:
        print("Bebê")
    elif idade <=12:
        print("Criança")
    elif idade <=17:
        print("Adolescente")
    elif idade <=59:
        print("Adulto")
    else:
        print("Idoso")
