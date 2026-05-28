# uma variavel é um nome que funciona como uma atiqueta para valores literais armazenados na memoria fisica do computador.
# uma variavel não guarda o valor em sí, ela funciona como uma referencia para o valor armazenado na memoria, quando criamos uma variavel e atribuimos um valor a ela o python cria um espaço na memoria para armazenar esse valor e associa esse espaço a variavel, é como se a variavel fosse o dedo que aponta para o valor armazenado na memoria, e quando acessamos a variavel o python vai até a mamoria e recurera o valor associado a ela.

# para criar uma variavel em python basta escolher um nome para ela e usar o operador de atribuição "=" para associar um valor.
nome = "Antonio" # aqui uma variavel é criada com o nome "nome" e associada ao valor "Antonio", então quando acessamos a variavel "nome" o python vai até a memoria e recupera o valor "Antonio".

idade = 30 # aqui uma variavel é criada com o nome "idade" e associada ao valor 30, então quando acessamos a variavel "idade" o python vai até a memoria e recupera o valor 30.

# uma variavel não se importa com o tipo de dado que está associado a ela, ela apenas aponta para o endereço de memoria onde o valor está armazenado, isso quer dizer que uma variavel pode apontar para valores de diferentes tipos de dados ao longo do tempo, por exemplo:
variavel = "Olá" # aqui a variavel "variavel" aponta para o valor "Olá" que é do tipo string.
variavel = 42 # aqui a mesma variavel "variavel" agora aponta para o valor 42 que é do tipo inteiro.

# nesse caso o valor "olá" fica sozinho na memoria sem ninguem apontar para ele, quando isso acontece o python usa um processo chamado Garbage Collector (Coletor de Lixo) para liberar a memoria ocupada por valores que não estão mais sendo referenciados por uma variavel.

#isso é posivel porque o python é uma linguagem de tipagem dinamica, ou seja o tipo de dado associado a uma variavel pode mudar durante a execução do programa. o tipo está no valor e não na variavel.

# recuperando o valor de uma variavel basta usar o nome da variavel, por exemplo:
print(nome) # aqui o python vai até a memoria e recupera o valor associado a variavel "nome" e imprime "Antonio".
print(idade) # a mesma coisa acontece aqui, o python recurera o valor da memoria associado a variavel.


# tambem é possivel guardar operações matematicas em variaveis.
ano_de_nascimento = 1990
ano_atual = 2026
idade_calculada = ano_atual - ano_de_nascimento # aqui a variavel "idade_calculada" guarda o resultado da operação matematica, que é 36.

print(idade_calculada) # aqui o python vai até a memoria e recupera o valor associado a variavel "idade_calculada" e imprime 36.