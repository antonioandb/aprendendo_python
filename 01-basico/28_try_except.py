# Em Python existem dois tipos de erros: erros de sintaxe e exceções.
#
# Erro de sintaxe é quando se escreve um código inválido.
#
# Exceções são erros que ocorrem durante a execução do programa,
# por exemplo, tentar ler um arquivo que não existe ou se conectar
# a um servidor offline.
#
# Para lidar com exceções usamos try...except. Colocamos o código
# que pode gerar uma exceção no bloco try e o código que trata a
# exceção no bloco except.

try:
    numero = int(input('digite um numero: '))
    resultado = 10 / numero
    print(f'o resultado é {resultado}')
except ValueError:
    print('voce deve digitar um numero valido')
except ZeroDivisionError:
    print('não é possivel dividir um numero por zero') 


# é possivel capturar o erro em uma variavel
try:
    numero = int(input('Digite um numero aqui: '))
    print(numero)
except ValueError as err:
    print(f'numero invalido, tipo do erro: {err}')

# a exceção deve ser usada para situações excepcionais esperadas, não para esconder erros de programação.