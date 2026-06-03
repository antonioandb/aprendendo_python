# extend() é um metodo de lista que adiciona os itens de uma lista em outra lista.

# temos a lista
nomes = ["Alice", "Bob", "Charlie", "David"]
# e queremos adicionar os itens de outra lista
novos_nomes = ["Eduardo", "Beatriz"]
# podemos usar o extend para adicionar os itens de novos_nomes na lista nomes
nomes.extend(novos_nomes) # o extend adiciona os itens de novos_nomes na lista nomes, ele modifica a lista nomes, adicionando os itens de novos_nomes no final.
print(nomes)

# -- comparação com append:
nomes.append(["Fernando", "Gabriela"]) # o append adiciona a lista ["Fernando", "Gabriela"] como um unico item no final da lista nomes, ou seja, ele adiciona a lista inteira como um item.
print(nomes)

# count() conta quantas vezes um item aparece na lista
quantidade_de_Eduardo = nomes.count("Eduardo") # conta quantas vezes o nome Eduardo aparece na liast nomes, aqui ele vai contar 1 e está armazenando o resultado em uma variavel.
print("quantidade de Eduardo na lista nomes:", quantidade_de_Eduardo)


# --reverse() inverte a ordem dos itens da lista original, ele modifica a lista original.
nomes.reverse() # o reverse inverte a ordem dos itens da lista nomes.
print("lista nomes invertida:", nomes)

# -- copy() cria uma copia da lista e retorna essa copia.
copia_nomes = nomes.copy()
print("copia da lista nomes:", copia_nomes)

# isso é ultil porque em python copia = nomes não cria uma  copia da lista nomes, ele apenas aponta para a mesma lista na memoria e qualquer modificação feita em copia vai afetar a lista nomes e vice versa.

# -- coisas interessantes que não são metodos:

# concatenar listas:
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_concatenada = lista_1 + lista_2 # o operador + concatena as listas, ele cria uma nova lista que é a concatenação de lista_1 e lista_2.

# repetir itens:
zeros = [0] * 5 # operador * repete os itens da lista.
print(zeros)

# -- in verifica se existe
if 4 in lista_2:
    print("o numero 4 está na lista_2")