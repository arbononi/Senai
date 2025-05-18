from os import system
from utils.my_functions import *

lin_padrao = 24
col_padrao = 3
size_padrao = 77

class Aula2405205:
    def __init__(self):
        self.limpar_centro_tela = { 'lin': 4, 'col': 2, 'value': ' ' * 79 }
        self.tela_principal = [
            { "lin":  1, "col":  1, "value": "╔═══════════════════════════════════════════════════════════════════════════════╗" },
            { "lin":  2, "col":  1, "value": "║                 CURSO PYTHON - SENAI - AULA DO DIA 31/05/2025                 ║" },
            { "lin":  3, "col":  1, "value": "╠═══════════════════════════════════════╦═══════════════════════════════════════╣" },
            { "lin":  4, "col":  1, "value": "║                                       ║                                       ║" },
            { "lin":  23, "col": 1, "value": "╠═══════════════════════════════════════╩═══════════════════════════════════════╣" },
            { "lin":  24, "col": 1, "value": "║ Escolha a opção desejada:                                                     ║" },
            { "lin":  25, "col": 1, "value": "╚═══════════════════════════════════════════════════════════════════════════════╝" },
        ]
        self.opcoes_disponiveis = {
            '1' : self.funcoes
        }
        self.opcoes = {
            '1' : { 'lin':  5, 'col':  3, 'value': ' 1 - Funções' },
            '0' : { 'lin': 21, 'col': 43, 'value': ' 0 - Sair' }
        }

    def iniciar(self):
        while True:
            self.desenhar_tela()
            posicionarCursor(lin_padrao, 29)
            opcao = input()
            if opcao == '0':
                break
            acao = self.opcoes_disponiveis.get(opcao)
            if not acao:
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                exibir_mensagem("Opção inválida. Tente novamente!", lin_padrao, col_padrao)
                continue
            if acao and callable(acao):
                esperar = acao()
            if esperar:
                esperar_tecla()

    def desenhar_tela(self):
        for info in self.tela_principal:
            if info["lin"] != 4:
                exibir_conteudo(info['value'], info['lin'], info['col'])
            else:
                lin = info['lin']
                while lin < 23:
                    exibir_conteudo(info['value'], lin, info['col'])
                    lin += 1
        
        for _, value in self.opcoes.items():
            exibir_conteudo(value['value'], value['lin'], value['col'])

    def limpar_tela(self):
        exibir_conteudo("═",  3, 41)
        info = self.limpar_centro_tela
        for lin in range(4, 23):
            exibir_conteudo(info['value'], lin, info['col'])
        exibir_conteudo("═", 23, 41)
    
    def funcoes(self):
        self.limpar_tela()
        limpar_linha(lin_padrao, col_padrao, size_padrao)
        exibir_mensagem("Opção ainda em desenvolvimento!", lin_padrao, col_padrao)
        return False

system('cls')
app = Aula2405205()
app.iniciar()
system('cls')