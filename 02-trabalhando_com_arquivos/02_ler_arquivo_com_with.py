#with é uma estrutura usada para gerenciar recursos automaticamente arquivos, ele garante que o arquivo será fachedo quando o bloco terminar.

with open('arquivo_texto.txt') as a:
    #conteudo = a.read()
    #linhas = a.readlines()
    linha = a.readline()

print(linha)

# funcões para ler arquivo:
# texto.read(tamanho)
# Lê o conteúdo do arquivo e o retorna como uma string.
# Se 'tamanho' for informado, lê apenas a quantidade de caracteres especificada.
# Sem argumentos, lê todo o restante do arquivo.

# texto.readline()
# Lê e retorna a próxima linha do arquivo como uma string.
# Normalmente inclui o caractere de quebra de linha '\n'.
# Retorna uma string vazia ('') quando o fim do arquivo é alcançado.

# texto.readlines()
# Lê todas as linhas restantes do arquivo e as retorna em uma lista de strings.
# Cada elemento da lista corresponde a uma linha do arquivo.
# Pode consumir muita memória em arquivos grandes.


# forma concisa de ler um arquivo linha por linha
with open('arquivo_texto.txt') as a:
    for linha in a:
        print(linha.strip())




















# texto.read(tamanho)
# Lê o conteúdo do arquivo e o retorna como uma string.
# Se 'tamanho' for informado, lê apenas a quantidade de caracteres especificada.
# Sem argumentos, lê todo o restante do arquivo.

# texto.readline()
# Lê e retorna a próxima linha do arquivo como uma string.
# Normalmente inclui o caractere de quebra de linha '\n'.
# Retorna uma string vazia ('') quando o fim do arquivo é alcançado.

# texto.readlines()
# Lê todas as linhas restantes do arquivo e as retorna em uma lista de strings.
# Cada elemento da lista corresponde a uma linha do arquivo.
# Pode consumir muita memória em arquivos grandes.