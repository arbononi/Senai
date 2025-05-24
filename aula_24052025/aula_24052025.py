import sys
import os
from os import system
import calculos
import try_except

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
            { "lin":  5, "col":  3, "value": " 1 - Adição" },
            { "lin":  6, "col":  3, "value": " 2 - Subtração" },
            { "lin":  7, "col":  3, "value": " 3 - Mutiplicação" },
            { "lin":  8, "col":  3, "value": " 4 - Divisão" },
            { "lin":  9, "col":  3, "value": " 5 - Exponenciação" },
            { "lin": 10, "col":  3, "value": " 6 - Raiz de um número" },
            { "lin": 11, "col":  3, "value": " 7 - Seno de um número "},
            { "lin": 12, "col":  3, "value": " 8 - Cosseno de um número" },
            { "lin": 21, "col":  3, "value": " 0 - Sair" }
        ]
        self.tela_try_except = [
            { 'lin':  5, 'col':  3, 'value': ' 1 - ValueError' },
            { 'lin':  6, 'col':  3, 'value': ' 2 - ZeroDivisionError' },
            { 'lin': 21, 'col':  3, 'value': ' 0 - Sair' }
        ]
        self.opcoes_disponiveis = {
            '1' : self.calculadora,
            '2' : self.try_except,
            '3' : self.calculadora_2
        }
        self.opcoes = {
            '1' : { 'lin':  5, 'col':  3, 'value': ' 1 - Calculadora' },
            '2' : { 'lin':  6, 'col':  3, 'value': ' 2 - Try .. Except' },
            '3' : { 'lin':  7, 'col':  3, 'value': ' 3 - Calculadora 2 ' },
            '0' : { 'lin': 21, 'col': 43, 'value': ' 0 - Sair' }
        }
        self.opcoes_calculadora = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.opcoes_try_except = [0, 1, 2]
        self.operacoes_calculadora_2 = [ '+', '-', '*', '/']

    def iniciar(self):
        while True:
            try:
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
            except KeyboardInterrupt:
                exibir_mensagem("Por favor, saia corretamente do sistema!", lin_padrao, col_padrao, wait_key=True)

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
                if operacao not in self.opcoes_calculadora:
                    exibir_mensagem("Opção inválida. Tente novamente!", lin_padrao, col_padrao, wait_key=True)
                    continue
                if operacao == 0:
                    break
                valores = self.get_valor(operacao)
                if len(valores) == 0:
                    limpar_linha(lin_padrao, col_padrao, size_padrao)
                    exibir_mensagem("Você não informou valores!", lin_padrao, col_padrao, wait_key=True)
                    continue
                match operacao:
                    case 1:
                        result = calculos.adicao(valores)
                        texto = "da adição"
                    case 2:
                        result = calculos.subtracao(valores)
                        texto = "da subtração"
                    case 3:
                        result = calculos.multiplicacao(valores)
                        texto = "da multiplicação"
                    case 4:
                        result = calculos.divisao(valores)
                        texto = "da divisão"
                    case 5:
                        result = calculos.exponenciacao(valores)
                        texto = "da exponenciação"
                    case 6:
                        result = calculos.raiz(valores)
                        texto = "da raiz"
                    case 7:
                        result = calculos.seno(valores[0])
                        texto = "do seno"
                    case 8:
                        result = calculos.cosseno(valores[0])
                        texto = "do cosseno"

                exibir_mensagem(f"O resultado {texto} é: {result:.2f}", lin_padrao, col_padrao, wait_key=True)
                limpar_linha(lin_padrao, col_padrao, size_padrao)
            except ValueError:
                exibir_mensagem("Valor incorreto!", lin_padrao, col_padrao, wait_key=True)
                continue
        return False

    def try_except(self):
        while True:
            try:
                self.limpar_tela()
                desenhar_tela(self.tela_try_except)
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                posicionarCursor(lin_padrao, col_padrao)
                opcao = int(input('Escolha a opção desejada: '))
                if opcao == 0:
                    break
                if opcao not in self.opcoes_try_except:
                    exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                    limpar_linha(lin_padrao, col_padrao, size_padrao)
                    continue
                match opcao:
                    case 1:
                        value, msg = try_except.testar_valueError(lin_padrao, col_padrao, size_padrao)
                        if value is None:
                            exibir_mensagem(msg, lin_padrao, col_padrao, wait_key=True)
                            continue
                    case 2:
                        msg = try_except.testar_divisao_por_zero(21, 3, size_padrao)
                        exibir_mensagem(msg, lin_padrao, col_padrao, wait_key=True)
            except Exception:
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                exibir_mensagem("Opção inválida! Tente novamente!", wait_key=True)
                limpar_linha(lin_padrao, col_padrao, size_padrao)

    def calculadora_2(self):
        while True:
            try:
                self.limpar_tela()
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                valor1 = self.get_valor_unico('primeiro')
                if valor1 == 0:
                    break
                valor2 = self.get_valor_unico('segundo', 7)
                operacao = self.get_operacao(9)
                match operacao:
                    case '+':
                        result = calculos.adicao([valor1, valor2])
                        texto = 'da soma dos números'
                    case '-':
                        result = calculos.subtracao([valor1, valor2])
                        texto = 'da subtração dos números'
                    case '*':
                        result = calculos.multiplicacao([valor1, valor2])
                        texto = 'da multiplicação dos números'
                    case '/':
                        result = calculos.divisao(valor1, valor2)
                        texto = 'da divisão dos números'
                limpar_linha(11, col_padrao, size_padrao)
                exibir_mensagem(f'O resultado {texto} {valor1} e {valor2} é: {result}', 11, col_padrao, wait_key=True)
                limpar_linha(11, col_padrao, size_padrao)
                continuar = exibir_mensagem('Deseja fazer outra operação? (S/N): ', lin_padrao, col_padrao, wait_key=True)
                if continuar.upper() != 'S':
                    break
            except ValueError:
                exibir_mensagem("Entrada numérica inválida!", lin_padrao, col_padrao, wait_key=True)
                continue
            except ZeroDivisionError:
                exibir_mensagem("Não é permitida a divisão por 0", lin_padrao, col_padrao, wait_key=True)
                continue

    def get_valor(self, operacao:int=0):
        lista = []
        limpar_linha(lin_padrao, col_padrao, size_padrao)
        while True:
            try:
                limpar_linha(21, 3, size_padrao)
                posicionarCursor(21, 3)
                valor = float(input("Informe o valor (0 para encerrar): "))
                if operacao == 6 and valor == 0 and len(lista) < 2:
                    exibir_mensagem("Índice não pode ser zeros", lin_padrao, col_padrao, wait_key=True)
                    continue
                lista.append(valor)
                if (operacao == 6 and len(lista) == 2) or \
                   (operacao == 7 or operacao == 8):
                    break
            except ValueError:
                exibir_mensagem("Valor inválido!", lin_padrao, col_padrao, wait_key=True)
                limpar_linha(lin_padrao, col_padrao, size_padrao)
        return lista

    def get_valor_unico(self, texto: str, lin=5):
        while True:
            try:
                limpar_linha(lin, 3, size_padrao)
                posicionarCursor(lin, col_padrao)
                valor = float(input(f"Digite o {texto} valor: "))
                break
            except ValueError:
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                exibir_mensagem(f'Entrada inválida para o {texto} valor!', lin_padrao, col_padrao, wait_key=True)
        return valor
    
    def get_operacao(self, lin=5):
        while True:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            operacao = exibir_mensagem(f'Escolha a operação desejada: {self.operacoes_calculadora_2}: ', lin, col_padrao, wait_key=True)
            if operacao not in self.operacoes_calculadora_2:
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                exibir_mensagem("Operação inválida! Tente novamente!", lin_padrao, col_padrao, wait_key=True)
                continue
            break
        return operacao



if __name__ == "__main__":
    system('cls')
    app = Aula2405205()
    app.iniciar()
    system('cls')