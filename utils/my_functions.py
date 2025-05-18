import sys
import msvcrt

OCULTAR_CURSOR = '\033[?25l'
MOSTRAR_CURSOR = '\033[?25h'

def esperar_tecla(ocultar_cursor: bool=True):
    if ocultar_cursor:
        print(OCULTAR_CURSOR, end="", flush=True)
    tecla = msvcrt.getch().decode("utf-8").upper()
    if ocultar_cursor:
        print(MOSTRAR_CURSOR, end="", flush=True)
    if tecla == "\r":
        tecla = ""
    return tecla

def posicionarCursor(linha: int, coluna: int):
    sys.stdout.write(f"\033[{linha};{coluna}H")

def limpar_linha(lin, col, size):
    posicionarCursor(lin, col)
    print(' ' * size, end='')

def exibir_mensagem(mensagem, lin, col, wait_key=True):
    limpar_linha(lin, col, 77)
    posicionarCursor(lin, col)
    print(mensagem, end='')
    if wait_key:
        tecla = esperar_tecla()
        if tecla == '\r':
            tecla = ''
        return tecla
    return None

def exibir_conteudo(conteudo, lin, col):
    posicionarCursor(lin, col)
    print(conteudo)


