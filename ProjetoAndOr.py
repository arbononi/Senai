from os import system as limpar

limpar("cls")

opcao = "S"

while (opcao == "S"):
    x = float(input("Informe o primeiro valor: "))
    y = float(input("Informe o segundo valor: "))
    
    if x == y:
        print("Por favor, não informe valores iguais")
    elif x > y:
        print("O maior valor digitado foi o primeiro:", x)
    elif x < y:
        print("O maior valor digitado foi o segundo:", y)
    
    opcao = input("Continuar (S/N): ").upper()
  