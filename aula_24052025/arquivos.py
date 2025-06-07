import sys
import os
from pathlib import Path
from utils.my_functions import *


lin_padrao = 24
col_padrao = 3
size_padrao = 77

class Arquivos:
    def __init__(self):
        self.limpar_centro_tela = { 'lin': 4, 'col': 2, 'value': ' ' * 79 }
        self.tela_arquivos = [
            { 'lin':  5, 'col': 3, 'value': ' 1- Ler o arquivo '},
            { 'lin':  6, 'col': 3, 'value': ' 2- Escrever no arquivo' },
            { 'lin':  7, 'col': 3, 'value': ' 3- Adicionar no arquivo' },
            { 'lin':  8, 'col': 3, 'value': ' 4- Digitar dados' },
            { 'lin':  9, 'col': 3, 'value': ' 5- Ler dados' },
            { 'lin': 10, 'col': 3, 'value': ' 6- Apagar dados' },
            { 'lin': 21, 'col': 3, 'value': ' 0- Retornar' }
        ]
        self.dados_user = [
            { 'lin': 5, 'col': 3, 'value': 'Nome ......: ' },
            { 'lin': 6, 'col': 3, 'value': 'Data Nascto: ' },
            { 'lin': 7, 'col': 3, 'value': 'CPF .......: ' },
            { 'lin': 8, 'col': 3, 'value': 'Telefone ..: ' }
        ]
        self.exibir_dados = [
            { 'lin':  3, 'col': 10, 'value': '╦' },
            { 'lin':  3, 'col': 40, 'value': '╦' },
            { 'lin':  3, 'col': 53, 'value': '╦' },
            { 'lin':  3, 'col': 67, 'value': '╦' },
            { 'lin':  4, 'col':  3, 'value': 'Codigo ║ Nome                        ║ Data Nasc. ║ CPF         ║ Telefone    ' },
            { 'lin':  5, 'col':  1, 'value': '╠════════╬═════════════════════════════╬════════════╬═════════════╬═════════════╣' },
            { 'lin':  6, 'col':  1, 'value': '║        ║                             ║            ║             ║             ║' },
            { 'lin': 23, 'col':  1, 'value': '╠════════╩═════════════════════════════╩════════════╩═════════════╩═════════════╣' }
        ]
        self.opcoes = {
            '1' : self.ler_arquivo,
            '2' : self.escrever,
            '3' : self.adicionar,
            '4' : self.digitar_dados,
            '5' : self.ler_dados,
            '6' : self.apagar_dados
        }
        

    def iniciar(self):
        while True:
            try:
                self.limpar_tela()
                desenhar_tela(layout=self.tela_arquivos)
                exibir_mensagem("Escolha a opção desejada: ", lin_padrao, col_padrao, wait_key=False)
                posicionarCursor(lin_padrao, 29)
                opcao = input()
                if opcao == '0':
                    break
                acao = self.opcoes.get(opcao)
                if not acao:
                    limpar_linha(lin_padrao, col_padrao, size_padrao)
                    exibir_mensagem("Opção inválida. Tente novamente!", lin_padrao, col_padrao)
                    continue
                if acao and callable(acao):
                    esperar = acao()
                if esperar:
                    esperar_tecla()
            except KeyboardInterrupt:
                exibir_mensagem("Por favor, saia corretamente do sistema!", lin_padrao, col_padrao)
            except ValueError:
                exibir_mensagem("Opção inválida", lin_padrao, col_padrao)

    def limpar_tela(self):
        exibir_conteudo("═",  3, 41)
        info = self.limpar_centro_tela
        for lin in range(4, 23):
            exibir_conteudo(info['value'], lin, info['col'])
        exibir_conteudo("═", 23, 41)

    def ler_arquivo(self):
        self.limpar_tela()
        lin = 3
        with open('aula_24052025/Dados/teste.txt', 'r', encoding="utf-8") as arquivo:
            for linha in arquivo:
                lin += 1
                exibir_conteudo(linha, lin, col_padrao)
                if lin == 24:
                    exibir_mensagem("Pressione qualquer tecla para continuar", lin_padrao, col_padrao)
                    self.limpar_tela()
        exibir_mensagem("Fim do arquivo", lin_padrao, col_padrao)
        return False

    def escrever(self):
        with open('aula_24052025/Dados/teste.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('Salvando dados no arquivo\n')

    def adicionar(self):
        with open('aula_24052025/Dados/teste.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write("Essa é uma nova linha no varquivo\n")

    def digitar_dados(self):
        self.limpar_tela()
        nome_arquivo = "aula_24052025/Dados/Dados_user.txt"
        registro = 0
        if not Path.exists(Path(nome_arquivo)):
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write('Dados de usuários\n')
        else:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
            registro = len(linhas) - 1

        desenhar_tela(self.dados_user)
        while True:
            self.limpar_dados_user()
            nome, cancelar = self.get_nome()
            if cancelar:
                break
            data_nasc, cancelar = self.get_datanasc()
            if cancelar:
                break
            cpf, cancelar = self.get_cpf()
            if cancelar:
                break
            telefone, cancelar = self.get_telefone()
            if cancelar:
                break
            confirmar = self.get_escolha("Confima os dados (S/N)? ")
            if confirmar == 'S':
                registro += 1
                fl_ok = self.gravar_registro(nome_arquivo, registro, nome, data_nasc, cpf, telefone)
                if fl_ok:
                    limpar_linha(lin_padrao, col_padrao, size_padrao)
                    exibir_mensagem('Dados inseridos com sucesso!', lin_padrao, col_padrao)
                    continuar = self.get_escolha('Deseja continuar registrando (S/N)? ')
                    if continuar != 'S':
                        break

    def limpar_dados_user(self):
        for i in range(5,9):
            exibir_conteudo(' ' * 64, i, 16)

    def ler_dados(self):
        self.limpar_tela()
        desenhar_tela(self.exibir_dados, 6, 23)
        limpar_linha(lin_padrao, col_padrao, size_padrao)
        nome_arquivo = "aula_24052025/Dados/Dados_user.txt"
        registro = 0
        if not Path.exists(Path(nome_arquivo)):
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            exibir_mensagem(f'Arquivo {nome_arquivo} não encontrado', lin_padrao, col_padrao)
        else:
            lin = 5
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    if linha.__contains__('Dados'):
                        continue
                    dados = linha.split("|")
                    lin += 1
                    exibir_conteudo(dados[0].rjust(6, ' '), lin, col_padrao)
                    if len(dados[1]) > 26:
                       exibir_conteudo(dados[1][26], lin, 12)
                    else:
                        exibir_conteudo(dados[1], lin, 12)
                    exibir_conteudo(dados[2], lin, 42)
                    exibir_conteudo(dados[3], lin, 55)
                    exibir_conteudo(dados[4], lin, 69)
                    if lin == 22:
                        limpar_linha(lin_padrao, col_padrao, size_padrao)
                        exibir_mensagem("Pressione qualquer tecla para continuar...", lin_padrao, col_padrao)
                        limpar_linha(lin_padrao, col_padrao, size_padrao)
                        lin = 5
        limpar_linha(lin_padrao, col_padrao, size_padrao)
        exibir_mensagem("Fim de arquivo", lin_padrao, col_padrao)
        limpar_linha(lin_padrao, col_padrao, size_padrao)
        for info in self.exibir_dados:
            match info['lin']:
                case 3:
                    exibir_conteudo("═", info['lin'], info['col'])
                    exibir_conteudo("═", 23, info['col'])
                case 5:
                    exibir_conteudo("║", 5, 1)
                    exibir_conteudo("║", 5, 81)
    
    def apagar_dados(self):
        while True:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            mensagem = 'Digite a senha para apagar os dados: '
            exibir_mensagem(mensagem, lin_padrao, col_padrao, wait_key=False)
            posicionarCursor(lin_padrao, col_padrao + len(mensagem))
            senha = input()
            if senha == '':
                break
            if senha != '123456':
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                exibir_mensagem('Senha inválida! Tente novamente', lin_padrao, col_padrao)
                continue
            nome_arquivo = "aula_24052025/Dados/Dados_user.txt"
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                pass
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            exibir_mensagem('Dados excluídos com sucesso!', lin_padrao, col_padrao)
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            break
        return False

    def get_nome(self):
        cancelar = False
        while True:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            exibir_conteudo('Digite CANCELAR para encerrar', lin_padrao, col_padrao)
            exibir_conteudo("→", 5, 2)
            posicionarCursor(5, 16)
            nome = input().title()
            if nome.upper() == 'CANCELAR':
                cancelar = True
            break
        exibir_conteudo(" ", 5, 2)
        return nome, cancelar

    def get_datanasc(self):
        cancelar = False
        while True:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            exibir_conteudo('Digite CANCELAR para encerrar', lin_padrao, col_padrao)            
            exibir_conteudo("→", 6, 2)
            posicionarCursor(6, 16)
            data_nasc = input()
            if data_nasc.upper() == 'CANCELAR':
                cancelar = True
            break
        exibir_conteudo(" ", 6, 2)
        return data_nasc, cancelar
    
    def get_cpf(self):
        cancelar = False
        while True:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            exibir_conteudo('Digite CANCELAR para encerrar', lin_padrao, col_padrao)            
            exibir_conteudo("→", 7, 2)
            posicionarCursor(7, 16)
            cpf = input()
            if cpf.upper() == 'CANCELAR':
                cancelar = True
            break
        exibir_conteudo(" ", 7, 2)
        return cpf, cancelar

    def get_telefone(self):    
        cancelar = False
        while True:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            exibir_conteudo('Digite CANCELAR para encerrar', lin_padrao, col_padrao)            
            exibir_conteudo("→", 8, 2)
            posicionarCursor(8, 16)
            telefone = input()
            if telefone.upper() == 'CANCELAR':
                cancelar = True
            break
        exibir_conteudo(" ", 8, 2)
        return telefone, cancelar

    def get_escolha(self, texto):
        while True:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            confirmar = exibir_mensagem(texto, lin_padrao, col_padrao, wait_key=True)
            if confirmar.upper() not in ('S', 'N'):
                limpar_linha(lin_padrao, col_padrao, size_padrao)
                exibir_mensagem("Opção inválida", lin_padrao, col_padrao, wait_key=True)
                continue
            break
        return confirmar.upper()

    def gravar_registro(self, nome_arquivo, registro, nome, data_nasc, cpf, telefone):
        try:
            with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
                stat = arquivo.write(f'{registro}|{nome}|{data_nasc}|{cpf}|{telefone}\n')
            return stat > 0
        except IOError as error:
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            exibir_mensagem(f'Erro ao salvar o registro: {error}', lin_padrao, col_padrao)
            limpar_linha(lin_padrao, col_padrao, size_padrao)
            return False

