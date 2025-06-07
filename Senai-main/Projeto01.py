from time import sleep as s

for i in range(10, 0, -1):
    print("Irá explodir em:", i, "segundos!!!!", sep=" ")
    s(1)
    if (i == 5):
       print()
       print("Você ainda tem chance de ir embora!")
       print()

print()
print("Seu tempo acabou!!!!!!")
print()
print("Booooooooooooooooommmmmmmmmmmm!!!!")