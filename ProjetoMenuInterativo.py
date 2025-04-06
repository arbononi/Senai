import os
import msvcrt
from time import sleep as s

opcoes = ["Iniciar", "Configurações", "Sair"]
indice_selecionado = 0

def limpar_tela():
    os.system('cls')

def exibir_menu():
    limpar_tela()
    print("Use ↑ ↓ para navegar, Enter para selecionar:\n")
    for i, opcao in enumerate(opcoes):
        if i == indice_selecionado:
            print(f"> \033[7m{opcao}\033[0m")  # destaque com ANSI
        else:
            print(f"  {opcao}")

def ler_tecla():
    tecla = msvcrt.getch()
    if tecla == b'\xe0':  # prefixo para teclas especiais (setas, etc.)
        tecla = msvcrt.getch()
        return tecla
    return tecla

while True:
    exibir_menu()
    tecla = ler_tecla()
    if tecla == b'H':  # seta para cima
        indice_selecionado = (indice_selecionado - 1) % len(opcoes)
    elif tecla == b'P':  # seta para baixo
        indice_selecionado = (indice_selecionado + 1) % len(opcoes)
    elif tecla == b'\r':  # Enter
        limpar_tela()
        print(f"Você escolheu: {opcoes[indice_selecionado]}")
        s(1)
        if (indice_selecionado == 2):
            break
    