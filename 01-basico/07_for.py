# o for é outra estrutura de repetição, ele é usado para iterar ou seja percorrer uma sequencia de elemantos, como listas, tuplas, dicionarios é até strings.

# exemplo de for percorrendo uma string:
texto = "python"
for letra in texto: # aqui a variavel letra vai receber cada caractere da string texto a cada iteração do for.
    print(letra)
    
# usando range:
# o range é uma função que gera uma sequencia de numeros em um intervalo especificado, ele é muito usado em conjunto com o for para repetir um bloco de codigo um numero determinado de vezes.
for i in range(5): # aqui o for vai se repetir 5 vazes e a variavel i vai receber os valores de 0 a 4 a cada iteração do for.
    print("Iteração:", i)
    
# for com listas 
frutas = ["maçã", "banana", "uva", "laranja"]

for fruta in frutas:
    if fruta == "uva":
        print("Encontramos a uva !")
        break # o break é uma palavra reservada que serva para sair completamente do loop, ou seja quando a uva for encontrada o for vai ser interrompido.
    print("verificando ... a fruta é uma :", fruta)
    

# pulando um numero

for i in range(10):
    
    if i == 6:
        print("pulando o numero 6")
        continue # o continue é uma palavra resenvada que pula a iteração atual do loop, ou seja quando i for igual a 6 o continue vai fazer com que o for pule para a proxima iteração.
    print("Numero atual:", i)
    
# break e continue são muito usados para controle de fluxo dentro de um loop, o break para sair completamente do loop eo continue para pular uma iteração especifica do loop e continuar com as proximas iterações.        