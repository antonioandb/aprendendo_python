# as vezes é preciso criar uma lista apartir de outra como em um mapeamento que é pegar uma lista e gerar outra a partir dela com os itens modificados:
numeros = [1, 2 ,3 ,4 ,5, 6, 7, 8, 9]
dobro = []
for n in numeros:
    dobro.append(n*2)

print(f"lista numeros duplicada",dobro)

# fazendo o mesmo de forma mais elegante com list comprehension
dobro2 = [n * 2 for n in numeros]
print("lista duplicada com list comprehension",dobro2)

# O que está à esquerda do 'for' é o corpo do loop (o valor a ser inserido); 
# os [ ] já criam a lista e inserem os itens, dispensando o uso de .append(). porque o processo já está sendo feito dentro da lista.

# tambem é posivel filtrar usando list comprehension:
numeros_filtrados = [n for n in numeros if n < 5]
print("todos os numeros menores do que 5", numeros_filtrados)

#o que vem na direita do for é mapeamento o que vem na esquerda do for é filtro, [mapeamento for n in variavel filtro]

# list comprehencion em uma lista de produtos
produtos = [
    {"nome": "tv", "preco": 300.0},
    {"nome" : "radio", "preco": 200.0},
    {"nome" : "celular", "preco": 2000.0}
]

novos_produtos = [{**produto, "preco": produto["preco"] * 1.5} for produto in produtos if produto['preco'] < 2000.0]

print(*novos_produtos, sep='\n') 

# cada produto é um dicionario, descompactamos o dicionario para alterar o preco, e depois filtramos para produtos menores dos que 2000.0