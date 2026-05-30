# os operadores logicos são usados para combinar ou inverter expressões booleanas, são eles: and, or, not.

# 1 and (E) exige 100% de verdade para ser verdadeiro, ou seja, ambas as expressões devem ser verdadeiras para que o resultado seja verdadeiro.
ingresso = True
convite = True
if ingresso and convite:
    print("Você pode entrar na festa!")
else:
    print("Desculpe, você não pode entrar na festa !")

# 2 or (OU) exige que apenas uma das expressões seja verdadeira para que o resultado seja verdadeiro então se pelo menos uma das expressões for verdadeira o resultado é verdadeiro.
estudante = False
idoso = True
if estudante or idoso:
    print("Você tem direito a desconto !")

# 3 not (NÃO) é um operador de negação, ele inverte o valor de uma expressão booleana ou seja se a expressão for verdadeira o resultado é falso e vice versa.
chovendo = True
if not chovendo:
    #executado se chovvendo for falso
    print("Vamos sair para passear!")
else:
    #executado se chovendo for verdadeiro
    print("vamos ficar em casa hoje, está chovendo !")

"""
RESUMO DA TABELA VERDADE:
| Operador | Regra Prática                      |
|----------|------------------------------------|
| AND      | os dois devem ser verdadeiros      |
| OR       | se um verdadeiro já basta          |
| NOT      | Do contra (inverte tudo)           |
"""