import sys
from os import system as limp

# ANSI colors
RESET = "\033[0m"
COR_DO_EXPRESSO = "\033[38;2;75;46;43m"
COR_DO_PINGADO = "\033[38;2;205;140;70m"
COR_DA_AGUA = "\033[38;2;173;216;230m"
COR_DO_LEITE = "\033[38;2;255;255;255m"
COR_DO_CAPPUCCINO = "\033[38;2;193;154;107m"
FUNDO_AMARELO_LETRA_PRETA = "\033[30;43m"
FUNDO_PRETO_LETRA_AMARELA = "\33[43;30m"

tela_principal = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                           *** CAFÉ'S SENAI ***                            ║
╠═════════════════════════════════════╦═════════════════════════════════════╣
║                                     ║                                     ║
║ 1 - CAFÉ EXPRESSO                   ║                                     ║
║ 2 - CAFÉ COM LEITE                  ║                                     ║
║ 3 - CAPPUCCINO                      ║                                     ║
║ 4 - ÁGUA QUENTE                     ║                                     ║
║ 5 - LEITE PURO                      ║                                     ║
║                                     ║                                     ║
║ 9 - DESLIGAR                        ║                                     ║
║                                     ║                                     ║
║                                     ║                                     ║
║                                     ║                                     ║
║                                     ║                                     ║
║                                     ║                                     ║
║                                     ║                                     ║
║                                     ║                                     ║
║                                     ║                                     ║
║ FAÇA SUA ESCOLHA:                   ║                                     ║
╠═════════════════════════════════════╩═════════════════════════════════════╣
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

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

tela_manutencao = [
    "┌─────────────────┐",
    f"│{FUNDO_PRETO_LETRA_AMARELA} (!)  MANUTENÇÃO {RESET}│",
    f"│{FUNDO_AMARELO_LETRA_PRETA}                 {RESET}│",
    f"│{FUNDO_AMARELO_LETRA_PRETA}    Máquina em   {RESET}│",
    f"│{FUNDO_AMARELO_LETRA_PRETA}    Manutenção   {RESET}│",
    f"├{FUNDO_AMARELO_LETRA_PRETA}─────────────────{RESET}┤",
    f"│{FUNDO_AMARELO_LETRA_PRETA}    Não Ligue    {RESET}│",
    "└─────────────────┘",

]
lista_mensagens = [
    "Seu Café Expresso está servido!  Hummm!!!! Que delícia!",
    "Seu Café com Leite está servido! Aproveite!",
    "Seu Cappuccino está servido! Ai, sim! Deu até vontade!",
    "Seu Água quente está servida! Vamos tomar um chá?",
    "Seu Leite está servido! Alimente-se!",
    "Aproveite as opções da vitrine!"
]

lista_telas = [
    cafe_expresso,
    cafe_com_leite,
    cappuccino,
    agua_quente,
    leite_puro,
    tela_manutencao
]

def desenha_tela_principal():
    limp("cls")
    print(tela_principal)

def limpar_desenho():
    for i in range(5, 21, 1):
        posicionarCursor(i, 40)
        print(" " * 37, end="")

def posicionarCursor(linha: int, coluna: int):
    sys.stdout.write(f"\033[{linha};{coluna}H")

def exibirMensagem(mensagem: str, reposicionarCursor: bool):
    posicionarCursor(23, 3)
    input(mensagem)
    posicionarCursor(23, 3)
    print(" " * len(mensagem))
    if (reposicionarCursor):
         limpar_campo_escolha()


def processar_opcao(opcao, tela):
    linha = 5
    for texto in tela:
        linha += 1
        posicionarCursor(linha,47)
        print(texto, end="")
    exibirMensagem(lista_mensagens[opcao - 1], True)
    limpar_desenho()   
   
def limpar_campo_escolha():
    posicionarCursor(21, 21)
    print("      ")
    posicionarCursor(21, 21)

limp("cls")
print(tela_principal)

posicionarCursor(21, 21)
sys.stdout.flush()

opcao = 0

while (opcao != 9):
   try:
      opcao = int(input())
      if (opcao == 75452):
          opcao = 6
      
      if (opcao < 1 or opcao > 6) and opcao != 9 and opcao != 75452:
         exibirMensagem("Opção inválida! Informe um número de 1 a 5 ou 9 pra encerrar", True)
         limpar_campo_escolha()
         continue
      
      if (opcao == 9):
         break

      processar_opcao(opcao, lista_telas[opcao - 1])
   except:
        exibirMensagem("Opção inválida! Pressione qualquer tecla para continuar!", True)

   limpar_campo_escolha()

exibirMensagem("Obrigado pela preferência. Volte sempre!!!", False)