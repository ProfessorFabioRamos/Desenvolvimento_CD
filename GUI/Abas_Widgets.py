import tkinter as tk
from tkinter import ttk

lista_cadastro = [
    "Nome: Bruno Costa, Idade: 54, Email: bruno.c@email.com",
    "Nome: Carla Fernandes, Idade: 27, Email: carla.f@email.com",
    "Nome: Francisco Mendes, Idade: 32, Email: francisco.m@email.com",
    "Nome: Eliz Silva, Idade: 19, Email: eliz.s@email.com"
]

def exibir_cadastro():
    # Modo normal para poder editar
    caixa_texto.config(state="normal")
    # Limpar caixa antes de inserir dados da linha 1 até o final
    caixa_texto.delete("1.0", tk.END)
    #Junta todos os  elementos da lista mas adiciona uma quebra de linha entre eles
    texto_formatado = "\n".join(lista_cadastro)
    #Insere texto formatado na caixa (END = começo)
    caixa_texto.insert(tk.END, texto_formatado)
    # Desliga a opção de edição
    caixa_texto.config(state="disabled")

def select_combo(event):
    valor = combo_opcoes.get()
    if valor != "Selecione uma opção":
        label_estado_civil.config(text = f"Estado Civil: {valor}")

def change_slider(valor): # valor = string
    print(valor)
    valor_int = f"{float(valor):.0f}"
    label_slider.config(text = f"Volume: {valor_int}")

root = tk.Tk()
root.title("Abas e Widgets")
root.geometry("450x300")

# Criação do notebook (container de abas)
notebook = ttk.Notebook(root)

# Criação  das abas (frames)
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
aba3 = ttk.Frame(notebook)

# Adicionar os frames ao notebook
notebook.add(aba1, text="Cadastro")
notebook.add(aba2, text="Consulta")
notebook.add(aba3, text="Configurações")

# Empacotar o notebook
notebook.pack(padx=10,pady=10, expand = True, fill = "both")

# Widgets da Aba 1
label_aba_1 = ttk.Label(aba1,text = "Formulário de Cadastro")
label_aba_1.pack(padx=20, pady=20)
entry_nome = ttk.Entry(aba1, width = 40)
entry_nome.pack(padx = 20, pady = 5)
btn_salvar = ttk.Button(aba1, text = "Salvar")
btn_salvar.pack(pady=10)

# Widgets da Aba 2
label_aba_2 = ttk.Label(aba2,text = "Área de Consulta")
label_aba_2.pack(padx=20, pady=20)
btn_buscar = ttk.Button(aba2, text = "Buscar", command= exibir_cadastro)
btn_buscar.pack(pady=10)
# Caixa de texto que recebe o cadastro
caixa_texto = tk.Text(
    aba2,
    height= 20,
    width=60,
    wrap="word",
    font = ("Arial",10)
)
# Expandir para ocupar a aba
caixa_texto.pack(pady= 20,fill="both", expand=True)
# Inicia bloqueado para edição
caixa_texto.config(state="disabled")

# Aba 3 - Novos Widgets
#Variável de controle do checkbox
var_check = tk.BooleanVar()
# Estado inicial do checkbox
var_check.set(False)
# Widget CheckBox
check_button = ttk.Checkbutton(aba3, text = "Receber Notificações",
                               variable=var_check)
check_button.pack(padx=20, pady=30)
# Função para buscar o valor da checkbox
#check_button.getboolean()

# Frame para dropdown e slider
frame = ttk.LabelFrame(aba3, text="Opções")
frame.pack(padx=10,pady=10)

lista_estado_civil = [
    "Selecione uma opção",
    "Solteiro(a)",
    "Casado(a)",
    "Divorciado(a)",
    "Viúvo(a)"
]
# Dropdown (ComboBox)
combo_opcoes = ttk.Combobox(frame, values= lista_estado_civil, state="readonly")
combo_opcoes.pack(padx=5,pady=10)
#Estado inicial
combo_opcoes.current(0)
#Label com o estado civil
label_estado_civil = ttk.Label(frame, text="Estado Civil:")
label_estado_civil.pack(padx=10, pady=5)
combo_opcoes.bind("<<ComboboxSelected>>", select_combo)

# Slider(Scale)
slider = ttk.Scale(
    frame,
    from_ = 0,
    to = 100,
    orient = "horizontal",
    command=change_slider
)
slider.pack(padx=5,pady=10, fill="x")
# Label com o valor do slider(scale)
label_slider = ttk.Label(frame, text = "Volume: 0")
label_slider.pack(padx=10,pady=5)

root.mainloop()
