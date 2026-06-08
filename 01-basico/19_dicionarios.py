# dicionários são estruturas de dados que armazenam pares de chave e valor.
# As chaves funcionam como uma espécie de índice personalizado.
# "chave": "valor"
pessoa = {
    "nome": "Antonio",
    "sobrenome": "Barros",
    "idade": 36,
    "enderecos": [
        {"rua": "vitoria", "numero": 111},
        {"rua": "dos ventos", "numero": 152},
    ],
}

print(pessoa)

# manipulando dicionarios:

# capturando os vaores apertir das chaves que funcionan como os indices da lista.
print(f"Nome: {pessoa['nome']}, dade: {pessoa['idade']}")

# cria ou atualiza ua chave.
pessoa["cidade"] = "Rj" 

# maneira de capturar o valor de uma chave de forma segura, para quando não se tem certeza se a cahve existe.
nome = pessoa.get("nome", "não existir") 
profissao = pessoa.get("profisao", "nao existe")# retorna a mensagem "nao existe" se a chave não existir

print(nome)
print(profissao)

# deleta uma chave.
del pessoa["sobrenome"]
print(pessoa)

# acessando os dados alinahdos
print("rua:", pessoa["enderecos"][0]["rua"]) # no indice 0 da lista endereços tem um dicionario co a chave rua
print("rua: ", pessoa["enderecos"][1]["rua"])