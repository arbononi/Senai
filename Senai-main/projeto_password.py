from os import system as limp
from time import sleep

password = 'SENAI'

senha = None
contador = 0

while password != senha:
    contador += 1
    limp('cls')
    senha = input('Digite a senha: ').upper()
    print('Checando digitação', end="")
    for i in range(5):
       print('.', end="")
       sleep(0.5)

print()
if contador < 5:
    print('Parabéns! Você foi rápido!')
else:
    print('Finalmente! Já estava ficando tonto de tanto repetir esse processo!!!!')
print("Tchau!!!!!")
sleep(3)
limp('cls')
