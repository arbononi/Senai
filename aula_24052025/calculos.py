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

def exponenciacao(valores):
    result = None
    for valor in valores:
        if result is None:
            result = valor
        else:
            result **= valor
    return result

