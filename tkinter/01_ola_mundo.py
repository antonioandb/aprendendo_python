#importando tkinter
import tkinter as tk

#criando uma instancia Tk que vai criar a janela
janela = tk.Tk()

#metodo do objeto que define o titulo da janela
janela.title("Olá Mundo!")

#metodo geometry que define o tamanho da janela 
janela.geometry("400x600")

#evitar que a janela seja redimensionada resizable(largura, altura)
janela.resizable(False, False)

#metodo que definem o tamanho padrão da janela: minsize, maxsize
janela.minsize(200,400)
janela.maxsize(400, 600)

#O método attributes() aceita pares de argumentos: janela.attributes(opcao, valor)
# tranparencia
janela.attributes("-alpha", 0.5)
#"-alpha" → qual atributo você quer alterar
#0.5 → valor desse atributo

#manter a janela na frente
janela.attributes("-topmost", True)
#"-topmost" → manter a janela na frente
#True → ativado

#alterando o icone padrão (apenas no windows)
#janela.iconbitmap('./assets/pythontutorial.ico')

#alterando icone padrão unix, em algumas interface graficas pode não aparecer
try:
    icone = tk.PhotoImage("assets/oculos-nerd.png")# png ou gif
    janela.iconphoto(True, icone)
except tk.TclError:
    print("icone não encontrado.")

#consultando um valor atual com print
print(janela.attributes("-alpha"))
# loop, sem isso a janela abre e fecha rapidamente
janela.mainloop()