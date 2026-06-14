# associando um retorno função a um widget para interação
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("comandos nos widgets")
janela.geometry("600x400")

# é possivel assciar uma função a um widget que tem a opção command, com isso toda vez que esse evento acontace a função é chamada deixando as coisas mais interativas.
def clicar_mouse():
    print("Botão clicado")

# depois disso é possivel associar a função ao um botão por exemplo com a opção Command, toda vez que ele por pressionado ele vai executar a função.
#o função é pasasda sem () caso contrario ela seria executa imadiatamante, quem deve executar a função é o botão.
botao = ttk.Button(janela, text="me aperte :)", command=clicar_mouse).pack()

# tambem é possivel pasar argumantos para uma função, pra isso é preciso de uma função que aceite argumntos e ele deve ser executada como argumento dentro e uma função lambda no command.
def selecionar(op):
    print(op)

btn1 = ttk.Button(janela, text="Azul", command=lambda: selecionar("Azul")).pack()
btn2 = ttk.Button(janela, text="Vermelho", command=lambda: selecionar("Vermelho")).pack()
btn2 = ttk.Button(janela, text="Verde", command=lambda: selecionar("Verde")).pack()

#Apenas alguns widgets suportam a opção de command


janela.mainloop()
