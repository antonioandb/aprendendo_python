# input é uma função nativa do python que pausa a execução do programa e espera o usuario digitar algo no teclado, quando o usuario digita e aperta enter, o valor digitado é retornado como uma string podendo ser armazenado em uma variavel.
nome = input("Digite seu nome: ")# quando o usuario digitar o nome e apertar enter, o valor digitado será armazenado na variavel como uma string mesmo se o que for digitado for um numero.

idade = input("Digite sua idade: ")


idade = int(idade) # aqui a variavel "idade" que é uma string é convertida para um inteiro para que possamos realizar operações matematicas ou comparações com ela.

#----
# if é uma estrutura condicional, ela faz o python executar um bloco de codigo caso a condição seja verdadeira, e pular esse bloco caso a condição seja falsa, exemplo:

if idade >= 18:# condição: se a idade for maior ou igual a 18
    print("Olá, " + nome + "!")
    print("Você é maior de idade. Bem-vindo!")

# como já dito caso a condição seja falsa ele pula o bloco, mas existe a possibilidade de adicionar um bloco de codigo para ser executado caso a condição seja falsa usando a palavra reservada "else". então ele pula para o else e executa o bloco de codigo associado a ele:
else:
    print("Olá, " + nome + "!")
    print("Você é menor de idade. Desculpe, você não pode navegar nesse site.")



# ELIF é o intermediario entre o if e o else, ele é usado para verificar uma condição adicional caso a primeira condição seja falsa, exemplo:

nota = int(input("Digite sua nota:"))

if nota >= 90:
    print("Parabéns! Você tirou uma nota exelente!")
elif nota >= 60:
    print("Parabéns! Você passou de ano!")
else:
    print("Infelizmente, vocẽ não passou de ano. Estude mais para a próxima vez!")
