from os import system as limp

limp("cls")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

soma = sub = mult = div = exp = None

soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
div = valor1 / valor2
exp = valor1 ** valor2

print(f"O resultado das operações desses valores são:")
print(f"O resultado da soma: {valor1} + {valor2} = {soma}")
print(f"O resultado da subtração: {valor1} - {valor2} = {sub}")
print(f"O resultado da multiplicação: {valor1} * {valor2} = {mult}")
print(f"O resultado da divisão: {valor1} / {valor2} = {div}")
print(f"O resultado da exponenciação (potência): {valor1} ** {valor2} = {exp}")