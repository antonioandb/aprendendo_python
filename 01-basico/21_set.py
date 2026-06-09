# set é um conjunto que não permite repetições, ele não pussuem inices a posição na memoria é arbitrária.
# por causa diso ele não suporta fatiamento e acesso por posição [].

frutas = {"banana", "maçã", "laranja", "abacate"}
print(frutas)

# metodos principais:

# len: retorna o tamanho do set
print(len(frutas))

# add: adiciona um elemento
frutas.add("limão")
print(frutas)

# update: atualiza, pode inserir multiplos elementos iteraveis de uma vez como listas ou dicionarios
frutas.update({"uva", "pesego"})
print(frutas)

# discard: remove um item se ele existir, não gera um erro caso o contrario
frutas.discard("uva")
print(frutas)

# remove: seelhante ao discard as gera erro caso o item não existir.
#frutas.remove("uva") gerou um erro
frutas.remove("limão")
print(frutas)

# pop: diferente da lista um set não possui ordem, por isso o pop retorna o ultimo elemento e remove ele mas ele é arbitrario.
pop = frutas.pop()
print(f"pop: {pop}")

# clear: faz a limpeza do set removeno tudo
frutas.clear()
print(frutas)

# copy: retorna uma cópia do set
copy = frutas.copy()
print(copy)

# OPERAÇÕES MATEMÁTICAS (ÁLGEBRA DE CONJUNTOS)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# UNIÂO (union): retorna um novo set com todos os elementos de ambos os sets (sem repetições), lembrando que não é necessario que os sets tenham o mesmo tamanho
união = set1.union(set2)
print(f"união: {união}")

# tambem é possivel usar o operador | (pipe)
união = set1 | set2 

# INTERSECÇÂO (intersection): retorna um novo set apenas com os elementos que estão em ambos os sets
intersecção = set1.intersection(set2) 
print(f"intersecção: {intersecção}")

# tabem é possivel usar o operador & (ampersand)
intersecção = set1 & set2

# DIFÊNCIA (difference): retorna um novo set com os elementos que estão no primeiro set e não no segundo set
diferença = set1.difference(set2)
print(f"diferença: {diferença}")

# tabem é possivel usar o operador - (minus)
diferença = set1 - set2

# SYMMETRIC DIFFERENCE (symmetric_difference): retorna um novo set com os elementos que estão em um ou outro, mas não em ambos
diferente = set1.symmetric_difference(set2)
print(f"diferente: {diferente}")

# tabem é possivel usar o operador ^ (caret)
diferente = set1 ^ set2 



# removendo elementos repetidos e uma lista
lista = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10]

# removendo elementos repetidos
sem_repetidos = list(set(lista))
print(f"sem_repetidos: {sem_repetidos}")


# verificações com in em set costuma ser muito rápida
funcionarios = {"Eduardo", "Ricardo", "Maria", "João", "Fernanda", "gomes"}

if "Eduardo in funcionarios":
    print(f"Funcionario {'Eduardo'} encontrado, dê um aumento para ele :)")