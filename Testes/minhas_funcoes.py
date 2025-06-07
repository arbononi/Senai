def somar(valor1, valor2):
    if not isinstance(valor1, (int,float)) or not isinstance(valor2, (int, float)):
        raise TypeError("Ambas as entradas devem ser números")
    return valor1 + valor2

def subtrair(valor1, valor2):
    if not isinstance(valor1, (int,float)) or not isinstance(valor2, (int, float)):
        raise TypeError("Ambas as entradas devem ser números")
    return valor1 - valor2

def dividir(dividendo, divisor):
    if not isinstance(dividendo, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Ambas as entradas devem ser números")
    if divisor == 0:
        raise ZeroDivisionError(f"Não é possível dividir {dividendo} por {divisor} quando divisor for zero!")
    return dividendo / divisor
    
def multiplicar(multiplicando, multiplicador):
    if not isinstance(multiplicando, (int, float)) or not isinstance(multiplicador, (int, float)):
        raise TypeError("Ambas as entradas devem ser números")
    return multiplicando * multiplicador
