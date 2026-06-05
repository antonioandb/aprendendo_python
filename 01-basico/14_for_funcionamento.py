# entendendo melhor o funcionamento do for
# ok, o for pode percorrer um objeto iteravel e "pegar" um item por vez, mas para um objeto ser iteravel ele precisa implementer o protocolo de iteração, e pra isso ele precisa ter um metodo cahmado __iter__() que retorna um iterador(iterator), o iterador é um objeto que tem um metodo chamado __next__() que retona o proximo item da coleção e levanta uma exceção StopIteration quando não tem mais itens para retornar.

texto = "Python".__iter__() # chamando o metodo .__iter__() da string "Python" que retorna um iterador.
print(texto) # retorna o objeto <str_ascii_iterator object at 0x7fbe23b4b2b0> que é um iterador de string juntamente  com o endereço de memória.

# o iterator é o elemento que sabe entregar um elemento por vez, e o for é o elemento que sabe usar o iterator para percorrer a coleção.

# chamando o metodo .__next__() do iterator para pegar o proximo item da string "Python".
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
#print(texto.__next__()) # aqui ele levanta a exceção StopIteration porque não tem mais itens para retornar, ou seja, ele já entregou todos os caracteres da string "Python".
# .__next__() tambem pode ser chamado usando a função next() que é uma função interna do python.

# fazendo um "for manual" usando o iterator e a função next() para percorrer a string "Python".
texto = "Python"
iterador = iter(texto) # assim como next() existe a função iter() que chama o metodo .__iter__() do objeto passado como argumento e retorna o iterador.
while True:
    try:
        print(next(iterador)) # aqui ele chama a função next() passando o iterador como argumento, e a função next() chama o metodo .__next__() do iterador para pegar o proximo item da string "Python".
    except StopIteration: # quando o iterador não tem mais itens para retornar ele levanta a exceção StopIteration, então aqui estamos tratando essa exceção para sair do loop quando isso acontecer.
        break

# Ou seja, iter() chama o método __iter__() do objeto e
# next() chama o método __next__() do iterador.
#
# O for é uma estrutura de controle que usa instruções internas
# equivalentes a iter() e next() para percorrer os itens de um
# objeto iterável de forma eficiente e elegante.

# observação: o nome do objeto é iterator mas normalmente é traduzido como iterador em portugues. :)