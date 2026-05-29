# while é uma estrutura de repetição, ele é como um if teimoso que repete o bloco de codigo associado a ele enquanto a condição for verdadeira.

contador = 0 # aqui criamos uma variavel contador para controlar quantas vezes o bloco de codigo vai ser executado.
while contador < 5: # aqui a condição é que o contador seja menor que 5, enquanto isso for verdadeiro o while executa o bloco.
    print("Contador:", contador)
    contador += 1 # para evitar um loop infinito é importante atualizar a variavel contador dentro do bloco.

    # o while é ultil para quando não sabemos quantas vezes o bloco de codigo precisa ser executado.

    # repetição determinada:
senha = "1234"
tentativa = ""
while tentativa != senha: # enquanto a tentativa for diferente da senha o bloco vai se repetir.
    tentativa = input("Digite a senha: ")
    # verificando se a senha digitada está errada
    if tentativa != senha:
        print("Senha incorreta, tente novamente.")
        
print("Senha correta, bem-vindo !")# como ele saiu do loop while isso significa que a tentativa é igual a senha, então o usuario digitou a senha correta.


# aqui o while vai se repetir até que o usuario digite a senha correta, e como não sabemos quantas tentativas o usuario vai precisar para acertar a senha o while é a estrutura de repetição ideal para esse caso.