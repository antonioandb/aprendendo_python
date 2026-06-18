# finally é um bloco opcional que sempre é executado, independentemente de uma exceção ter ocorrido ou não.


try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
    
except ZeroDivisionError as err:
    # executa se der erro de divasão por zero
    print(f'Divisão por zero não é possível. Erro: {err}')

except ValueError as err:
    # executa se der erro de tipo
    print(f'O valor digitado é inválido. Erro: {err}')

else:
    # else executa apenas se não der erro
    print(resultado)
    
finally:
    print('Execução acabou.')

# O bloco finally é normalmente usado para liberar recursos
# que precisam ser fechados independentemente de erros.
# Por exemplo: fechar arquivos, conexões de banco de dados
# ou conexões de rede.

