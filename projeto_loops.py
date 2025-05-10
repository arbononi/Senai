from os import system as limp
from enum import Enum
from time import sleep

class StatusTemperatura(Enum):
    HIPOTERMIA = 1
    NORMAL = 2
    FEBRIL = 3
    FEBRE = 4

continuar = True

def determina_temperatura(temp):
    if temp < 36.7:
        return StatusTemperatura.HIPOTERMIA
    elif temp < 37.8:
        return StatusTemperatura.NORMAL
    elif temp > 37.8 and temp < 38.0:
        return StatusTemperatura.FEBRIL
    else:
        return StatusTemperatura.FEBRE

def determinar_status(idade, temperatura_corporal):
    if (temperatura_corporal == StatusTemperatura.FEBRE or temperatura_corporal == StatusTemperatura.FEBRIL) or idade < 18:
        return False
    return True

def imprimir_informacoes(nome, idade, temp_corpo, status):
    linhas = []
    linhas.append(f'Olá, {nome}')
    linhas.append(f'Você tem, atualmente, {idade} anos e seu estado corporal é {temp_corpo.name}')
    linhas.append(f'Portanto, você {('está apto' if status else 'não está apto')} para exercer a função que precisamos!')
    if status:
        linhas.append('Nos vemos na segunda para você começar o treinamento!')
    else:
        linhas.append('Sinto muito! Obrigado pela atenção!')
    for linha in linhas:
        for letra in linha:
            print(letra, end="")
            sleep(0.1)
        print()
    return True if input('Deseja continuar? (S/N) ').upper() == 'S' else False

def get_nome():
    while True:
        nome = input('Digite seu nome: ')
        if nome == '':
            input('Ah, por favor, diga seu nome!!!')
            continue
        break
    return nome

def get_idade():
    while True:
        try:
            idade = int(input("Informe sua idade (Não se preocupe. Sou discreto!): "))
            if idade == 0:
                input("Oh, meu Deus!!! Estou falando com um espírito que ainda não nasceu!!!! Fala sério, vai?!!")
                continue
            break
        except ValueError:
            print('Valor inválido!')
    return idade

def get_temperatura():
    while True:
        try:
            temp = float(input('Informe sua temperatura: '))
            break
        except ValueError:
            print('Valor inválido!')
    return temp

while continuar:
    limp('cls')
    nome = get_nome()
    idade = get_idade()
    temp = get_temperatura()
    temperatura_corporal = determina_temperatura(temp)
    status = determinar_status(idade, temperatura_corporal)
    continuar = imprimir_informacoes(nome=nome, idade=idade, temp_corpo=temperatura_corporal, status=status)

