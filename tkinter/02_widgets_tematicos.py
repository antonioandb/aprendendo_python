# o Tkinter tem duas gerações de widgets o mais antigo tk e o mais novos ttk, o ttk subtitue varios widgets do tk mas não todos.
# os novos widgets (ttk widget) tem varias vantagens uma delas é que eles têm a aparência nativa da plataforma na qual o programa é executado.
import tkinter as tk
from tkinter import ttk #importando os novos widgets

janela = tk.Tk()
janela.title("Widgets")
janela.geometry("400x600")

#exemplo de widgets antigo e novo
tk.Label(janela, text="Classico").pack()
ttk.Label(janela, text="Novo").pack()


janela.mainloop()
