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

# Pressão Arterial
# - Baixa (Menor que 10)
# - Normal (Entre 10.1 e 14)
# - Alta  (Maior que 14)

# Batimentos Cardíacos
# Bradicardia (Abaixo de 60 BPM)
# Normal (Entre 60 e 100 BPM)
# Taquicardia (Acima de 100 BPM)

# Classificação do atendimento

# Atendimento normal
# - Temperatura : Normal ou Febre Leve
# - Pressão Arterial: Normal
# - Batimentos  : Normal

# Atendimento Grave
# - Temperatura : Febre Alta
# - Pressão Arterial: Alta
# - Batimentos  : Taquicardia

# Atendimento Urgente
# - Temperatura : Hipotermia
# - Pressão Arterial: Baixa
# - Batimentos  : Braquicardia

import sys
from os import system as limp
from time import sleep as s
import Funcoes

tela_principal = """
╔══════════════════════════════════════════════════════════════════════════╗
║                      CENTRO HOSPITALAR GRACE HOPPER                      ║
╠════════════════════════╦═════════════════════════════════════════════════╣
║                        ║                                                 ║
║ 1 - CENTRO DE TRIAGEM  ║                                                 ║
║ 2 - RESULTADOS         ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║ 9 - DESLIGAR           ║                                                 ║
║                        ║                                                 ║
║                        ║                                                 ║
║ FAÇA SUA ESCOLHA: [ ]  ║                                                 ║
╠════════════════════════╩═════════════════════════════════════════════════╣
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝"""

tela_triagem = [
"┌─────────────────────────────────────────────┐",
"│                                             │",
"├─────────────────────────────────────────────┤",
"│ NOME :                                      │",
"│ Idade:                                      │",
"├─────────────────────────────────────────────┤",
"│             EXAMES PRELIMINARES             │",
"├─────────────────────────────────────────────┤",
"│ Temperatura .......:                        │",
"│ Pressão Arterial ..:                        │",
"│ Frequência Cardíaca:                        │",
"│                                             │",
"│                                             │",
"└─────────────────────────────────────────────┘"
]

titulo_tela = [
    "CENTRO DE TRIAGEM",
    "RESULTADO EXAMES"
]

tipo_tela = [
    "Confirma os Dados (S/N): ",
    "Atendimento Recomendado: "
]

descricao_temperatura = [
    "Hipotermia",
    "Normal",
    "Febre Leve",
    "Febre Alta"
]

descricao_pressao = [
    "Baixa",
    "Normal",
    "Alta"
]

descricao_batimentos = [
    "Com Braquicardia",
    "Normal",
    "Com Taquicardia"
]

status_atendimento = 3
status_temperatura = -1
status_batimentos = -1
status_pressao = -1

situacao_paciente = [ "Normal", "Grave", "Urgente", "Sem previsão" ]

def informar_valor(mensagem, linha, coluna):
    fl_ok = False
    valor = 0

    Funcoes.posicionarCursor(23, 3)
    print(mensagem)
    Funcoes.posicionarCursor(linha, coluna)

    while not fl_ok:
        try:
            valor = float(input().replace(",", "."))
            fl_ok = True
        except ValueError:
            Funcoes.limpar_linha()
            Funcoes.posicionarCursor(23, 3)
            print("Informação inválida!")
            Funcoes.limpar_linha()
            Funcoes.posicionarCursor(linha, coluna)
    return valor

def definir_atendimento(temperatura, pressao, batimentos):
    result = 3
    global status_temperatura
    global status_pressao
    global status_batimentos

    # Checando a temperatura
    if (temperatura < 35):
        status_temperatura = 0
    elif (temperatura >= 35 and temperatura <= 37.5):
        status_temperatura = 1
    elif (temperatura >= 37.6 and temperatura <= 39):
        status_temperatura = 2
    else:
        status_temperatura = 3

    # Checando a pressão arterial
    if (pressao < 10):
        status_pressao = 0
    elif (pressao >= 10 and pressao <= 14):
        status_pressao = 1
    else:
        status_pressao = 2

    # Checando os batimentos cardíacos
    if (batimentos < 60):
        status_batimentos = 0
    elif (batimentos >= 60 and batimentos <= 100):
        status_batimentos = 1
    else:
        status_batimentos = 2

    # Checando o tipo de Atendimento
    if (status_temperatura == 0 and status_pressao == 0 and status_batimentos == 0):
        result = 2
    elif ((status_temperatura == 1 or status_temperatura == 2) and status_pressao == 1 and status_batimentos == 1):
        result = 0
    elif (status_temperatura == 3 and status_pressao == 2 and status_batimentos == 2):
        result = 1
    else:
        result = 3
    return result

def efetuar_triagem():
    global lista_pacientes
    Funcoes.desenhar_tela(6, tela_triagem)
    Funcoes.posicionarCursor(7, 30)
    print(str.center(titulo_tela[0], 43, " "))
    linha = 9
    Funcoes.exibirMensagem(23, 3, "Informe o nome do paciente")
    Funcoes.posicionarCursor(linha, 37)
    nome = input()
    Funcoes.limpar_linha()
    idade = int(informar_valor("Informe a idade do paciente", 10, 37))
    temperatura = informar_valor("Informe a temperatura do paciente", 14, 51)
    pressao_arterial = informar_valor("Informe a pressão arterial do paciente", 15, 51)
    batimentos_cardiacos = informar_valor("Informe os frequência cardíaca do paciente", 16, 51)
    Funcoes.limpar_linha()
    status_atendimento = definir_atendimento(temperatura, pressao_arterial, batimentos_cardiacos)

    Funcoes.posicionarCursor(18, 30)

    if input(tipo_tela[0]).upper() == "S":
        paciente = {
            "Nome": nome, 
            "Idade": idade, 
            "Temperatura": temperatura, 
            "Status_Temperatura" : descricao_temperatura[status_temperatura],
            "Pressao": pressao_arterial, 
            "Status_Pressao" : descricao_pressao[status_pressao],
            "Frequencia" : batimentos_cardiacos, 
            "Status_Batimentos" : descricao_batimentos[status_batimentos],
            "Tipo_Atendimento" : situacao_paciente[status_atendimento]
        }
        lista_pacientes.append(paciente)

def exibir_resultados():
    global lista_pacientes

    for paciente in lista_pacientes:
        Funcoes.desenhar_tela(6, tela_triagem)
        Funcoes.posicionarCursor(7, 30)
        print(str.center(titulo_tela[1], 43, " "))
        linha = 9
        Funcoes.posicionarCursor(linha, 37)
        print(paciente["Nome"])
        linha += 1
        Funcoes.posicionarCursor(linha, 37)
        print(paciente["Idade"])
        linha += 4
        Funcoes.posicionarCursor(linha, 51)
        print(f"{paciente["Temperatura"]} - {paciente["Status_Temperatura"]}")
        linha += 1
        Funcoes.posicionarCursor(linha, 51)
        print(f"{paciente["Pressao"]} - {paciente["Status_Pressao"]}")
        linha += 1
        Funcoes.posicionarCursor(linha, 51)
        print(f"{paciente["Frequencia"]} - {paciente["Status_Batimentos"]}")
        linha += 2
        Funcoes.posicionarCursor(linha, 30)
        print(f"Atendimento Recomendado: {paciente["Tipo_Atendimento"]}")
        Funcoes.posicionarCursor(23, 3)
        Funcoes.exibirMensagem(23, 3, "Pressione qualquer tecla para visualizar próximo paciente", "")
        input()

lista_pacientes = []

continuar = "S"
limp("cls")
print(tela_principal)
opcao = 0

while opcao != 9:
    Funcoes.posicionarCursor(21, 22)
    try:
        opcao = int(input())

        if opcao == 9:
            Funcoes.exibirMensagem(23, 3, "Obrigado por usar o Centro Hospitalar Grace Hopper! Volte Sempre!")
            s(0.9)
            break
        elif opcao == 1:
            efetuar_triagem()
        else:
            exibir_resultados()
        
        Funcoes.limpar_tela(5, 22, 28, 47)
        Funcoes.limpar_linha(21, 22, 1)
    except ValueError:
        Funcoes.exibirMensagem(23, 3, "Opção inválida! Digite 1, 2 ou 9 para encerrar!", "")
        input()
        Funcoes.limpar_linha()
limp("cls")