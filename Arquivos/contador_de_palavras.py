import string

def contar_palavras(nome_arquivo):
    contagem = {}
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            texto_completo = f.read()
        # Normalizar para minusculas
        texto_completo = texto_completo.lower()
        pontuacoes = string.punctuation
        # Remover pontuações
        for sinal in pontuacoes:
            texto_completo = texto_completo.replace(sinal, "")
        # Separa a string completa em uma lista de palavras
        lista_palavras = texto_completo.split()
        # Contar as palavras
        for palavra in lista_palavras:
            if palavra in contagem:
                contagem[palavra] += 1 # Se já existir incrementa
            else:
                contagem[palavra] = 1 # Se não  existir cria e define como 1
        return contagem

    except  FileNotFoundError:
        print("Arquivo não encontrado")
        return {}

resultado = contar_palavras("exemplo.txt")
print("--- Frequencia de Palavras ---")
palavras_ordenadas = sorted(resultado.items(),
                            key=lambda item: item[1], reverse=True)

for palavra, quantidade in palavras_ordenadas:
    print(f"{palavra} | {quantidade}")

try:
    with open("relatorio_palavras.txt", "w", encoding = "utf-8") as f:
        for palavra, quantidade in palavras_ordenadas:
            linha = f"{palavra} | {quantidade} \n"
            f.write(linha)
    print("Arquivo de relatório criado com sucesso")
except Exception as e:
    print(e)
