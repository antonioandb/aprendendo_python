# Função com número variável de argumentos
# para quando não sabemos quantos argumentos uma função pode receber podemos usar o *args, ele permite que a função receba um numero variavel de argumantos não nomeados.
# os argumentos passados para a função usando *args são armazenados em uma tupla dentro da função e pode ser iterados como qualque tupla.
def somar(*args):
    total = 0
    for num in args:
        total += num
    return total

soma1 =somar(1, 3, 5) 

print(soma1) # 9

#tupla de numeros
numeros = (2, 4, 6)
soma2 = somar(*numeros) # aqui a tupla numeros é descompactada usando o * e cada elemento da tupla é passado como um argumento separado para a função somar
print(soma2) # 12