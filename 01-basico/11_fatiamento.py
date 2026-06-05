# fatiamento em listas é uma tecnica que permite acessar uma parte especifica da lista usando uma sintaxe especial. [inicio:fim:passo]
# temos a lista
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# para acessar os itens da lista usamos o indice por exemplo, numeros[0] retorna o primeiro item , numero[1] retona o segundo item e assim vai. mas para acessar uma parte especifica da lista podemos usar o fatiamento exemplo, numeros[2:5] retorna os itens do indice 2 até o indice 4.
print(numeros[2:5])
# sintaxe: [inicio:fim:passo]
# inicio é o indice onde começa o fatiamento, se não for especificodo ele começa do indice 0.
# fim é o indice onde termina o fatiamento, se não for especificado ele termina no ultimo indice da lista.
# passo é o numero de itens que serão pulados entre os itens do fatiamneto, se não for especificado ele é 1 ou seja ele retorna todos os itens entre o inicio e o fim.
# exemplo de fatiamento com passo:
print(numeros[0:10:2]) # começao no indice 0 termina no 9 pulando de 2 em 2, ou seja ele está retornando os numeros pares da lista.
print(numeros[1:10:2]) # começao no indice 1 termina no 9 pulando de 2 em 2, ou seja ele está retornando os numeros impares da lista.

# omitindo o inicio e o fim:
print(numeros[:5]) # omitindo o inicio ele comaça do indice 0 e termina no indice 4, ou seja ele retorna os 5 primeiros itens da lista.
print(numeros[5:]) # omitindo o fim ele começa no indice 5 e termina no ultimo indice da lista, ou seja ele retorna os itens a partir do indice 5 até o final da lista.
print(numeros[::3]) # omitindo o inicio e o fim, ele retorna os itens da lista pulando de 3 em 3.