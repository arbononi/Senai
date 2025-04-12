#╔═══════════════════════════════════════════════════════════════════════════╗
#║                           *** CAFÉ'S SENAI ***                            ║
#╠═════════════════════════════════════╦═════════════════════════════════════╣
#║                                     ║                                     ║
#║ 1 - CAFÉ EXPRESSO                   ║                                     ║
#║ 2 - CAFÉ COM LEITE                  ║                                     ║
#║ 3 - CAPPUCCINO                      ║                                     ║
#║ 4 - ÁGUA QUENTE                     ║                                     ║
#║ 5 - LEITE PURO                      ║                                     ║
#║ 6 - BALANÇAR A FUMAÇA               ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║ 9 - DESLIGAR                        ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║ ESCOLHA UMA DAS BEBIDAS ACIMA: [ ]  ║                                     ║
#╠═════════════════════════════════════╩═════════════════════════════════════╣
#║                                                                           ║
#╚═══════════════════════════════════════════════════════════════════════════╝

import sys
from os import system as limp
from PIL import Image
from time import sleep as s

# ANSI colors
RESET = "\033[0m"
COR_DO_EXPRESSO = "\033[38;2;75;46;43m"
COR_DO_PINGADO = "\033[38;2;205;140;70m"
COR_DO_CAPPUCCINO = "\033[38;2;193;154;107m"
COR_DA_AGUA = "\033[38;2;173;216;230m"
COR_DO_LEITE = "\033[38;2;255;255;255m"

cores_do_liquido = [
    COR_DO_EXPRESSO,
    COR_DO_PINGADO,
    COR_DO_CAPPUCCINO,
    COR_DA_AGUA,
    COR_DO_LEITE
]

minha_tela = [
    "╔═══════════════════════════════════════════════════════════════════════════╗",
    "║                           *** CAFÉ'S SENAI ***                            ║",
    "╠═════════════════════════════════════╦═════════════════════════════════════╣",
    "║                                     ║                                     ║",
    "║ 1 - CAFÉ EXPRESSO                   ║                                     ║",
    "║ 2 - CAFÉ COM LEITE                  ║                                     ║",
    "║ 3 - CAPPUCCINO                      ║                                     ║",
    "║ 4 - ÁGUA QUENTE                     ║                                     ║",
    "║ 5 - LEITE PURO                      ║                                     ║",
    "║ 6 - BALANÇAR A FUMAÇA               ║                                     ║",
    "║                                     ║                                     ║",
    "║                                     ║                                     ║",
    "║                                     ║                                     ║",
    "║                                     ║                                     ║",
    "║                                     ║                                     ║",
    "║                                     ║                                     ║",
    "║                                     ║                                     ║",
    "║ 9 - DESLIGAR                        ║                                     ║",
    "║                                     ║                                     ║",
    "║                                     ║                                     ║",
    "║ ESCOLHA UMA DAS BEBIDAS ACIMA: [ ]  ║                                     ║",
    "╠═════════════════════════════════════╩═════════════════════════════════════╣",
    "║                                                                           ║",
    "╚═══════════════════════════════════════════════════════════════════════════╝"
]

xicara_vazia = [
    "           ",
    "           ",
    "           ",
    "           ",
    "┌─────────────────┐",
    "│                 │",
    "│                 ├─┬┐",
    "│                 │ ││",
    " \\               /  ││",
    "  \\             /───┴┘",
    "   \\           /",
    "    `─────────´"
    
]

fumaca_fase1 = [
    "      ((   ",
    "       ))  ",
    "        (( ",
    "         ))",
]

fumaca_fase2 = [
    "        (( ",
    "        )) ",
    "       ((  ",
    "       ))  ",
]

fases_fumaca = [
    fumaca_fase1,
    fumaca_fase2
]

cafe_expresso = [
    "      ((",
    "       ))",
    "        ((",
    "         ))",
    "┌─────────────────┐",
    "│                 │",
    f"│{COR_DO_EXPRESSO}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}├─┬┐",
    f"│{COR_DO_EXPRESSO}█████████████████{RESET}│ ││",
    f" \\{COR_DO_EXPRESSO}███████████████{RESET}/  ││",
    f"  \\{COR_DO_EXPRESSO}█████████████{RESET}/───┴┘",
    f"   \\{COR_DO_EXPRESSO}███████████{RESET}/",
    "    `─────────´"
]

cafe_com_leite = [
    "      ((",
    "       ))",
    "        ((",
    "         ))",
    "┌─────────────────┐",
    "│                 │",
    f"│{COR_DO_PINGADO}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}├─┬┐",
    f"│{COR_DO_PINGADO}█████████████████{RESET}│ ││",
    f" \\{COR_DO_PINGADO}███████████████{RESET}/  ││",
    f"  \\{COR_DO_PINGADO}█████████████{RESET}/───┴┘",
    f"   \\{COR_DO_PINGADO}███████████{RESET}/",
    "    `─────────´"
]

leite_puro = [
    "      ((",
    "       ))",
    "        ((",
    "         ))",
    "┌─────────────────┐",
    "│                 │",
    f"│{COR_DO_LEITE}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}├─┬┐",
    f"│{COR_DO_LEITE}█████████████████{RESET}│ ││",
    f" \\{COR_DO_LEITE}███████████████{RESET}/  ││",
    f"  \\{COR_DO_LEITE}█████████████{RESET}/───┴┘",
    f"   \\{COR_DO_LEITE}███████████{RESET}/",
    "    `─────────´"
]

agua_quente = [
    "      ((",
    "       ))",
    "        ((",
    "         ))",
    "┌─────────────────┐",
    "│                 │",
    f"│{COR_DA_AGUA}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}├─┬┐",
    f"│{COR_DA_AGUA}█████████████████{RESET}│ ││",
    f" \\{COR_DA_AGUA}███████████████{RESET}/  ││",
    f"  \\{COR_DA_AGUA}█████████████{RESET}/───┴┘",
    f"   \\{COR_DA_AGUA}███████████{RESET}/",
    "    `─────────´"
]

cappuccino = [
    "      ((",
    "       ))",
    "        ((",
    "         ))",
    "┌─────────────────┐",
    "│                 │",
    f"│{COR_DO_CAPPUCCINO}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}├─┬┐",
    f"│{COR_DO_CAPPUCCINO}█████████████████{RESET}│ ││",
    f" \\{COR_DO_CAPPUCCINO}███████████████{RESET}/  ││",
    f"  \\{COR_DO_CAPPUCCINO}█████████████{RESET}/───┴┘",
    f"   \\{COR_DO_CAPPUCCINO}███████████{RESET}/",
    "    `─────────´"
]

list_message_service = [
    "Seu Café Expresso está servido!  Hummm!!!! Que delícia!",
    "Seu Café com Leite está servido! Aproveite!",
    "Seu Cappuccino está servido! Ai, sim! Deu até vontade!",
    "Seu Água quente está servida! Vamos tomar um chá?",
    "Seu Leite está servido! Alimente-se!"
]

item_pedido = [
    cafe_expresso,
    cafe_com_leite,
    cappuccino,
    agua_quente,
    leite_puro
]

def posicionarCursor(linha: int, coluna: int):
    sys.stdout.write(f"\033[{linha};{coluna}H")

def exibirMensagem(mensagem: str, reposicionarCursor: bool):
    posicionarCursor(23, 3)
    input(mensagem)
    posicionarCursor(23, 3)
    print(" " * len(mensagem))
    if (reposicionarCursor):
        posicionarCursor(21, 35)
        print(" ")
        posicionarCursor(21, 35)

def limpar_desenho():
    for i in range(4, 21):
        posicionarCursor(i, 40)
        print(" " * 37, end="")

def exibir_xicara_vazia():
    linha = 4
    for texto in xicara_vazia:
        linha += 1
        posicionarCursor(linha, 47)
        print(texto, end="")

def servir_pedido(codigo_item: int):
    enchendo_xicara(codigo_item)
    balancar_fumaca(False)
    exibirMensagem(list_message_service[codigo_item], True)
    exibir_xicara_vazia()
    posicionarCursor(21, 35)

def enchendo_xicara(codigo_item: int):
    init_design = 10
    stop_line = 16
    caracter_liquid = f"{cores_do_liquido[codigo_item]}█{RESET}"
    caracter_movto = " "
    show_liquid = True
    # Enchendo a xícara
    while init_design > 5:
        for linha in range(5, stop_line):
            if linha == 9:
                if show_liquid:
                   continue
                else:
                    posicionarCursor(linha - 1, 56)
                    print(caracter_liquid, end="")
                    continue
            posicionarCursor(linha, 56)
            if show_liquid:
                print(caracter_liquid, end="")
            else:
                print(caracter_movto, end="")
                if (linha > 5) and (linha != 10):
                    posicionarCursor(linha - 1, 56)
                    print(caracter_liquid, end="")
            s(0.1)

        posicionarCursor(stop_line - 1, 47)
        print(item_pedido[codigo_item][init_design])
        show_liquid = False
        stop_line -= 1
        init_design -= 1
    for linha in range(10, 4, -1):
        posicionarCursor(linha, 47)
        print(item_pedido[codigo_item][init_design] + "  ")
        init_design -= 1
        s(0.08)

def balancar_fumaca(wait_time: bool):
    linha = 9
    fase = 0
    contador = 0

    while contador < 10:
        for texto in fases_fumaca[fase]:
            linha -= 1
            posicionarCursor(linha, 47)
            print(texto, end="")
            s(0.1)
        contador += 1
        if fase:
            fase = 0
        else:
            fase = 1
        linha = 9
    if wait_time:
       s(1)

limp("cls")

for linha in minha_tela:
    print(linha)

exibir_xicara_vazia()
posicionarCursor(21, 35)

sys.stdout.flush()
opcao = 0

while (opcao != 9):
    try:
        opcao = int(input())
        if ((opcao < 1 or opcao > 6) and (opcao != 9)):
            exibirMensagem("Opção inválida! Informe um número de 1 a 5 ou 9 pra encerrar", True)
            continue
        if opcao == 9:
            break
        if opcao == 6:
            balancar_fumaca(True)
            exibir_xicara_vazia()
            posicionarCursor(21, 35)
            print(" ")
            posicionarCursor(21, 35)
        else:
            servir_pedido(opcao - 1)
    except:
        exibirMensagem("Opção inválida! Pressione qualquer tecla para continuar!", True)
        
exibirMensagem("Obrigado pela preferência. Volte sempre!!!", False)