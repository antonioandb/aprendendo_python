# exitem tres formas de definir opções formas de definir opções de um widgets.
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("opçõe do widgets")
janela.geometry("600x400")

# 1 no construtor do widget na hora da criação
ttk.Label(janela, text="Olá").pack()

# 2 usando um indice de dicionario apo a criação
#criando o widget
texto = ttk.Label(janela)
#definindo o rotulo
texto["text"] = "Olá Novamente"
texto.pack()

# 3 usando o metodo config() com argumento de palavra chave
texto2 = ttk.Label(janela)
texto2.config(text="Oi")
texto2.pack()
janela.mainloop()