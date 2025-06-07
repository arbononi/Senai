from os import system
from minhas_funcoes import *


system('cls')
print("Bem-vindo à calculadora do SENAI!")

try:
    resultado_soma = somar(10, 5)
    print(f'O resultado da soma 10 + 5 é: {resultado_soma}')
except Exception as ex:
    print(ex)

try:
    resultado_sub = subtrair(10, 5)
    print(f'O resultado da subtracao 10 - 5 é: {resultado_sub}')
except Exception as ex:
    print(ex)

try:
    resultado_div = dividir(10, 5)
    print(f'O resultado da divisão de 10 por 2 é: {resultado_div}')
    resultado_div_neg = dividir(10, -2)
    print(f'O resultado da divisão de 10 por -2 é: {resultado_div_neg}')
    resultado_div0 = dividir(5, 0)
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)

try:
    resultado_mult = multiplicar(10, 2)
    print(f'O resultado da multiplicação de 10 por 2 é: {resultado_mult}')
except Exception as ex1:
    print(ex1)

print('\nPrograma finalizado')