
pessoa = {
    "nome": "Eduardo",
    "sobrenome": "Andrade",
    "interesses": ["python", "linux", "docker"]
}

# metodos:
print(f"Retornando somente as chaves: {pessoa.keys()}")
print("-"*30)
print(f"Retornando somente os valores: {pessoa.values()}")
print("-"*30)

# .items retorna chave e valor, otimo para usar com o  for
for chave, valor in pessoa.items():
    print(f"Chave: {chave}, Valor: {valor}")


 # diferenças entre get e setdefault

# get: se a chave existe, retorna o valor;
# se não existe, retorna o valor padrão
print(pessoa.get("idade", "não existe")) 

# setdefault: se a chave existe, retorna o valor;
# se não existe, cria a chave e retorna o valor padrão.
# diferente de get(), setdefault() altera o dicionário.
print(pessoa.setdefault("idade", 0)) 

# setdefault não sobreescreve uuma chave existente
print(pessoa.setdefault("nome", "nome_padrão")) 

# por causa do append essa expressão retorna None.
pessoa.setdefault("interesses", []).append("automação")
# mas se imprimir a lista se verifica que ela foi alterada
print(pessoa["interesses"])

# update atualiza uma chave e criar se não existir
pessoa.update(sobrenome = "Andrade", profissao = "programador")
print(pessoa)

# pop: deleta uma chave e retorna o valor dela
nome_removido = pessoa.pop("nome")
print(f"chave: {nome_removido} deletada")

# delete: remove e retorna o último par chave-valor inserido
deletado = pessoa.popitem()
print(f"item deletado {deletado}")

print("--" * 10)
print(pessoa)


# resumo:
#| Método         | O que faz                                 |
#| -------------- | ----------------------------------------- |
#| `get()`        | Consulta segura                           |
#| `setdefault()` | Consulta e cria se não existir            |
#| `keys()`       | Retorna as chaves                         |
#| `values()`     | Retorna os valores                        |
#| `items()`      | Retorna chave e valor                     |
#| `update()`     | Atualiza ou adiciona chaves               |
#| `pop()`        | Remove uma chave e retorna seu valor      |
#| `popitem()`    | Remove e retorna o último par chave-valor |
#| `del`          | Remove uma chave sem retornar nada        |


