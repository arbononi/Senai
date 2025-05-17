# Nesta aula veremos - Lista [], Tupla () e Dicionário {}
# list_dados_users = [ 'André', 'Rogério', 'Bononi']
# tupla_numeros = ( 1, 2, 3)
# dict_chave_valor = { 'nome': 'André, 'idade': 55, 'comissao': 5.5 }

import sys
import msvcrt
from os import system
from time import sleep
from datetime import datetime

class Aula17052025:
    def __init__(self):
        self.opcoes = {
            "1": self.listas,
            "2": self.excluir_item,
            "3": self.adicionar_item,
            "4": self.inserir_item,
            "5": self.classificar_lista,
            "6": self.tarefa_lista,
            "7": self.tuplas,
            "8": self.tarefa_tupla,
            "9": self.dicionarios,
            "10": self.editar_dicionario,
            "11": self.incluir_nova_chave,
            "12": self.tarefa_dicionario_1,
            "13": self.festa_aniversario,
            "14": self.funcoes
        }
        self.dict_menu = [
            { "lin" :  5, "col" :  3, "value": " 1 - Listas" },
            { "lin" :  6, "col" :  3, "value": " 2 - Exclusão de itens da Lista" },
            { "lin" :  7, "col" :  3, "value": " 3 - Adicionar itens na Lista" },
            { "lin" :  8, "col" :  3, "value": " 4 - Inserir item na Lista" },
            { "lin" :  9, "col" :  3, "value": " 5 - Classificar Lista" },
            { "lin" : 10, "col" :  3, "value": " 6 - Tarefa com Listas" },
            { "lin" : 11, "col" :  3, "value": " 7 - Tuplas" },
            { "lin" : 12, "col" :  3, "value": " 8 - Tarefa com Tuplas" },
            { "lin" : 13, "col" :  3, "value": " 9 - Dicionários" },
            { "lin" : 14, "col" :  3, "value": "10 - Editar dados do Dicionário" },
            { "lin" : 15, "col" :  3, "value": "11 - Incluir nova chave no Dicionário" },
            { "lin" :  5, "col" : 44, "value": "12 - Tarefa Dicionário - 1" },
            { "lin" :  6, "col" : 44, "value": "13 - Festa de Aniversário" },
            { "lin" :  7, "col" : 44, "value": "14 - Funções" },
            { "lin" : 15, "col" : 44, "value": " 0 - Sair" },
        ]
        self.lista_convidados = [
            'André', 'Elenice', 'Carla', 'Júnior',
            'Iraide', 'Sônia - Prima',
            'Dinei', 'Simone', 'Camilly', 'Gabriel',
            'D. Maria', 'Seo Jove',
            'Lucimar', 'Wanderley', 'Douglas', 'Maria Raquel',
            'Eliete', 'Roberta',
            'Gilberto', 'Sônia Cunhada', 'Igor',
            'Maira', 'Felipe', 'Beatriz',
            'Tatiane', 'Daniel', 'Igor',
            'Silvana', 'Solange', 'Silvinha'
        ]
        self.tela_principal = [
            { "lin":  1, "col": 1, "value": "╔══════════════════════════════════════════════════════════════════════════════╗" },
            { "lin":  2, "col": 1, "value": "║                       MENU PRINCIPAL - AULA 17/05/2025                       ║" },
            { "lin":  3, "col": 1, "value": "╠════════════════════════════════════════╦═════════════════════════════════════╣" },
            { "lin":  4, "col": 1, "value": "║                                        ║                                     ║" },
            { "lin": 17, "col": 1, "value": "╠════════════════════════════════════════╩═════════════════════════════════════╣" },
            { "lin": 18, "col": 1, "value": "║ Escolha a opção desejada:                                                    ║" },
            { "lin": 19, "col": 1, "value": "╚══════════════════════════════════════════════════════════════════════════════╝" }
        ]
        self.tela_tarefas = [
            { "lin":  3, "col": 42, "value": "═" },
            { "lin":  4, "col":  1, "value": "║                                                                              ║"},
            { "lin": 17, "col": 42, "value": "═" },
        ]

    def desenhar_tela(self):
        system('cls')
        for info in self.tela_principal:
            if info["lin"] == 4:
                lin = 4
                while lin < 17:
                    self.exibir_conteudo(info["value"], lin, info["col"])
                    lin += 1
            else:
                self.exibir_conteudo(info["value"], info["lin"], info["col"])
        for info in self.dict_menu:
            self.exibir_conteudo(info["value"], info["lin"], info["col"])
        
    def limpar_tela(self):
        for info in self.tela_tarefas:
            if info["lin"] == 4:
                lin = info["lin"]
                while lin < 17:
                   self.exibir_conteudo(info["value"], lin, info["col"])
                   lin += 1
            else:
                self.exibir_conteudo(info["value"], info["lin"], info["col"])

    def get_nome(self):
        while True:
            nome = input('Digite seu Nome: ')
            if nome == '':
                print('Por favor, digite seu nome.')
                self.aguardar_tecla()
                continue
            break
        return nome
    
    def get_data_nascto(self):
        while True:
            data_nascto = input('Digite sua data de nascimento (DD/MM/YYYY): ')
            if data_nascto == '':
                print('Por favor, informe sua data de nascimento (não conto pra ninguém!!!)')
                self.aguardar_tecla()
                continue
            try:
                data = datetime.strptime(data_nascto, '%d/%m/%Y')
                break
            except ValueError:
                print('Data inválida!')
        return data_nascto
    
    def get_int(self, texto):
        while True:
            try:
                valor = int(input(f'Digite o número do seu {texto}: '))
                break
            except ValueError:
                print('Valor inválido!')
        return valor

    def aguardar_tecla(self):
        msvcrt.getch()

    def exibir_conteudo(self, conteudo, lin, col):
        self.posicionarCursor(lin, col)
        print(conteudo)

    def posicionarCursor(self, linha: int, coluna: int):
        sys.stdout.write(f"\033[{linha};{coluna}H")

    def iniciar(self):
        while True:
            self.desenhar_tela()
            try:
                self.exibir_conteudo("Escolha a opção desejada: ", 18, 3)
                self.posicionarCursor(18, 29)
                opcao = int(input())
                if opcao == 0:
                    break
                acao = self.opcoes.get(str(opcao))
                if acao is None:
                    _ = input("Opção inválida!")
                    continue
                if acao and callable(acao):
                    self.limpar_tela()
                    esperar = acao()
                if esperar:
                    self.exibir_conteudo('Pressione qualquer tecla para continuar...', 18, 3)
                    self.posicionarCursor(18, 46)
                    self.aguardar_tecla()
            except ValueError as ex:
                _ = input('Valor inválida! Tente novamente! ')
        system('cls')

    def listas(self):
        valores = [37,48,11,29,100,99]
        i = 0
        lin = 4
        self.exibir_conteudo("Impressão com While", lin, 3)
        lin += 1
        while i < len(valores):
            lin += 1
            self.exibir_conteudo(f'Conteúdo do índice {i}: {valores[i]}', lin, 3)
            i += 1
        lin = 4
        self.exibir_conteudo("Impressão com For", lin, 30)
        i = 0
        lin += 1
        for valor in valores:
            lin += 1
            self.exibir_conteudo(f'Conteúdo do índice {i}: {valor}', lin, 30)
            i += 1
        lin += 2
        self.exibir_conteudo("Imprimindo a lista direto", lin, 3)
        teste = valores
        teste1 = valores.copy()
        lin += 1
        self.exibir_conteudo(f'Valores: {valores} - Endereço Memória: {hex(id(valores))}', lin, 3)
        lin += 1
        self.exibir_conteudo(f'Testes: {teste} - Endereço Memória: {hex(id(teste))}', lin, 3)
        self.exibir_conteudo(f'Testes1: {teste1} - Endereço Memória: {hex(id(teste1))}', lin, 3)
        # del(valores[0])
        # print(f'Valores: {valores}')
        # print(f'Testes: {teste}')
        # print(f'Testes1: {teste1}')

        return True

    def excluir_item(self):
        print("Excluindo itens da lista")
        lista = [1, 2, 3, 4, 5, 6]
        continuar = 'S'
        while continuar == 'S':
            print(f'A lista contém {len(lista)} itens que são: {lista}')
            try:
                indice = int(input('Digite a posição do item que deseja excluir (valor inicial = 0): '))
                if indice > (len(lista) - 1):
                    print('Você digitou um valor maior que o permitido! ')
                    self.aguardar_tecla()
                    continue
                del(lista[indice])
                if len(lista) == 0:
                    print("Você excluiu todos os itens da lista!")
                    break
                while True:
                    continuar = input('Valor excluído com sucesso! Deseja continuar excluindo (S/N)? ').upper()
                    if continuar not in ['S','N']:
                        print("Opção inválida!")
                        sleep(1)
                        continue
                    break
            except ValueError as ex:
                print('Valor inválido!')
            
        print("Obrigado por brincar comigo!!! Até a próxima!")
        return True

    def adicionar_item(self):
        print('Adicionando item à lista')
        lista = [1, 2, 3, 4, 5, 6]
        print(f'A lista contém {len(lista)} que são: {lista}')
        sleep(1)
        nome = input('Qual é seu nome? ')
        print(f'Obrigado, {nome.title()}. Agora você faz parte da minha lista!!!')
        lista.append(nome)
        print(f'A lista contém {len(lista)} que são: {lista}')
        return True
    
    def inserir_item(self):
        print("Inserindo item numa posição da lista!")
        lista = [1, 2, 3, 4, 5, 6]
        print(f'A lista contém {len(lista)} que são: {lista}')
        nome = input("Digite seu nome: ")
        while True:
            try:
                indice = int(input(f"Em qual posição você deseja inserir o valor {nome}? "))
                if indice > len(lista):
                    print('Índice não permitida!')
                    self.aguardar_tecla()
                    continue
                break
            except ValueError as ex:
                print('Valor inválido!')
                self.aguardar_tecla()
                continue
        lista.insert(indice, nome)
        print(f'Agora a lista contém {len(lista)} que são: {lista}')
        return True

    def classificar_lista(self):
        lista = ['André', 'Rogério', 'Bononi']
        print(f'A lista atual está assim: {lista}')
        print('Vou classificá-la na ordem crescente: ....')
        sleep(1.5)
        lista.sort()
        print()
        print(f'Agora a lista está ordenada: {lista}')
        print()
        print('Agora vou classificá-la em ordem descrescente...')
        sleep(1.5)
        lista.sort(reverse=True)
        print()
        print(f'Agora na ordem descrescente: {lista}')
        return True

    def tarefa_lista(self):
        print('Solicitar ao usuário que insira as seguintes dados no sistema:')
        print('Nome: deve ser uma string')
        print('Data Nascimento: dever ser uma string')
        print('CPF: deve ser um int')
        print('Telefone: deve ser um int')
        print()
        print('Salvar as informações do usuário numa lista[]')
        print('Imprimir os dados')
        print('Deletar o CPF do usuário e reimprimir os dados')
        dados_user = []
        dados_user.append(self.get_nome())
        dados_user.append(self.get_data_nascto())
        dados_user.append(self.get_int('CPF'))
        dados_user.append(self.get_int('Telefone'))
        print()
        print('Os dados inseridos foram: ')
        print(f'Nome...........: {dados_user[0]}')
        print(f'Data Nascimento: {dados_user[1]}')
        print(f'No. CPF .......: {dados_user[2]}')
        print(f'Telefone ......: {dados_user[3]}')
        sleep(1)
        print()
        print('Agora foi excluir o dado CPF')
        sleep(1)
        print('Excluindo....')
        del(dados_user[2])
        print()
        print('Imprimindo dados atualizados:')
        print(f'Nome...........: {dados_user[0]}')
        print(f'Data Nascimento: {dados_user[1]}')
        print(f'Telefone ......: {dados_user[2]}')
        return True

    def tuplas(self):
        print('Entendendo Tuplas')
        print('Vou criar a tupla chamada dados com os seguintes valores:')
        print('André, 03/12/1969, 12345678901, 16999999999')
        dados = ('André', '03/12/1969', 12345678901, 16999999999)
        print('Tupla criada')
        print(dados)
        return True
    
    def tarefa_tupla(self):
        print('Solicitar ao usuário que insira as seguintes dados no sistema:')
        print('Nome: deve ser uma string')
        print('Data Nascimento: dever ser uma string')
        print('CPF: deve ser um int')
        print('Telefone: deve ser um int')
        print()
        print('Salvar as informações do usuário numa tupla()')
        print('Imprimir os dados')
        print()
        print('Insira seus dados conforme solicitado')
        nome = self.get_nome()
        data_nascto = self.get_data_nascto()
        num_cpf = self.get_int('CPF')
        telefone = self.get_int('Telefone')
        tupla = ( nome, data_nascto, num_cpf, telefone)
        print()
        print('Os dados inseridos foram: ')
        print(f'Nome...........: {tupla[0]}\nData Nascimento: {tupla[1]}\nNo. CPF .......: {tupla[2]}\nTelefone ......: {tupla[3]}\n')
        return True

    def dicionarios(self):
        print('Entendendo dicionários...')
        info = { 'nome': 'André', 'data_nascto': '17/05/2025', 'cpf': 12345678901, 'telefone': 12345678901 }
        print(f'Dados: {info}\n')
        print('Dados por linha')
        for chave, valor in info.items():
            print(f'{chave}: {valor}')
        print()
        return True
        
    def editar_dicionario(self):
        dados = { 'nome': 'André', 'data_nascto': '17/05/2025', 'cpf': 12345678901, 'telefone': 12345678901 }        
        print('Editando dados em dicionários: ')
        print(f"Dado o dicinário dados: {dados}")
        sleep(1)
        print('Vamos alterar o nome')
        sleep(1)
        dados['nome'] = 'Rogério'
        print(f'Nome alterado: {dados}\n')
        return True

    def incluir_nova_chave(self):
        dados = { 'nome': 'André', 'data_nascto': '17/05/2025', 'cpf': 12345678901, 'telefone': 12345678901 }        
        print('Inserindo nova chave em dicionários: ')
        print(f"Dado o dicinário dados: {dados}")
        sleep(1)
        print('Vamos incluir o endereço')
        sleep(1)
        dados['endereco'] = 'Rua Barão do Rio Branco, 1100, Centro - Sertãozinho - SP'
        print(f'Novo dicinário dados: {dados}\n')
        return True

    def tarefa_dicionario_1(self):
        print('Solicitar ao usuário que insira as seguintes dados no sistema:')
        print('Nome: deve ser uma string')
        print('Data Nascimento: dever ser uma string')
        print('CPF: deve ser um int')
        print('Telefone: deve ser um int')
        print()
        print('Salvar as informações do usuário num dicionário()')
        print('Imprimir os dados')
        print()
        dados = {}
        print('Insira seus dados conforme solicitado')
        dados['nome'] = self.get_nome()
        dados['data_nascto'] = self.get_data_nascto()
        dados['cpf'] = self.get_int('CPF')
        dados['telefone'] = self.get_int('Telefone')
        print()
        print('Os dados inseridos foram: ')
        print(f'Nome...........: {dados['nome']}\nData Nascimento: {dados['data_nascto']}\n\
No. CPF .......: {dados['cpf']}\nTelefone ......: {dados['telefone']}\n')
        return True

    def festa_aniversario(self):
        print('Festa de Aniversário\n')
        convidados = {}
        i = 0
        while i < 30:
            for nome in self.lista_convidados:
                print('Digite seu nome: ', end='')
                for letra in nome:
                    print(letra, end='')
                    sleep(0.1)
                i += 1
                convidados[f"Convidado_{i}"] = nome
                print(f'\nConvidado No {i} - {nome} registrou sua entrada!')
            # nome = self.get_nome()
            # if nome == "12345":
            #     break
            
        for chave, valor in convidados.items():
            print(f'{chave} - {valor}')
        return True

    def funcoes(self):
        print('Função ainda não implementada...\n')
        return True
        
app = Aula17052025()
app.iniciar()



