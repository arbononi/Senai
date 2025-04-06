import os
import time

RESET = "\033[0m"
ESPUMA  = "\033[38;2;255;245;225m"   # espuma
LEITE   = "\033[38;2;210;180;140m"   # leite vaporizado
CAFE    = "\033[38;2;123;63;0m"      # café expresso
XICARA  = "\033[38;2;160;82;45m"     # xícara marrom clara

# Arte da xícara com camadas dentro
xicara = [
    f"{ESPUMA}     ~ ~     {RESET}",
    f"{ESPUMA}    (   )    {RESET}",
    f"{XICARA}   ..........",
    f"   |        |]{RESET}",
    f"{ESPUMA}   |  ░░░   |{RESET}",    # espuma
    f"{LEITE}   |  ▒▒▒   |{RESET}",    # leite vaporizado
    f"{CAFE}   |  ▓▓▓   |{RESET}",     # café expresso
    f"{XICARA}   \\        /",
    f"    `------'{RESET}"
]

# Mostrar a xícara
for linha in xicara:
    print(linha)