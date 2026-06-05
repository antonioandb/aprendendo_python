# tuplas são estruturas de dados imutaveis uma vez criadas não podem ser alteradas
# são representadas por parenteses ()
# são usadas para armazenar dados relacionados, como coordenadas, datas, etc

# podem ser criadas com ou sem parenteses, mas é recomendado usar para melhor legibilidade
nomes = ("João", "Maria", "Pedro")
cores = "vermelho", "verde", "azul"
# para acessar os elementos da tupla, usamos o indice começando do 0 assim como nas listas
print(nomes[0]) # João
print(cores[1])# verde

# tupla de um unico valor
tupla_unica = ("Python",) # é necessario a virgula para indicar que é uma tupla
apenas_str = ("Python") # sem virgula é apenas uma srtring
print(type(apenas_str)) # <class 'str'>
print(type(tupla_unica)) # <class 'tuple'>


# tuplas podem ser usadas para desempacotamento de valores
coordenadas = (10, 20)
x, y = coordenadas # desempacotamento
print(f"x: {x}, y: {y}") # x: 10, y: 20

# o fatiamento também funciona em tuplas
print(nomes[0:2]) # (joão, maria)

# conversão de lista para tupla

lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla) # (1, 2, 3)

# garente que os dados não sejam alterados e pode ser usadas como chaves em dicionarios ou elementos de conjuntos.



