#╔═══════════════════════════════════════════════════════════════════════════╗
#║                           *** CAFÉ'S SENAI ***                            ║
#╠═════════════════════════════════════╦═════════════════════════════════════╣
#║                                     ║                                     ║
#║ 1 - CAFÉ EXPRESSO                   ║                                     ║
#║ 2 - CAFÉ COM LEITE                  ║                                     ║
#║ 3 - CAPPUCCINO                      ║                                     ║
#║ 4 - ÁGUA QUENTE                     ║                                     ║
#║ 5 - LEITE PURO                      ║                                     ║
#║                                     ║                                     ║
#║ 9 - DESLIGAR                        ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║                                     ║                                     ║
#║ ESCOLHA UMA DAS BEBIDAS ACIMA: [ ]  ║                                     ║
#╠═════════════════════════════════════╩═════════════════════════════════════╣
#║                                                                           ║
#╚═══════════════════════════════════════════════════════════════════════════╝

import sys
from os import system as limp

# ANSI colors
RESET = "\033[0m"
COR_DO_EXPRESSO = "\033[38;2;75;46;43m"
COR_DO_PINGADO = "\033[38;2;205;140;70m"
COR_DA_AGUA = "\033[38;2;173;216;230m"
COR_DO_LEITE = "\033[38;2;255;255;255m"
COR_DO_CAPPUCCINO = "\033[38;2;193;154;107m"

cafe_expresso = [
    "      ((",
    "       ))",
    "        ((",
    "         ))",
    "┌─────────────────┐",
    "│                 │",
    f"│{COR_DO_EXPRESSO}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}├─┬┐",
    f"│{COR_DO_EXPRESSO}█████████████████{RESET}│ ││",
    f" \{COR_DO_EXPRESSO}███████████████{RESET}/  ││",
    f"  \{COR_DO_EXPRESSO}█████████████{RESET}/───┴┘",
    f"   \{COR_DO_EXPRESSO}███████████{RESET}/",
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
    f" \{COR_DO_PINGADO}███████████████{RESET}/  ││",
    f"  \{COR_DO_PINGADO}█████████████{RESET}/───┴┘",
    f"   \{COR_DO_PINGADO}███████████{RESET}/",
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
    f" \{COR_DO_LEITE}███████████████{RESET}/  ││",
    f"  \{COR_DO_LEITE}█████████████{RESET}/───┴┘",
    f"   \{COR_DO_LEITE}███████████{RESET}/",
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
    f" \{COR_DA_AGUA}███████████████{RESET}/  ││",
    f"  \{COR_DA_AGUA}█████████████{RESET}/───┴┘",
    f"   \{COR_DA_AGUA}███████████{RESET}/",
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
    f" \{COR_DO_CAPPUCCINO}███████████████{RESET}/  ││",
    f"  \{COR_DO_CAPPUCCINO}█████████████{RESET}/───┴┘",
    f"   \{COR_DO_CAPPUCCINO}███████████{RESET}/",
    "    `─────────´"
]
def limpar_desenho():
    for i in range(4, 21, 1):
        posicionarCursor(i, 40)
        print(" " * 37, end="")

def posicionarCursor(linha: int, coluna: int):
    sys.stdout.write(f"\033[{linha};{coluna}H")

def exibirMensagem(mensagem: str, reposicionarCursor: bool):
    posicionarCursor(22, 3)
    input(mensagem)
    posicionarCursor(22, 3)
    print(" " * len(mensagem))
    if (reposicionarCursor):
        posicionarCursor(20, 35)
        print(" ")
        posicionarCursor(20, 35)

def opcao1():
    linha = 4
    for texto in cafe_expresso:
        linha += 1
        posicionarCursor(linha,47)
        print(texto, end="")

    exibirMensagem("Seu Café Expresso está servido!  Hummm!!!! Que delícia!", True)
    limpar_desenho()
    posicionarCursor(20, 35)

def opcao2():
    linha = 4
    for texto in cafe_com_leite:
        linha += 1
        posicionarCursor(linha,47)
        print(texto, end="")

    exibirMensagem("Seu Café com Leite está servido! Aproveite!", True)
    limpar_desenho()
    posicionarCursor(20, 35)

def opcao3():
    linha = 4
    for texto in cappuccino:
        linha += 1
        posicionarCursor(linha,47)
        print(texto, end="")

    exibirMensagem("Seu Cappuccino está servido! Ai, sim! Deu até vontade!", True)
    limpar_desenho()
    posicionarCursor(20, 35)

def opcao4():
    linha = 4
    for texto in agua_quente:
        linha += 1
        posicionarCursor(linha,47)
        print(texto, end="")

    exibirMensagem("Seu Água quente está servida! Vamos tomar um chá?", True)
    limpar_desenho()
    posicionarCursor(20, 35)    

def opcao5():
    linha = 4
    for texto in leite_puro:
        linha += 1
        posicionarCursor(linha,47)
        print(texto, end="")

    exibirMensagem("Seu Leite está servido! Alimente-se!", True)
    limpar_desenho()
    posicionarCursor(20, 35)

limp("cls")

print("╔" + "═" * 75 + "╗")
print("║" + " " * 27 + "*** CAFÉ'S SENAI ***" + " " * 28 + "║")
print("╠" + "═" * 37 + "╦" + "═" * 37 + "╣")
print("║" + " " * 37 + "║" + " " * 37 + "║")
print("║ 1 - CAFÉ EXPRESSO" + " " * 19 + "║" + " " * 37 + "║")
print("║ 2 - CAFÉ COM LEITE" + " " * 18 + "║" + " " * 37 + "║")
print("║ 3 - CAPPUCCINO" + " " * 22 + "║" + " " * 37 + "║")
print("║ 4 - ÁGUA QUENTE" + " " * 21 + "║" + " " * 37 + "║")
print("║ 5 - LEITE PURO" + " " * 22 + "║" + " " * 37 + "║")
print(("║" + " " * 37 + "║" + " " * 37 +"║\n") * 7, end="")
print("║ 9 - DESLIGAR" + " " * 24 + "║" + " " * 37 + "║")
print(("║" + " " * 37 + "║" + " " * 37 +"║\n") * 2, end="")
print("║ ESCOLHA UMA DAS BEBIDAS ACIMA: [ ]  ║" + " " * 37 + "║")
print("╠" + "═" * 37 + "╩" + "═" * 37 + "╣")
print("║" + " " * 75 + "║")
print("╚" + "═" * 75 + "╝")
posicionarCursor(20, 35)

sys.stdout.flush()
opcao = 0

while (opcao != 9):
    try:
        opcao = int(input())
        if ((opcao < 1 or opcao > 5) and (opcao != 9)):
            exibirMensagem("Opção inválida! Informe um número de 1 a 5 ou 9 pra encerrar", True)
            continue
        if (opcao == 9):
            break
        
        if (opcao == 1):
            opcao1()
        elif (opcao == 2):
            opcao2()
        elif (opcao == 3):
            opcao3()
        elif (opcao == 4):
            opcao4()
        else:
            opcao5()
    except:
        exibirMensagem("Opção inválida! Pressione qualquer tecla para continuar!", True)
        
exibirMensagem("Obrigado pela preferência. Volte sempre!!!", False)