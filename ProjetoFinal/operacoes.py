import math

def verificar_operacoes(operacao:int, valor1, valor2=0):
    match operacao:
        case 1:
            result = soma(valor1, valor2)
        case 2:
            result = sub(valor1, valor2)
        case 3:
            result = mult(valor1, valor2)
        case 4:
            result = div(valor1, valor2)
        case 5:
            result = expoente(valor1, valor2)
        case 6:
            result = raiz(valor1, valor2)
        case 7:
            result = seno(valor1)
        case 8:
            result = cosseno(valor1)
        case 9:
            result = tangente(valor1)
    
    return result

#P101 - Autor: Viviane
# "Criar função que soma as variaveis"
# Revisor - Natha

def soma(numero1,numero2):
    res = numero1 + numero2
    return res

#P102 - Autor: Felipe Sponchiado
# "Criar função que subtrai as variaveis"
# Revisor - André Bononi
def sub( numero1, numero2):
    res = numero1 - numero2
    return res

#P104 - Autor: Vitor Lucas
# "Criar função que multiplica as variveis"
# Revisor - Nathan
def mult(num1, num2):
    result = num1 * num2
    return result

def div(valor1, valor2):
    if valor2 == 0:
        return "Erro: divisão por zero"
    res = valor1/valor2
    return res

#P106 - Autor: Vitor M
# "Criar função que eleva a um numero"
# Revisor - André Bononi
def expoente(valor1, valor2):
    res = valor1 ** valor2
    return res

#P105 - Autor: Felipe
# "Criar função que extrai a raiz da variavel"
# Revisor - Nathan
def raiz(valor1, valor2):
    if valor2 == 0:
        return "Erro: divisão por zero"
    res = valor1**(1/valor2)
    return res

#P107 - Autor: Heron
# "Criar função que extrai seno, o cosseno e tangente"
# Revisor - Nathan
def seno(valor):
    return math.sin(valor)

def cosseno(valor):
    return math.cos(valor)

def tangente(valor):
    return math.tan(valor)

       
         
        