import json

# ESCRITA
dados_alunos = {
    "universidade":"CEUB",
    "ano_letivo": 2025,
    "aprovados" : True,
    "alunos" : [
        {"nome": "Ana Silva", "nota": 9.4, "presença": "100%"},
        {"nome": "Carlos Souza", "nota": 8.0, "presença": "92%"},
        {"nome": "João Nogueira", "nota": 7.5, "presença": "80%"},
    ]
}

try:
    with open("dados_universidade.json", "w", encoding="utf-8") as f:
        json.dump(dados_alunos, f, indent = 3,ensure_ascii= False)
    print("Arquivo criado com sucesso")
except Exception as e:
    print("Erro:",e)
#################################################################################
# LEITURA
try:
    with open("dados_universidade.json", "r", encoding="utf-8") as f:
        dados_carregados = json.load(f)
        print(f"Universidade: {dados_carregados["universidade"]}")
        print("\nLista de Alunos:")
        for aluno in dados_alunos["alunos"]:
            print(f"- {aluno["nome"]}, Nota: {aluno["nota"]}, Presença: {aluno["presença"]}")
except FileNotFoundError:
    print("Arquivo não encontrado")
except json.JSONDecodeError:
    print("O arquivo existe mas não é um JSON válido.")
