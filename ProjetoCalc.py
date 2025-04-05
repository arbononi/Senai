from os import system as limp

limp("cls")

valor1 = 50
valor2 = 10
soma = None
sub = None
mult = None
div = None
exp = None

soma = valor1 + valor2
sub = valor1 - valor1
mult = valor1 * valor2
div = valor1 / valor2
exp = valor1 ** valor2

print(f"O resultado das operações desses valores são:")
print(f"Soma: {valor1} + {valor2} = {soma}")
print(f"Subtração: {valor1} - {valor2} = {sub}")
print(f"Multiplicação: {valor1} * {valor2} = {mult}")
print(f"Divisão: {valor1} / {valor2} = {div}")
print(f"Exponenciação (Potência): {valor1} ** {valor2} = {exp}")


