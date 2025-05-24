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

def posicionarCursor(lin: int, col: int):
    sys.stdout.write(f"\033[{lin};{col}H")

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

def desenhar_tela(layout, start_loop=0, end_loop=0):
    for info in layout:
        if start_loop > 0 and info["lin"] == start_loop:
            lin = info["lin"]
            while lin < end_loop:
                exibir_conteudo(info["value"], lin, info["col"])
                lin += 1
        else:
            exibir_conteudo(info["value"], info["lin"], info["col"])

