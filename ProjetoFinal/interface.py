import funcoes
from time import sleep

lin_padrao = 24
col_padrao = 3
size_padrao = 77
        
limpar_setor_operacoes = { "col": 39, "size": 42 }
tela_principal = [
    { "lin" : 1, "col": 1, "value": "╔═══════════════════════════════════════════════════════════════════════════════╗" },
    { "lin" : 2, "col": 1, "value": "║               CURSO PYTHON - SENAI - PROJETO FINAL - CALCULADORA              ║" },
    { "lin" : 3, "col": 1, "value": "╠════════════════════════════════════╦══════════════════════════════════════════╣" },
    { "lin" : 4, "col": 1, "value": "║                                    ║                                          ║" },
    { "lin": 23, "col": 1, "value": "╠════════════════════════════════════╩══════════════════════════════════════════╣" },
    { "lin": 24, "col": 1, "value": "║                                                                               ║" },
    { "lin": 25, "col": 1, "value": "╚═══════════════════════════════════════════════════════════════════════════════╝" },
]

tela_boas_vindas = [
    { "lin":  5, "col": 41, "value" : "┌───────────────────────────────────┐" },
    { "lin":  6, "col": 41, "value" : "│                                   │" },
    { "lin":  7, "col": 41, "value" : "│            Calculadora            │" },
    { "lin":  8, "col": 41, "value" : "│      Seja bem vindo, Usuário!     │" },
    { "lin":  9, "col": 41, "value" : "│                                   │" },
    { "lin": 10, "col": 41, "value" : "│                                   │" },
    { "lin": 11, "col": 41, "value" : "│                                   │" },
    { "lin": 12, "col": 41, "value" : "│                                   │" },
    { "lin": 13, "col": 41, "value" : "│       Projeto elaborado pela      │" },
    { "lin": 14, "col": 41, "value" : "│   Turma 2/2025 - Python - Sábado  │" },
    { "lin": 15, "col": 41, "value" : "│      Senai - SP - Sertãozinho     │" },
    { "lin": 16, "col": 41, "value" : "│                                   │" },
    { "lin": 17, "col": 41, "value" : "└───────────────────────────────────┘" },
]

tela_calculadora = {
     "0": { "lin": 21, "col":  3, "value": " 0 - Sair" },
     "1": { "lin":  5, "col":  3, "value": " 1 - Adição" },
     "2": { "lin":  6, "col":  3, "value": " 2 - Subtração" },
     "3": { "lin":  7, "col":  3, "value": " 3 - Mutiplicação" },
     "4": { "lin":  8, "col":  3, "value": " 4 - Divisão" },
     "5": { "lin":  9, "col":  3, "value": " 5 - Exponenciação" },
     "6": { "lin": 10, "col":  3, "value": " 6 - Raiz" },
     "7": { "lin": 11, "col":  3, "value": " 7 - Seno"},
     "8": { "lin": 12, "col":  3, "value": " 8 - Cosseno" },
     "9": { "lin": 13, "col":  3, "value": " 9 - Tangente "},
    "10": { "lin": 14, "col":  3, "value": "10 - Histórico" }
}

tela_try_except = [
    { 'lin':  5, 'col':  3, 'value': ' 1 - ValueError' },
    { 'lin':  6, 'col':  3, 'value': ' 2 - ZeroDivisionError' },
    { 'lin': 21, 'col':  3, 'value': ' 0 - Sair' }
]

opcoes_calculadora = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def exibir_interface():
    funcoes.desenhar_tela(tela_principal, start_loop=4, end_loop=23)
    funcoes.desenhar_tela(tela_boas_vindas)
    sleep(3)
    limpar_visualizacao()
    montar_opcoes()

def montar_opcoes():
    for _, value in tela_calculadora.items():
        funcoes.exibir_conteudo(value["value"], value["lin"], value["col"])

def limpar_linha():
    funcoes.limpar_linha(lin=lin_padrao, col=col_padrao, size=size_padrao)

def limpar_visualizacao():
    for lin in range(4, 23):
        funcoes.exibir_conteudo(" " * limpar_setor_operacoes["size"], lin, limpar_setor_operacoes["col"])

def exibir_historico(historicos):
    limpar_visualizacao()
    lin = 3
    for hist in historicos:
        lin += 1
        funcoes.exibir_conteudo(hist, lin, col=40)
        if lin == 22:
            limpar_linha()
            funcoes.exibir_mensagem("Pressione qualquer tecla para continuar...", lin=lin_padrao, col=col_padrao)
            limpar_visualizacao()
    limpar_linha()
    funcoes.exibir_mensagem("Fim do Histórico. Pressione qualquer tecla para encerrar...", lin=lin_padrao, col=col_padrao)
    limpar_visualizacao()
    
