#CRIAR O MENU E UMA MÁQUINA DE CAFÉ EXPRESSO
#MENU A SER IMPRESSO

#*************************************
#*************************************
#*************************************
#*********** CAFÉ'S SENAI ************
#*************************************
#* ESCOLHA UMA BEBIBA ABAIXO         *
#*************************************
#1 - CAFÉ EXPRESSO                   *
#2 - CAFÉ COM LEITE                  *
#3 - CAPPUCCINO                      *
#4 - ÁGUA QUENTE                     *
#5 - LEITE PURO                      *
#*                                   *
#*************************************

from os import system as limp

limp("cls")
opcao = 0
caracter = "*"

# while opcao != 9:
#    limp("cls")
#    print(caracter * 37)
#    print(caracter * 37)
#    print(caracter * 12, "CAFÉ'S SENAI", caracter * 11)
#    print(caracter * 37)
#    print(caracter * 37)
#    print(caracter, "     ESCOLHA UMA BEBIBA ABAIXO     ", caracter)
#    print("*" * 37)
#    print(caracter, "                                   ", caracter)
#    print(caracter, " 1 - CAFÉ EXPRESSO                 ", caracter)
#    print(caracter, " 2 - CAFÉ COM LEITE                ", caracter)
#    print(caracter, " 3 - CAPPUCCINO                    ", caracter)
#    print(caracter, " 4 - ÁGUA QUENTE                   ", caracter)
#    print(caracter, " 5 - LEITE PURO                    ", caracter)
#    print(caracter, "                                   ", caracter)
#    print(caracter, " 9 - DESLIGAR                      ", caracter)
#    print(caracter, "                                   ", caracter)
#    print(caracter * 37)
#    print()
#    print()
#    opcao = int(input("Opção: "))

#    if opcao == 1:
#       print("Você escolheu 1 - CAFÉ EXPRESSO.")
#    elif opcao == 2:
#       print("Você escolheu 2 - CAFÉ COM LEITE.")
#    elif opcao == 3:
#       print("Você escolheu 3 - CAPPUCCIONO")
#    elif opcao == 4:
#       print("Você escolheu 4 - ÁGUA QUENTE")
#    elif opcao == 5:
#       print("Você escolheu 5 - LEITE PURO")
#    elif opcao == 9:
#       print("Obrigado pela preferência. Volte Sempre!!!!")
#    else:
#       print("Opção inválida!")
#    input()

print((caracter * 43 + "\n") * 2, end="")
print(caracter * 10, end="")
print("\tCAFÉ'S SENAI\t", caracter * 10)
print(caracter * 43)
print("*     ESCOLHA UMA DAS BEBIDAS ABAIXO:     *")
