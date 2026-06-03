# em Python as listas possuem vários métodos que facilitam sua manipulação.

nomes = ["Alice", "Bob", "Charlie", "David"]

#  append e insert: adicionando itens a lista
nomes.append("Eduardo") # o append adiciona um item no final da lista.
print(nomes)

nomes.insert(1, "Beatriz") # o insert adiciona um item em uma posição especifica da lista, o primeiro parametro é o indice onde o item vai ser adicionado e o segundo parametro é o item que vai ser adicionado.
print(nomes)

# remove e pop: removendo itens da lista
removido = nomes.pop() # o pop remove o ultimo item da lista e retorna ele, aqui estamos armazenando o item removido na variavel removido. tammbem é possivel remover um item especifico pelo indice: nomes.pop(2) isso vai remover o item com indice 2 da lista.
print("Item removido:", removido)
print(nomes)

nomes.remove("Charlie") # o remove remove a primeira ocorrencia do item especifico na lista, aqui estamos removendo o item "Charlie"
print(nomes)

# sort e sorted: ordenando itens da lista
numeros = [5, 2, 9, 1, 3]

ordenados = numeros.sort() # o sort ordena a lista em ordem crescente, ATENÇÃO ele modifica a lista original.
print("lista original ordenada:",numeros)
print("variavel ordenada:",ordenados) # o sort não retorna a lista ordenada, ele retorna None.

# é um erro comum tentar armazenar o resultado do sort em uma variavel como eu fiz aqui, o correto seria apenas chamar o sort sem atribuir a variavel, numeros.sort() e depois imprimir a lista numeros para ver ele ordenada.

# sorted é uma função que retorna uma nova lista ordenada, sem modificar a lista original.
numeros_2 = [5, 2, 9, 1, 3]
numeros_ordenados = sorted(numeros_2)
print("lista original:", numeros_2) # a lista numeros_2 continua desordenada.
print("nova lista ordenada:", numeros_ordenados) # a variavel numeros_ordenados agora tem a lista numeros_2 ordenada, mas a lista numeros_2 continua desordenada.



# buscar a posição de um elemento, se o elemento não existir na lista, o método index gera um ValueError.
posicao_tres = numeros.index(3) # o index retorna o indice da primeira ocorrencia do item especifico na lista, aqui estamos buscando a posição do numero 3 na lista numeros.
print("o index do numero 3:", posicao_tres)
# lembre-se que eu ordennei a lista  numeros com o sort, então a posição do numero 3 é diferente da posição que ele tinha antes de ser ordendo, eu mesmo me confundi com isso 😅.


# len: é uma função global que retorna o numero de itens em uma lista

tamanho = len(numeros) # aqui estamos usando a função len para obter o numero de itens na lista numeros.
print("tamanho da lista numeros:", tamanho)

# clear: limpa todos os itens da lista
numeros.clear() # o clear remove todos os itens da lista, deixando ela vazia.
print("lista numeros após clear:", numeros)


# lembrando que append e sort mexem na lista original o mesmo vale para clear, remove e pop, eles modificam a lista original.