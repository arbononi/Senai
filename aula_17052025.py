# Nesta aula veremos - Lista [], Tupla () e Dicionário {}
# list_dados_users = [ 'André', 'Rogério', 'Bononi']
# tupla_numeros = ( 1, 2, 3)
# dict_chave_valor = { 'nome': 'André, 'idade': 55, 'comissao': 5.5 }

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
            "12": self.tarefa_dicionario
        }
        self.menu = [
            " 1 - Listas",
            " 2 - Exclusão de itens da Lista",
            " 3 - Adicionar itens na Lista",
            " 4 - Inserir item na Lista",
            " 5 - Classificar Lista",
            " 6 - Tarefa com Listas",
            " 7 - Tuplas",
            " 8 - Tarefa com Tuplas",
            " 9 - Dicionários",
            "10 - Editar dados do Dicionário",
            "11 - Incluir nova chave no Dicionário",
            "12 - Tarefa Dicionário",
            " 0 - Sair"
        ]

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

    def iniciar(self):
        while True:
            system('cls')
            for opcoes in self.menu:
                print(opcoes)
            print()
            try:
                opcao = int(input('Escolha a opção desejada: '))
                if opcao == 0:
                    break
                acao = self.opcoes.get(str(opcao))
                if acao is None:
                    _ = input("Opção inválida!")
                    continue
                if acao and callable(acao):
                    system('cls')
                    esperar = acao()
                if esperar:
                    print('Pressione qualquer tecla para continuar...')
                    self.aguardar_tecla()
                    system('cls')
            except ValueError as ex:
                _ = input('Valor inválida! Tente novamente! ')
        system('cls')

    def listas(self):
        valores = [37,48,11,29,100,99]
        i = 0
        print("Impressão com While")
        while i < len(valores):
            print(f'Conteúdo do índice {i}: {valores[i]}')
            i += 1
        print()
        print("Impressão com For")
        i = 0
        for valor in valores:
            print(f'Conteúdo do índice {i}: {valor}')
            i += 1
        print()
        print("Imprimindo a lista direto")
        teste = valores
        teste1 = valores.copy()
        print(f'Valores: {valores} - Endereço Memória: {hex(id(valores))}')
        print(f'Testes: {teste} - Endereço Memória: {hex(id(teste))}')
        print(f'Testes1: {teste1} - Endereço Memória: {hex(id(teste1))}')
        del(valores[0])
        print(f'Valores: {valores}')
        print(f'Testes: {teste}')
        print(f'Testes1: {teste1}')

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
        lista.append(nome) # type: ignore
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

    def tarefa_dicionario(self):
        print('Solicitar ao usuário que insira as seguintes dados no sistema:')
        print('Nome: deve ser uma string')
        print('Data Nascimento: dever ser uma string')
        print('CPF: deve ser um int')
        print('Telefone: deve ser um int')
        print()
        print('Salvar as informações do usuário num dicionário()')
        print('Imprimir os dados')
        print()
        dados = { 'nome': '', 'data_nascto': '', 'cpf': 0, 'telefone': 0 }
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


        
        

app = Aula17052025()
app.iniciar()



