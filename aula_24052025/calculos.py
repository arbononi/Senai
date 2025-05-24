import math

def adicao(valores):
    result = None
    for valor in valores:
        if result is None:
            result = valor
        else:
            result += valor
    return result

def subtracao(valores):
    result = None
    for valor in valores:
        if result is None:
            result = valor
        else:
            result -= valor
    return result

def multiplicacao(valores):
    result = None
    for valor in valores:
        if result is None:
            result = valor
        else:
            result *= valor
    return result

def divisao(valores):
    result = None
    for valor in valores:
        if valor == 0:
            continue
        elif result is None:
            result = valor
        else:
            result /= valor
    return result

def divisao(valor1, valor2):
    return valor1 / valor2

def exponenciacao(valores):
    result = None
    for valor in valores:
        if result is None:
            result = valor
        else:
            result **= valor
    return result

def raiz(valores):
    valor = valores[0]
    indice = valores[1]
    if indice == 0:
        indice = 1
    return valor ** (1 / indice)

def seno(valor):
    return math.sin(valor)

def cosseno(valor):
    return math.cos(valor)
