# isinstance e uma funcão que checa se o objeto é uma instancia de uma classe especifica e retorna True ou False
lista = ["a", 22, 40.5, [1,2,3], {"nome" : "Antonio"}, (1,2,3), {1,2}]

for item in lista:
    if isinstance(item, str):
        print(item.upper())

    if isinstance(item, (int, float)):
        print(item * 2)

    if isinstance(item, list):
        item.append("isso é uma lista")
        print(item)

    if isinstance(item, set):
        item.add("isso é um set")
        print(item)

    if isinstance(item, tuple):
        print("isso é uma tupla")
        print(item)

    if isinstance(item, dict):
        item.update(sobrenome="barros")
        print(item)