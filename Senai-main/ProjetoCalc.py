from os import system as limp

limp("cls")

opcao = 0

while(opcao != 6):
    limp("cls")
    
    soma = sub = mult = div = exp = None
    #soma, sub, mult, div, exp = None, None, None, None, None

    opcao = int(input("Escolha a operação:\n1- Soma\n2- Subtração\n3-Multiplicação\n4- Divisão\n5- Exponenciação\n6-Encerrar\n\n"))
    
    if (opcao < 1 or opcao > 6):
        print("Opção inválida!")
        continue
    if (opcao == 6):
        break
    
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    soma = valor1 + valor2
    sub = valor1 - valor1
    mult = valor1 * valor2
    div = valor1 / valor2
    exp = valor1 ** valor2

    if (opcao == 1):
        print(f"O resultado da soma: {valor1} + {valor2} = {soma}")
    elif (opcao == 2):
        print(f"O resultado da subtração: {valor1} - {valor2} = {sub}")
    elif (opcao == 3):
        print(f"O resultado da multiplicação: {valor1} * {valor2} = {mult}")
    elif (opcao == 4):
        print(f"O resultado da divisão: {valor1} / {valor2} = {div}")
    elif (opcao == 5):
        print(f"O resultado da exponenciação (potência): {valor1} ** {valor2} = {exp}")
    
    input("Pressione qualquer tecla para continuar...")