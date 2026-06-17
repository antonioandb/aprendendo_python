import tkinter as tk

# Inicialização da janela principal
janela = tk.Tk()
janela.geometry('400x600')
janela.title('Vinculando Funções')


def ao_apertar_enter(event):
    """Esta função executa toda vez que o usuário aperta a tecla Enter."""
    print(event)

# O mecanismo de vinculação de eventos (bind) atribui a função ao widget,
# fazendo com que ela execute quando o evento '<Return>' acontecer.
btn = tk.Button(janela, text="aperte enter para executar o evento")
btn.bind('<Return>', ao_apertar_enter)

btn.focus()  # Dá o foco do teclado para o botão ao iniciar
btn.pack(expand=True)

janela.mainloop()