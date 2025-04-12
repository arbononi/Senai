from os import system as limp

limp("cls")

# nome = "André Rogério Bononi"
# print(nome)
# for letra in nome:
#    print(letra)

# nome = input("Digite seu nome:\n")
# data = int(input("Digite o ano que você nasceu:\n"))
# idade = 2025 - data

# print()
# print("Seu nome é:", nome)
# print("Sua idade é", idade, "anos")

def formatar_cpf(num_cpf: int) -> str:
   strCpf = str(num_cpf)
   return f"{strCpf[:3]}.{strCpf[3:6]}.{strCpf[6:9]}-{strCpf[9:]}"

def formatar_fone(num_fone: int) -> str:
   strFone = str(num_fone)
   return f"({strFone[:2]}) {strFone[2:7]}-{strFone[7:]}"

nome = input("Digite seu Nome: ")
data_nasc = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")
num_cpf = int(input("Digite o número do seu CPF (somente os números): "))
telefone = int(input("Digite o número do seu telefone com DDD (somente os números): "))

print()
print("Seus dados são:")
print("Nome " + "." * 13 + ": ", nome)
print("Data de Nascimento: ", data_nasc)
print("CPF No " + "." * 11 + ": ", formatar_cpf(num_cpf))
print("Telefone No " + "." * 6 + ": ", formatar_fone(telefone))

print()

