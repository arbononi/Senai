import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.my_functions import *

def testar_valueError(lin, col, size):
    while True:
        try:
            limpar_linha(lin, col, size)
            posicionarCursor(lin, col)
            valor = int(input('Digite um valor: '))
            return valor, None
        except ValueError as ex:
            return None, ex
        
def testar_divisao_por_zero(lin, col, size):
    try:
        limpar_linha(lin, col, size)
        exibir_mensagem("Vou tentar dividir 10 por 0", lin, col, wait_key=True)
        result = 100 / 0
    except ZeroDivisionError as ex:
        return ex
