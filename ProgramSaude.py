# Desenvolva em Python um script que solicite ao usuário que insira as suas informações 
# - Pressão
# - Temperatura
# - Batimentos cardíacos

# Com base nos dados informados, o programa deverá analisar cada uma separadamente para classificar a condição do usuário

# Temperatura Corporal
# - Hipotermia (Abaixo de 35° C)
# - Normal (Entre 35° C e 37.5° C)
# - Febre Leve (de 37.6°C A 39° C)
# - Febre Alta (acima de 39° C)

# Batimentos Cardíacos
# Taquicardia (Acima de 100 BPM)
# Bradicardia (Baixao de 60 BPM)
# Normal (Entre 60 e 100 BPM)

# Pressão Arterial
# - Normal (Entre 10.1 e 14)
# - Alta  (Maior que 14)
# - Baixa (Menor que 10)

# Classificação do atendimento

# Atendimento normal
# - Temperatura : Normal ou Febre Leve
# - Batimentos  : Normal
# - Pressão Arterial: Normal

# Atendimento Grave
# - Temperatura : Febre Alta
# - Batimentos  : Taquicardia
# - Pressão Arterial: Alta

# Atendimento Urgente
# - Temperatura : Hipotermia
# - Batimentos  : Braquicardia
# - Pressão Arterial: Baixa


from os import system as limp

descricao_temperatura = [
    "Hipotermia",
    "Normal",
    "Febre Leve",
    "Febre Alta"
]

descricao_pressao = [
    "Normal",
    "Baixa",
    "Alta"
]

descricao_batimentos = [
    "Normal",
    "Com Braquicardia",
    "Com Taquicardia"
]

status_atendimento = -1
status_temperatura = -1
status_batimentos = -1
status_pressao = -1

situacao_paciente = [
    "Atendimento Normal",
    "Atendimento Grave",
    "Atendimento Urgente"
]


continuar = "S"
classificacao = -1

while continuar == "S":
    limp("cls")
    try:
        temperatura = float(input("Informe sua temperatura: "))
        pressao_arterial = float(input("Informe sua pressão arterial: "))
        batimentos_cardiacos = int(input("Informe seus batimentos cardíacos: "))

        # Classificação temperatura
        if (temperatura < 35):
            status_temperatura = 0
        elif (temperatura >= 35 and temperatura <= 37.5):
            status_temperatura = 1
        elif (temperatura >= 37.6 and temperatura <= 39):
            status_temperatura = 2
        else:
            status_temperatura = 3
            
        # Classificação batimentos cardíacos
        if (batimentos_cardiacos < 60):
            status_batimentos = 1
        elif (batimentos_cardiacos > 60 and batimentos_cardiacos <= 100):
            status_batimentos = 0
        else:
            status_batimentos = 2

        # Classificação da Pressão Arterial
        if (pressao_arterial <=10):
            status_pressao = 1
        elif (pressao_arterial >= 10.1 and pressao_arterial <= 14):
            status_pressao = 0
        else:
            status_pressao = 2

        if ((status_temperatura == 1 or status_temperatura == 2) and status_batimentos == 0 and status_pressao == 0):
            status_atendimento = 0
        elif (status_temperatura == 3 and status_batimentos == 2 and status_pressao == 2):
            status_atendimento = 1
        else:
            status_atendimento = 2

        print()
        print(f"O paciente está com pressão {descricao_pressao[status_pressao]}, temperatura {descricao_temperatura[status_temperatura]} e")
        print(f"{descricao_batimentos[status_batimentos]}")
        print()
        print(f"Portanto, seu atendimento foi classificado em {situacao_paciente[status_atendimento]}")

    except:
        print("Informação inválida!")
    
    continuar = input("Digite S para continuar... ").upper()

print("Fim de Programa...")


