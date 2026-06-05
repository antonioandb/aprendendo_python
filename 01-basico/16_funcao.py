# função é um bloco de codigo reutilizavel que realiza uma tarefa especifica
# pode receber argumentos de entrada e retornar um valor de saida.

def saudar(nome, idade):
    print(f"Olá {nome}, você tem {idade} anos.")


saudar("Antonio", 30) # aqui a função é chamada com os argumentos "Antonio" e 30. ela irá imprimir "Olá Antonio, você tem 30 anos.", mas nesse caso ela não retorna nenhum valor apenas imprime a mensagem na tela.

# o returno é o "produto final" da função, é o valor que ela retorna para quem a chamou, se a função não tiver um return ele retorna None por padrão.
def somar(a, b):
    return a + b

resultado = somar(5, 3) # aqui a função é chamada com os argumentos, diferente do exemplo anterior ela retorna um valor e esse valor é armazenado em uma variavel.
print(resultado) # 8

# valor padrão para argumentos
def conexao(ip, porta=8080):
    print(f"Conectando ao {ip} na porta {porta}.")

conexao("192.168.0.1")# aqui a função é chamada apenas com o argumento ip, o argumento porta irá usar o valor padrão 8080

# uma função deve fazer apenas uma coisa bem feita, se ela fizer muitas coisas pode se tornar dificil de entender e manter.
