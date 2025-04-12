#Imprimir na tela as seguintes informações
# Nome:
# Telefone:
# Endereço:
# Data Nascimento:
# Nascimento:
# Naturalidade:

from os import system as limp

limp("cls")

nome_completo = ""
telefone = ""
endereco = ""
data_nasc = ""
nacionalidade = ""
naturalidade = ""
opcao = 0

def ImprimePadrao():
    limp("cls")
    print("Nome ..........:", "André Rogério Bononi")
    print("Telefone ......:", "(XX) XXXXX-XXXX")
    print("Endereço ......:", "YYY YYYYYY YYYYY, NNNN")
    print("Data Nascimento:", "05/04/2025")
    print("Nacionalidade .:", "Brasileira")
    print("Naturalidade ..:", "Sertãozinho\n")
    
    input("Pressione qualquer coisa para continuar....")

def DigitarDados():
    limp("cls")
   
    nome_completo = input("Informe seu nome completo: ")
    telefone = input("Informe seu telefone com DDD: ")
    endereco = input("Informe seu endereço: ")
    data_nasc = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    nacionalidade = input("Informe sua nacionalidade: ")
    naturalidade = input("Informe a cidade onde nasceu: ")
 
    limp("cls")

    print("Os dados digitados foram:\n")
    print("Nome ..........:", nome_completo)
    print("Telefone ......:", telefone)
    print("Endereço ......:", endereco)
    print("Data Nascimento:", data_nasc)
    print("Nacionalidade .:", nacionalidade)
    print("Naturalidade ..:", naturalidade, "\n")

    input("Pressione qualquer coisa para continuar....")

while opcao != 9:
   limp("cls")

   print("1- Dados padrão")
   print("2- Informar os dados")
   print("9- Encerrar programa")

   opcao = int(input("Escolha a opção desejada: "))
   
   if (opcao == 1):
      ImprimePadrao()
   elif opcao == 2:
      DigitarDados()
   elif opcao != 9:
      input("Opção inválida!")
   
