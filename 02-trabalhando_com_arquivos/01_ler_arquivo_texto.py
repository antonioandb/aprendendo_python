# a função open() é usado para ler um arquivo, ela retorna um objeto iteravel que representa as linhas do texto do arquivo.
texto = open('arquivo_texto.txt')

# o objeto retornado é um iterator por isso é possivel extrair as linhas do texto manualmente.
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
# quando as linhas se esgotarem o iterator fica vazio

#porém a melhor maneira de ler um arquivo aberto é usando os metodos read(), readline() e readlines().

  
# é importante fechar o arquivo aberto que não está mais em uso
texto.close()






