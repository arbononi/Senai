import os
import time

# # Padrões de vapor que vão se alternando pra criar o efeito de movimento
# vapor_animado = [
#     ["   (  )   (   )  )",
#      "    ) (   )  (  (",
#      "    ( )  (    ) )"],
    
#     ["    )  )   )   )",
#      "   ( (   (   ((",
#      "    ) )   )   )"],
    
#     ["   (   )  (   ) ",
#      "    ) (    ) (  ",
#      "   (   )  (   ) "]
# ]

# xicara = [
#     "   _____________",
#     "  <_____________> ___",
#     "  |             |/ _ \\",
#     "  |               | | |",
#     "  |               |_| |",
#     " _|             |\\___/",
#     " /               \\",
#     "|_________________|",
#     " \\_______/\_______/"
# ]

# def limpar_tela():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def desenhar_xicara_com_vapor():
#     while True:
#         for vapor in vapor_animado:
#             limpar_tela()
#             for linha in vapor:
#                 print(linha)
#             for linha in xicara:
#                 print(linha)
#             time.sleep(0.4)

# try:
#     desenhar_xicara_com_vapor()
# except KeyboardInterrupt:
#     limpar_tela()
#     print("☕ Até a próxima pausa pro café!")


# ANSI colors
RESET = "\033[0m"
VAPOR = "\033[37m"     # branco
XICARA = "\033[38;2;139;69;19m"  # marrom (chocolate escuro)

vapor_animado = [
    [f"{VAPOR}   (  )   (   )  ){RESET}",
     f"{VAPOR}    ) (   )  (  ({RESET}",
     f"{VAPOR}    ( )  (    ) ){RESET}"],
    
    [f"{VAPOR}    )  )   )   ){RESET}",
     f"{VAPOR}   ( (   (   (( {RESET}",
     f"{VAPOR}    ) )   )   ){RESET}"],
    
    [f"{VAPOR}   (   )  (   ) {RESET}",
     f"{VAPOR}    ) (    ) (  {RESET}",
     f"{VAPOR}   (   )  (   ) {RESET}"]
]

xicara = [
    f"{XICARA}   _____________{RESET}",
    f"{XICARA}  <_____________> ___{RESET}",
    f"{XICARA}  |             |/ _ \\{RESET}",
    f"{XICARA}  |               | | |{RESET}",
    f"{XICARA}  |               |_| |{RESET}",
    f"{XICARA} _|             |\\___/{RESET}",
    f"{XICARA} /               \\{RESET}",
    f"{XICARA}|_________________|{RESET}",
    f"{XICARA} \\_______/\\_______/{RESET}"
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_xicara_com_vapor():
    while True:
        for vapor in vapor_animado:
            limpar_tela()
            for linha in vapor:
                print(linha)
            for linha in xicara:
                print(linha)
            time.sleep(0.4)

try:
    desenhar_xicara_com_vapor()
except KeyboardInterrupt:
    limpar_tela()
    print("☕ Até a próxima pausa pro café!")    