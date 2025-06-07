from os import system as limp

continuar = "S"

while continuar.upper() == "S":
    
    limp("cls")

    blocks = int(input("Insira o número de blocos: "))  

    # Escreva seu código aqui.
    base = 0
    altura = 0
    block_image = "X"
    used_blocks = 0
    blocks_info = blocks
    blocks_design = 0

    while blocks > 0:
        base += 1
        if base > blocks:
            base -= 1
            break
        blocks -= base
        altura += 1
        used_blocks += base

    #
    
    limp("cls")

    print("Total de blocos ....:", blocks_info)
    print("Blocos utilizados ..:", used_blocks)
    print("A altura da pirâmide:", altura)
    print("Base composta por ..:", base, "blocos")
    print()

    blocks_design = base * 2 - 1

    for i in range(1, altura + 1):
        qtd_spaces = blocks_design - base
        design_pyramid = " " * qtd_spaces + " ".join([block_image] * i)
        print(design_pyramid, " " * qtd_spaces, "linha:", i)
        blocks_design -= 1

    print()
    continuar = input("Deseja continuar (S/N)? ")