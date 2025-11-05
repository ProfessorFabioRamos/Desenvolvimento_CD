import tkinter as tk

root = tk.Tk()

root.title("Calculadora 2")

root.geometry("220x300")

# Variavel com a cor de fundo
cor_de_fundo = "#09b7ba"
root.configure(bg= cor_de_fundo)

title = tk.Label(root,text="CALCULADORA", font = ("Arial",16,"bold"),
         bg= cor_de_fundo)
title.grid(row = 0, column = 0, columnspan =2, pady=10)

# Caixa de input de texto 1
entry1 = tk.Entry(root, width =10)
entry1.grid(row=1, column = 0, padx = 20, pady=5, sticky = "e")
# Alinhamento e = East(leste, direita)

# Caixa de input de texto 2
entry2 = tk.Entry(root, width=10)
entry2.grid(row=1, column = 1, padx = 20, pady=5, sticky = "e")

# Variável global do resultado
result = 0
# Função com as 4 operações
def operacao(id):
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    match(id):
        case 0:
            result = num1 + num2
        case 1:
            result = num1 - num2
        case 2:
            result = num1 * num2
        case 3:
            result = num1 / num2
        case _:
            result = num1 + num2
    label_result.config(text = f"Result: {result:.2f}")

# Botão de soma
sum_button = tk.Button(root, text="+")
sum_button.grid(row=2, column=0,padx=10, pady=10)
sum_button.config(command=lambda:operacao(0))

# Botão de subtração
sub_button = tk.Button(root, text="-")
sub_button.grid(row=2, column=1,padx=10, pady=10)
sub_button.config(command=lambda:operacao(1))

# Botão de multiplicação
mult_button = tk.Button(root, text="x")
mult_button.grid(row=3, column=0,padx=10, pady=10)
mult_button.config(command=lambda:operacao(2))

# Botão de divisão
div_button = tk.Button(root, text="/")
div_button.grid(row=3, column=1,padx=10, pady=10)
div_button.config(command=lambda:operacao(3))

# Label a ser alterada
label_result = tk.Label(root, text = "Result: ", font = ("Arial",16),
                        bg = cor_de_fundo, fg = "#c90c35")
label_result.grid(row=4,column=0,columnspan=2,pady=10)

root.mainloop()
