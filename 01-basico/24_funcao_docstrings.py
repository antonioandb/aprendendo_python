# python tem uma função chamada help() para mostrar a documentação de uma função, é possivel usar ele para mostrar a documentação de módulos, classes, funções e palavras-chave.

#print(help(print))# documentação do print

# é possivel criar uma documentoação em uma funcão com uma string na primeiro linha dela, o python reconhece isso como uma docstring:
#def soma(a, b):
#    "soma e retorna dois parametros"
#    return a + b


#print(help(soma))

# para usar uma docstring em varias linhas se usa """ """

def multiplica(a, b):
    """
    recebe dois argumentos:
    a: um inteiro
    b: um inteiro
    retorna:
     int: resultado da multiplicação

    """
    return a * b

#print(help(multiplica))

# o python armazena as documentação em .__doc__

print(multiplica.__doc__)