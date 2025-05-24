import sys
import os
from os import system
import calculos

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.my_functions import *

lin_padrao = 24
col_padrao = 3
size_padrao = 77

class Aula2405205:
    def __init__(self):
        self.limpar_centro_tela = { 'lin': 4, 'col': 2, 'value': ' ' * 79 }
        self.tela_principal = [
            { "lin":  1, "col": 1, "value": "╔═══════════════════════════════════════════════════════════════════════════════╗" },
            { "lin":  2, "col": 1, "value": "║                 CURSO PYTHON - SENAI - AULA DO DIA 24/05/2025                 ║" },
            { "lin":  3, "col": 1, "value": "╠═══════════════════════════════════════╦═══════════════════════════════════════╣" },
            { "lin":  4, "col": 1, "value": "║                                       ║                                       ║" },
            { "lin": 23, "col": 1, "value": "╠═══════════════════════════════════════╩═══════════════════════════════════════╣" },
            { "lin": 24, "col": 1, "value": "║ Escolha a opção desejada:                                                     ║" },
            { "lin": 25, "col": 1, "value": "╚═══════════════════════════════════════════════════════════════════════════════╝" },
        ]
        self.tela_calculadora = [
            { "lin":  5, "col":  3, "value": "1 - Adição" },
            { "lin":  6, "col":  3, "value": "2 - Subtração" },
            { "lin":  7, "col":  3, "value": "3 - Mutiplicação" },
            { "lin":  8, "col":  3, "value": "4 - Divisão" },
            { "lin":  9, "col":  3, "value": "5 - Exponenciação" },
            { "lin": 21, "col":  3, "value": "0 - Sair" }
        ]
        self.opcoes_disponiveis = {
            '1' : self.calculadora
        }
        self.opcoes = {
            '1' : { 'lin':  5, 'col':  3, 'value': ' 1 - Calculadora' },
            '0' : { 'lin': 21, 'col': 43, 'value': ' 0 - Sair' }
        }

    def iniciar(self):
        while True:
            desenhar_tela(layout=self.tela_principal, start_loop=4, end_loop=24)
            self.montar_opcoes()
            posicionarCursor(lin_padrao, 29)
            opcao = input()
            if opcao == '0':
                break
            acao = self.opcoes_disponiveis.get(opcao)
            if not acao:
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                exibir_mensagem("Opção inválida. Tente novamente!", lin_padrao, col_padrao, wait_key=True)
                continue
            if acao and callable(acao):
                esperar = acao()
            if esperar:
                esperar_tecla()

    def montar_opcoes(self):
        for _, value in self.opcoes.items():
            exibir_conteudo(value['value'], value['lin'], value['col'])

    def limpar_tela(self):
        exibir_conteudo("═",  3, 41)
        info = self.limpar_centro_tela
        for lin in range(4, 23):
            exibir_conteudo(info['value'], lin, info['col'])
        exibir_conteudo("═", 23, 41)
    
    def calculadora(self):
        self.limpar_tela()
        limpar_linha(lin_padrao, col_padrao, size_padrao)
        valores = []
        while True:
            self.limpar_tela()
            desenhar_tela(self.tela_calculadora)
            posicionarCursor(lin_padrao, col_padrao)
            operacao = input("Escolha a operação desejada: ")
            try:
                operacao = int(operacao)
                if operacao not in [1,2,3,4,5,0]:
                    exibir_mensagem("Opção inválida. Tente novamente!", lin_padrao, col_padrao, wait_key=True)
                    continue
                if operacao == 0:
                    break
                valores = self.get_valor()
                if len(valores) == 0:
                    limpar_linha(lin_padrao, col_padrao, size_padrao)
                    exibir_mensagem("Você não informou valores!", lin_padrao, col_padrao, wait_key=True)
                    continue
                match operacao:
                    case 1:
                        result = calculos.adicao(valores)
                        texto = "adição"
                    case 2:
                        result = calculos.subtracao(valores)
                        texto = "subtração"
                    case 3:
                        result = calculos.multiplicacao(valores)
                        texto = "multiplicação"
                    case 4:
                        result = calculos.divisao(valores)
                        texto = "divisão"
                    case 5:
                        result = calculos.exponenciacao(valores)
                        texto = "exponenciação"
                exibir_mensagem(f"O resultado da {texto} é: {result:.2f}", lin_padrao, col_padrao, wait_key=True)
                limpar_linha(lin_padrao, col_padrao, size_padrao)
            except ValueError:
                exibir_mensagem("Valor incorreto!", lin_padrao, col_padrao, wait_key=True)
                continue
        return False

    def get_valor(self):
        lista = []
        limpar_linha(lin_padrao, col_padrao, size_padrao)
        while True:
            try:
                limpar_linha(21, 3, size_padrao)
                posicionarCursor(21, 3)
                valor = float(input("Informe o valor (0 para encerrar): "))
                if valor == 0:
                    break
                lista.append(valor)
            except ValueError:
                exibir_mensagem("Valor inválido!", lin_padrao, col_padrao, wait_key=True)
                limpar_linha(lin_padrao, col_padrao, size_padrao)
        return lista


if __name__ == "__main__":
    system('cls')
    app = Aula2405205()
    app.iniciar()
    system('cls')