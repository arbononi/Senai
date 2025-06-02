#P111 - Autor: Caune
# "Criar novo arquivo para armazenamento do historico"
# Revisor - André
#P122 - Autor:Viviane
# "Criar função que verifica se ja existe arquivo"
# Revisor - Nathan

import os

nome_do_arquivo = "historico.txt"

simbolo_operacoes = [ '+', '-', '*', '/', '**', '\u221A', 'sin', 'cos', 'tan' ]

def arquivo():
    if os.path.isfile(nome_do_arquivo):
        return True
    return False

def criar_arquivo():
    with open(nome_do_arquivo, 'w', encoding='utf-8') as hist:
        pass

def salvar_historico(valor1, operacao, valor2, result):
    conteudo = set_conteudo(valor1, operacao, valor2, result)
    with open(nome_do_arquivo, 'a', encoding='utf-8') as hist:
        status = hist.write(f'{conteudo}\n')
    return status > 0

def ler_historico():
    with open(nome_do_arquivo, "r", encoding='utf-8') as hist:
        lista = hist.readlines()
    return lista

def set_conteudo(valor1, operacao, valor2, result):
    simbolo = simbolo_operacoes[(operacao - 1)]
    if operacao in [7, 8, 9]:
        conteudo = f'{simbolo} {valor1} = {result}'
    else:
        conteudo = f'{valor1} {simbolo} {valor2} = {result}'
    return conteudo
    