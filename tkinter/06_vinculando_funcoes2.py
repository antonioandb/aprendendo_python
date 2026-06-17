import tkinter as tk

# Inicialização da janela principal
janela = tk.Tk()
janela.geometry('400x600')
janela.title('Vinculando Funções')


def ao_apertar_enter(event):
    """Esta função executa toda vez que o usuário aperta a tecla Enter."""
    print("enter pressionado")

def log(event):
    
    print(event)

# vinculando mais de uma função ao um widget, quando se usa mais de um bind em um widget a segunda função sobreescreve a primeira por isso é preciso usar o parametro add='+' 
btn = tk.Button(janela, text="aperte enter para executar o evento")
btn.bind('<Return>', ao_apertar_enter)
btn.bind('<Return>', log, add='+')

btn.focus()  # Dá o foco do teclado para o botão ao iniciar
btn.pack(expand=True)

janela.mainloop()