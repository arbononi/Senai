import sys

def limpar_linha(linha = 23, coluna = 3, tamanho = 72):
    posicionarCursor(linha, coluna)
    print(" " * tamanho)
    posicionarCursor(linha, coluna)

def posicionarCursor(linha, coluna):
    sys.stdout.write(f"\033[{linha};{coluna}H")

def exibirMensagem(linha, coluna, mensagem, saltar_linha ="\n"):
    posicionarCursor(linha, coluna)
    print(mensagem, saltar_linha)

def limpar_tela(start, stop, column, size):
    
    for linha in range(start, stop):
        posicionarCursor(linha, column)
        print(" " * size, end="")

def desenhar_tela(linha_inicial, layout):
    for texto in layout:
        posicionarCursor(linha_inicial, 28)
        print(texto, end="")
        linha_inicial += 1
