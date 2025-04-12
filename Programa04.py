from os import system as limpar

limpar("cls")


configuracao = """
TABELA DE REFERENCIA
   CRIANÇA ...: DE  0 A 12 ANOS
   ADOLESCENTE: DE 13 A 17 ANOS
   ADULTO.....: DE 18 A 59 ANOS
   IDOSO .....: ACIMA DE 59 ANOS
"""

tela_principal = """
      
    1- Grupo Etário
    2- Aprovação de Aluno
    9- Encerrar

"""

def grupo_etario():

    continuar = "S"

    while (continuar == "S"):

        limpar("cls")
        idade = int(input("Informe sua idade: "))

        if (idade >= 0 and idade <= 12):
            print("Você é uma criança!")
        elif (idade > 12 and idade < 18):
            print("Você é adolescente!")
        elif (idade >= 18 and idade <=59):
            print("Você é um adulto!!!")
        elif (idade >= 60):
            print("Você está na melhor idade (Idoso)")
        else:
            print("Com quem estou falando se você ainda não nasceu?????")
        print()
        continuar = input("Continuar (S/N) ").upper()

    continuar = "S"
    
    print(configuracao)

def aprovacao_aluno():
    
    continuar = "S"

    while continuar == "S":
        limpar("cls")
    
        nota_final = float(input("Informe a nota final do aluno: "))
        frequencia = float(input("Informe a frequencia do aluno: "))

        if (nota_final >= 7 and frequencia >= 75):
            print("Aluno Aprovado!!!")
        else:
            print("Aluno Reprovado!")

        continuar = input("Informar outro aluno (S/N): ").upper()

opcao = 0
limite_opcao = 2

while opcao != 9:
    limpar("cls")
    print(tela_principal)
    
    try:
        opcao = int(input("Faça sua escolha: "))

        if ((opcao < 1 or opcao > limite_opcao) and opcao != 9):
            input("Opção inválida!" )
            continue
        if (opcao == 1):
            grupo_etario()
        elif (opcao == 2):
            aprovacao_aluno()
    except:
        input("Opção inválida! ")
    
print("Obrigado!!! Volte Sempre!!!")

