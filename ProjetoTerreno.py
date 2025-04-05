from os import system as limp

limp("cls")

#Calcular a área de um terreno.
#Inserir valor de Base e altura e apresentar a área

largura = 0.0
comprimento = 0.0

largura = float(input("Informe a largura do Terreno: "))
comprimento = float(input("Informe o comprimento do Terreno: "))
area_terreno = largura * comprimento

limp("cls")

print("Largura informada:", largura)
print("Comprimento informado:", comprimento)
print("Seu terreno tem uma área de ", area_terreno, " m² de área.", sep="")
print()

largura_int = int(largura)
comprimento_int = int(comprimento)

#Visão Horizontal
#Linha Superior
print("╔", ("═" * comprimento_int), "╗", sep="")
#Linhas intermediárias
print(("║" + " " * comprimento_int +  "║\n") * (largura_int - 2), end="")
#Base Inferior
print("╚", ("═" * comprimento_int), "╝", sep="")

#Visão Vertical
#Linha Superior
print("╔", ("═" * largura_int), "╗", sep="")
#Linhas intermediárias
print(("║" + " " * largura_int +  "║\n") * (comprimento_int - 2), end="")
#Linha inferior
print("╚", ("═" * largura_int), "╝", sep="")

