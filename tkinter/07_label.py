import tkinter as tk
from tkinter import ttk

#configura janela
janela = tk.Tk()
janela.geometry('400x600')
janela.title('widget Label')

# label exibe um texto ou imagem na tela
label = ttk.Label(janela, text='Exibindo Texto')# criando uma instancia de Label
label.pack()# colaca o label na janela principal

#para laterar a font se usa um argumento de palavra chave chamado font 
label2 = ttk.Label(
    janela,
    text= 'texto grande',
    font=("Helvetica", 16)
    )
label2.pack()

# para usar uma imagem na label se usa outro widget Chamado photoImage, e com o parametro image do label a imagem é inserida dentro do label, o perametro compound controla como o texto e a imagem vão dividor espaço.
imagem = tk.PhotoImage(file='assets/python.png')
label3 = ttk.Label(
    janela,
    image = imagem,
    text='Python',
    padding=5,
    compound=tk.TOP
)
#Valorres do compound, e O que ele faz?
#tk.TOP,Coloca a imagem acima do texto.
#tk.BOTTOM,Coloca a imagem abaixo do texto.
#tk.LEFT,Coloca a imagem à esquerda do texto (muito usado em botões com ícones).
#tk.RIGHT,Coloca a imagem à direita do texto.
#tk.CENTER,"Coloca a imagem no centro, fazendo o texto ficar escrito em cima da imagem (como se a imagem fosse um fundo)."

label3.pack()

janela.mainloop()