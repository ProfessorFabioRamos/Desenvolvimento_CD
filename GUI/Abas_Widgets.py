import tkinter as tk
from tkinter import ttk

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

root.mainloop()
