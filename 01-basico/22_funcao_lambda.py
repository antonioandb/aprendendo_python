# função lambda é uma função anônima, ela não precisa de () nem das palavras reservadas def e return, uma função lambda já retorna automaticamente o valor.

# sintaxe lambada:  lambda parametros: expressão

# comparação com uma função normal:
def somar(a ,b):
    return a + b

print(somar(1, 2))

# com a função lambda:
subtrair = lambda a, b: a - b

print(subtrair(1, 2))


# exeplo de uso
# criar uma função que executa outras funções
def executar(funcao, *args):
    return funcao(*args)

# executando a função somar criada anteriormente
print(executar(somar, 1, 2))

# com lambda: executando uma função lambda que acaba de ser criada em uma unica linha
print(executar(lambda a, b: a * b, 2, 3))
