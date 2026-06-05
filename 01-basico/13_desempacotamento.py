# desempacotamento de listas é uma tecnica que permite atribuir os itens de uma lista a variaveis separadas usando a sintaxe: variavel1, variavel2, variavel3 = lista

nomes = ["Alice", "Bob", "Charlie"]
# para desempacotar os itens da lista nomes em variaveis separadas, podemos usar a sintaxe de desempacotamento:
nome1, nome2, nome3 = nomes
print(nome1) # Alice
print(nome2) # Bob
print(nome3) # Charlie

# se a lista tiver mais itens do que variaveis podemos usar o operador * para pegar o resto dos itens da lista em uma variavel.
primeiro, *resto = nomes
print(primeiro) # Alice
print(resto) # ['Bob', 'Charlie']
# resto é uma lista com os itens restantes da lista nomes.

# omitindo valores:
_, nome2, _ = nomes # o _ é uma convenção para indicar que a variavel não será usada, ou seja estamos omitindo os valores de nome1 e nome3 e pegando apenas o valor de nome2.
print(nome2) # Bob
