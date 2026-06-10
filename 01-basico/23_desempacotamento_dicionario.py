# gererando dois dicionarios
pessoa = {"nome": "Antonio", "sobrenome": "Barros"}
dados_pessoais = {"idade": 30, "profissão": "programador"}

# dempacotando os dois dicionarios em um só e adicionando novas chaves.
pessoa_completa = {
    **pessoa, 
    **dados_pessoais,
    "interesses": ["python", "linux", "docker"]
    }
print(pessoa_completa)

# o operador ** desempacota ou espalha chave e valor de um dicionario e adiciona eles ao outro, se existir chaves repetidas ele serão sobreescritos.
# diferente de * que desepacota ou espalha elemento de sequencia (listas, tuplas, etc). 

# # kwargs = keyword arguments (argumentos nomeados)
# com kwargs a função pode receber chave e valor via argumentos nomeados
def mostrar_argumentos(*args, **kwargs):
    # não nomeados vão para args
    for arg in args:
        print(arg)
    # nomeados vão para kwargs
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
#args recebe os argumentos posicionais extras em uma tupla
#kwargs recebe os argumentos nomeados extras em um dicionário

# mostrar pessoa_completa
mostrar_argumentos(**pessoa_completa)


# exemplo, desempacotar um dicionario grande em uma função

configuracoes = {
    "placa_mae": "ASUS TUF Gaming B550M",
    "processador": "AMD Ryzen 5 5600X",
    "memoria": "16 GB DDR4 3200MHz",
    "placa_de_video": "NVIDIA RTX 3060 12GB",
    "armazenamento": "SSD 1TB NVMe",
    "monitor": "LG 24'' 144Hz Full HD",
    "fonte": "Corsair 650W 80 Plus Bronze",
    "gabinete": "Cooler Master Q300L",
    "sistema": "Windows 11",
}

mostrar_argumentos(**configuracoes)