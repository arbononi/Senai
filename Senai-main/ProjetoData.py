from os import system as limp
from datetime import datetime


limp("cls")

#Solicitar os seguintes dados ao usuário
#Nome
#Dia do Nascimento
#Mês do Nascimento
#Ano do Nascimento
#Imprimir as seguintes informações
#Bem vindo {nome} ao SENAI!!!
#Sua data de Nascimento é {dia}/{mes}/{ano}
#Sua idade é {idade} anos

nome = input("Informe seu Nome:\n")
dia = int(input("Informe o dia do seu nascimento:\n"))
mes = int(input("Informe o mês do seu nascimento (número do mês):\n"))
ano = int(input("Informe o ano do seu nascimento:\n"))
hoje = datetime.today()
idade = datetime.now().year - ano

if (hoje.month, hoje.day) < (mes, dia):
    idade -= 1

limp("cls")

print(f"Bem vindo,{nome} ao SENAI!!!")
print(f"Sua data de nascimento é {dia:02}/{mes:02}/{ano:04}")
print(f"Sua idade é {idade} anos")
print()