from os import system as limp
from time import sleep

def get_numero():
    while True:
        try:
            tabuada = int(input('Qual a tabuada deseja verificar? '))
            break
        except ValueError:
            print("Valor inválido!")
    return tabuada

def iniciar(tabuada):
    x = 0
    while x < 10:
        x += 1
        print(f'{x} * {tabuada} =', x * tabuada)
        sleep(0.5)
    return tabuada

limp('cls')

while True:
    tabuada = get_numero()
    if tabuada == 0:
        break
    iniciar(tabuada)