# assim como o list comprehension é possivel gerar um set apartir de outro aplicando uma expressão a cada elemento

tags = {'PYHTON', 'KOTLIN', 'JAVA', 'LUA'}
novas_tags = {tag.lower() for tag in tags if tag != 'JAVA'}
print(novas_tags)

# criando um novo conjunto com os elementos em minusculos mas só os que são diferentes de JAVA