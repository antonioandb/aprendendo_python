# iteração é o processo de percorrer os itens de uma coleção como uma lista, tupla ou dicionario. em python a maneira mais comum de iterar sobre uma coleção é usando um loop for.

frutas = ["maçã", "banana", "laranja", "uva"]

# iteração simples, apenas valores 
for fruta in frutas:
    print(fruta)

# iteração com indice e valor usando a função enumerate() que retorna o indice e o value de cada item da coleção.
for indice, fruta in enumerate(frutas):
    print(f"indice: {indice}, fruta: {fruta}")

# o enumerate() entrega uma tupla com indice e valor, então podemos usar a sintaxe de desempacotamento para pegar o indice e o valor em variaveis separadas.

