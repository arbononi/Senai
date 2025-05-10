import sys
import msvcrt
from os import system as limp
from time import sleep

class ProjetoLoops():
    _lin_opcao = 0
    _col_opcao = 22

    layout = [
        { "col": 1, "value": "╔═══════════════════════════════════════╗", "loop": False },
        { "col": 1, "value": "║                                       ║", "loop": True },
        { "col": 1, "value": "╠═══════════════════════════════════════╣", "loop": False },
        { "col": 1, "value": "║ Escolha uma opção:                    ║", "loop": False },
        { "col": 1, "value": "╚═══════════════════════════════════════╝", "loop": False }

    ]
    menu = [
        { "lin":  3, "col": 3, "value": " 1 - Tabuada com While" },
        { "lin":  4, "col": 3, "value": " 2 - Tabuada em For" },
        { "lin":  5, "col": 3, "value": " 3 - For com 2 parâmetros" },
        { "lin":  6, "col": 3, "value": " 4 - For com 3 parâmetros" },
        { "lin":  7, "col": 3, "value": " 5 - Checar Números Pares Com While" },
        { "lin":  8, "col": 3, "value": " 6 - Hipótese de Collatz" },
        { "lin":  9, "col": 3, "value": " 7 - Multiplos de um número" },
        { "lin": 10, "col": 3, "value": " 8 - Impressão de números inteiros" },
        { "lin": 11, "col": 3, "value": " 9 - Imprimir Nome" },
        { "lin": 12, "col": 3, "value": "10 - Imprimir somente consoantes " },
        { "lin": 13, "col": 3, "value": "11 - Tratar Frase " },
        { "lin": 14, "col": 3, "value": " S - Sair do Sistema " }
    ]

    vogais = [ 'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ú', 'ã', 'õ', 'à', 'â', 'ô' ]
    limite = 8

    def __init__(self):
        self.opcoes = {
            "1" : self.tabuada_com_while,
            "2" : self.tabuada_com_for,
            "3" : self.for_com_2_parametros,
            "4" : self.for_com_3_parametros,
            "5" : self.checar_numeros_pares,
            "6" : self.hiposete_collatz,
            "7" : self.multiplos,
            "8" : self.imprimir_inteiros,
            "9" : self.imprimir_nome,
            "10": self.imprimir_consoantes,
            "11": self.tratar_frase,
            "S" : self.fechar
        }

    def iniciar(self):
        while True:
            limp('cls')
            self.desenha_tela()
            self.exibir_menu()
            self.posicionar_cursor(self._lin_opcao, self._col_opcao);
            opcao = input()
            if opcao == 'S':
                break
            if opcao not in self.opcoes.keys():
                print("Opção inválida!")
                sleep(1)
                continue
            acao = self.opcoes.get(opcao)
            if acao and callable(acao):
                limp('cls')
                esperar = acao()
            if esperar:
                print()
                _ = input('Pressione qualquer tecla para continuar')

    def posicionar_cursor(self, lin, col):
        sys.stdout.write(f"\033[{lin};{col}H")

    def desenha_tela(self):
        lin = 1
        for linha in self.layout:
            if linha["loop"]:
                for x in range(len(self.opcoes) + 2):
                    self.posicionar_cursor(lin, linha["col"])
                    print(linha["value"], end="")
                    lin += 1
            else:
                self.posicionar_cursor(lin, linha["col"])
                print(linha["value"], end="")
                lin += 1
            if "Escolha" in linha["value"]:
                self._lin_opcao = lin - 1

    def exibir_menu(self):
        for opcao in self.menu:
            self.posicionar_cursor(opcao["lin"], opcao["col"])
            print(opcao["value"], end="")

    def tabuada_com_while(self):
        while True:
            try:
                tabuada = int(input("Informe a tabuada desejada ou 0 para encerrar: "))
                if tabuada == 0:
                    break
                x = 1
                while x < 10:
                    print(f'{x} * {tabuada} = {x * tabuada}')
                    x += 1
                    sleep(0.5)
            except ValueError:
                print("Valor inválido!")
        return False
    
    def tabuada_com_for(self):
        while True:
            try:
                tabuada = int(input("Informe a tabuada desejada ou 0 para encerrar: "))
                if tabuada == 0:
                    break
                for x in range(1,10):
                    print(f'{x} * {tabuada} = {x * tabuada}')
                    sleep(0.5)
            except ValueError:
                print("Valor inválido!")
        return False
    
    def for_com_2_parametros(self):
        print ("For começando em 2 e indo até 10")
        for x in range(2, 11):
            print(f'x = {x}')
            sleep(0.5)
        return True
    
    def for_com_3_parametros(self):
        print("For começando em 1 e indo até 20, saltando de 2 em 2")
        for x in range(1, 20, 2):
            print(f'x = {x}')
            sleep(0.5)
        return True
    
    def hiposete_collatz(self):
        etapas = 0
        try:
            c0 = int(input('Digite um número inteiro diferente de 0: '))
            while True:
                if c0 % 2 == 0:
                    c0 = int(c0 / 2)
                else:
                    c0 = int(3 * c0 + 1)
                print(f'c0 = {c0}')
                etapas += 1
                sleep(0.5)
                if c0 == 1:
                    print(f'Etapas= {etapas}')
                    break
        except ValueError:
            print('Valor inválido!')
            sleep(2)
        return True
    
    def checar_numeros_pares(self):
        qtdPares = 0
        while True:
            try:
                numero = int(input("Digite um número: "))
                if numero % 2 == 0:
                    qtdPares += 1
                    print("Você digitou um número Par")
                else:
                    print("Você digitou um número ímpar")
                if qtdPares == 3:
                    print("Obrigado pela participação!")
                    break
            except ValueError:
                print("Número inválido!")
        return True
    
    def multiplos(self):
        print('Determinar os múltiplos de um número')
        try:
            multiplo = int(input('Informe qual número você quer os múltiplos: '))
            limite = int(input('Digite um limite: '))
            for x in range(1, limite + 1):
                if x % multiplo == 0:
                    print(x)
                    sleep(0.5)
        except ValueError:
            print('Valor inválido!')
        return True
    
    def imprimir_inteiros(self):
        while True:
            try:
                limite = int(input('Imprimir inteiros até: '))
                for i in range(limite + 1):
                    print(f'{i};', end="")
                    sleep(0.5)
                break
            except ValueError:
                print("Valor inválido")
        print()
        return True
    
    def imprimir_nome(self):
        while True:
            limp('cls')
            nome = input("Digite um nome o SAIR para encerrar: ").upper()
            if nome == "SAIR":
                break
            if nome == '':
                print("Por favor, digite um nome!")
                continue
            for letra in nome.title():
                print(letra, end="")
                sleep(0.3)
            print()
            for letra in nome.title():
                print(letra)
                sleep(0.3)
        return False
    
    def imprimir_consoantes(self):
        nome = input("Digite um nome: ")
        for letra in nome:
            if letra.lower() not in [ 'a', 'e', 'i', 'o', 'u']:
                print(letra)
        return True
    
    def tratar_frase(self):
        frase = input("Digite uma frase: ")
        palavra = None
        qtd_vogais = 0
        for letra in frase:
            if letra == " ":
               print(f'A palavra {palavra} começa com uma {"consoante" if consoante else "vogal"} e possui {qtd_vogais} vogal(is)')
               palavra = None
               qtd_vogais = 0
            else:
                if palavra is None:
                    palavra = letra
                    if letra.lower() not in self.vogais:
                        consoante = True
                    else:
                        qtd_vogais += 1
                        consoante = False
                else:
                    palavra += letra
                    if letra.lower() in self.vogais:
                        qtd_vogais += 1

        if palavra is not None:
            print(f'A palavra {palavra} começa com uma {"consoante" if consoante else "vogal"} e possui {qtd_vogais} vogal(is)')
        return True

    def fechar(self):
        pass

_app = ProjetoLoops()
_app.iniciar()
