import sys
import os
from os import system
from time import sleep
from funcoes import *
from operacoes import verificar_operacoes
import interface
import historico

class Principal:
    def __init__(self):
        if not historico.arquivo():
            historico.criar_arquivo()
        pass

    def iniciar(self):
        interface.exibir_interface()
        while True:
            interface.limpar_linha()
            exibir_conteudo("Escolha a opção desejada:", interface.lin_padrao, interface.col_padrao)
            posicionarCursor(interface.lin_padrao, 29)
            try:
                opcao = int(input())
                if opcao not in interface.opcoes_calculadora:
                    interface.limpar_linha()
                    exibir_mensagem("Opção inválida!", interface.lin_padrao, interface.col_padrao)
                    continue
            except ValueError:
                interface.limpar_linha()
                exibir_mensagem("Opção não permitida!", interface.lin_padrao, interface.col_padrao)
                continue
            if opcao == 0:
                break
            if opcao == 10:
                lista = historico.ler_historico()
                interface.exibir_historico(lista)
                continue
            valor1, valor2 = self.solicitar_valores(opcao)
            result = verificar_operacoes(opcao, valor1, valor2)
            exibir_conteudo("O resultado da operação foi:", lin=9, col=40)
            exibir_conteudo(result, lin=10, col=42)
            status = historico.salvar_historico(valor1, opcao, valor2, result)
            interface.limpar_linha()
            if status > 0:
                exibir_mensagem('Histórico salvo com sucesso!', interface.lin_padrao, interface.col_padrao)
            else:
                exibir_mensagem('Histórico não foi salvo!', interface.lin_padrao, interface.col_padrao)
                
    def solicitar_valores(self, operacao: int):
        interface.limpar_linha()
        interface.limpar_visualizacao()
        info = interface.tela_calculadora.get(str(operacao))
        exibir_conteudo(f'Operação selecionada: {info['value']}', lin=4, col=40)
        # Aguarda entrada do primeiro valor
        while True:
            try:
                exibir_conteudo('Informe o primeiro valor: ', lin=6, col=40)
                posicionarCursor(lin=6, col=66)
                valor1 = float(input())
                break
            except ValueError as ex:
                interface.limpar_linha()
                exibir_mensagem("Entrada inválida! Tente novamente", interface.lin_padrao, interface.col_padrao)
                interface.limpar_linha()
        # Aguarda entrada do segundo valor quando for o caso
        if operacao not in[7, 8, 9]:
            while True:
                try:
                    exibir_conteudo('Informe o segundo valor.: ', lin=7, col=40)
                    posicionarCursor(lin=7, col=66)
                    valor2 = float(input())
                    break
                except ValueError as ex:
                    interface.limpar_linha()
                    exibir_mensagem("Entrada inválida! Tente novamente", interface.lin_padrao, interface.col_padrao)
                    interface.limpar_linha()
        else:
            valor2 = 0
        
        return valor1, valor2
    
if __name__ == "__main__":
    system("cls")
    app = Principal()
    app.iniciar()
    interface.limpar_linha()
    exibir_conteudo("Obrigado por utilizar nosso sistema!", interface.lin_padrao, interface.col_padrao)
    sleep(3)
    system("cls")
