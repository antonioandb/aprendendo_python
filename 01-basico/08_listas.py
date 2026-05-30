# uma lista armazena uma coleção de itens em uma variavel, ela é mutavel ou seja podemos alterar os itens da lista depois de criada, ela é organizada ou seja os itens da lista tem uma ordem e cada item tem um indice que começa em 0.

# criando uma lista
frutas = ["banana", "maçã", "uva", "laranja", "abacaxi"] # aqui criamos uma lista de frutas com 5 itens.

# indices:               0        1       2       3          4
#valores: # frutas = ["banana", "maçã", "uva", "laranja", "abacaxi"]

# acessando itens da lista
print(frutas[0]) # aqui estamos acessando o item com indice 0 da lista, que é a banana.
print(frutas[2]) # aqui estamos acessando o item com indice 2 da lista, que é a uva.

# MUTABILIDADE: fazendo um indice apontar para outro valor.
frutas[1] = "morango" # aqui estamos alterando o item com indice 1 da lista, que era a maçã, para morango.
print(frutas)

# MATRIZES: uma lista pode conter outras listas, dá para maginar como coordenadas: [linha][coluna] ou seja a primeira lista é a linha e a segunda lista é a coluna.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0]) # aqui estamos acessando a primeira linha da matriz, que é a lista [1, 2, 3].
print(matriz[1][2]) # aqui estamos acessando o item com indice 2 da segunda linha da matriz que é o numero 6.