# Exemplo 1: Capturando um erro específico (ZeroDivisionError)

try:
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print(f"O resultado é: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir um número por zero!")

print("O programa continua depois da exceção.")

# Exemplo 2: Capturando um erro de conversão (ValueError)

try:
    entrada_usuario = input("Por favor, digite um NÚMERO inteiro: ")
    numero = int(entrada_usuario)
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: Isso não é um número inteiro válido!")

# Exemplo 3: Capturando vários tipos de exceção

lista = [1, 2, 3]
indice = 5 # Um índice que não existe
divisor = 0  # Um divisor zero

try:
    # Tente uma operação arriscada (pode dar IndexError)
    valor = lista[indice]
    print(f"Valor no índice {indice}: {valor}")
    
    # Tente outra operação arriscada (pode dar ZeroDivisionError)
    resultado = 10 / divisor
    print(f"Resultado da divisão: {resultado}")

except IndexError:
    print(f"Erro: O índice {indice} está fora do alcance da lista.")
except ZeroDivisionError:
    print("Erro: Tentativa de divisão por zero.")

print("O programa segue em frente.")

# Exemplo 4: Usando o bloco 'else'

try:
    numerador = 10
    denominador = 2 # Um valor válido
    resultado = numerador / denominador
except ZeroDivisionError:
    print("Erro: Divisão por zero não permitida.")
else:
    # Este bloco só executa se o 'try' der certo
    print(f"A divisão foi um sucesso! Resultado: {resultado}")

# Exemplo 5: Usando o bloco 'finally'

try:
    arquivo = open("meu_arquivo_teste.txt", "w") # "w" = modo de escrita (write)
    arquivo.write("Olá, alunos!")
    # Vamos forçar um erro para ver o 'finally' em ação
    # int("abc") # Descomente esta linha para ver o 'finally' funcionando com erro
except TypeError:
    print("Erro: Não consegui converter o tipo.")
finally:
    # Este bloco executa SEMPRE
    arquivo.close()
    print("Recurso (arquivo) fechado com sucesso no bloco 'finally'.")
  
# Exemplo 6: Juntando tudo (try, except, else, finally)

def dividir_numeros():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        
        resultado = n1 / n2

    except ValueError:
        print("\n[Erro] Você deve digitar apenas números.")
    except ZeroDivisionError:
        print("\n[Erro] O segundo número não pode ser zero.")
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"\n[Erro Inesperado] Ocorreu um problema: {e}")
    else:
        # Só executa se não houver erros
        print(f"\n[Sucesso] O resultado é: {resultado}")
    finally:
        # Executa sempre
        print("\n--- Fim da tentativa de divisão ---")

# Vamos executar a função
dividir_numeros()
