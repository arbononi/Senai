import msvcrt
import sys
from os import system
from random import randrange

OCULTAR_CURSOR = '\033[?25l'
MOSTRAR_CURSOR = '\033[?25h'

class FinalProjectCisco:
    def __init__(self):
        self.tabuleiro =  [
            { "lin":  1, "col": 1, "value": "╔═══════╦═══════╦═══════╗" },
            { "lin":  2, "col": 1, "value": "║       ║       ║       ║" },
            { "lin":  3, "col": 1, "value": "║       ║       ║       ║" },
            { "lin":  4, "col": 1, "value": "║       ║       ║       ║" },
            { "lin":  5, "col": 1, "value": "╠═══════╬═══════╬═══════╣" },
            { "lin":  6, "col": 1, "value": "║       ║       ║       ║" },
            { "lin":  7, "col": 1, "value": "║       ║       ║       ║" },
            { "lin":  8, "col": 1, "value": "║       ║       ║       ║" },
            { "lin":  9, "col": 1, "value": "╠═══════╬═══════╬═══════╣" },
            { "lin": 10, "col": 1, "value": "║       ║       ║       ║" },
            { "lin": 11, "col": 1, "value": "║       ║       ║       ║" },
            { "lin": 12, "col": 1, "value": "║       ║       ║       ║" },
            { "lin": 13, "col": 1, "value": "╚═══════╩═══════╩═══════╝" }
        ]
        self.coordenadas = {
            '0': { 'lin':  3, 'col':  5 },
            '1': { 'lin':  3, 'col': 13 },
            '2': { 'lin':  3, 'col': 21 },
            '3': { 'lin':  7, 'col':  5 },
            '4': { 'lin':  7, 'col': 13 },
            '5': { 'lin':  7, 'col': 21 },
            '6': { 'lin': 11, 'col':  5 },
            '7': { 'lin': 11, 'col': 13 },
            '8': { 'lin': 11, 'col': 21 }
        }
        self.condicoes = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (3, 4, 6)
        ]

        self.board = ['','','','','','','','','']
        self.free = []
        self.peca_computador = 'X'
        self.peca_humano = 'O'
        self.vencedor = ''
    
    def esperar_tecla(self, ocultar_cursor: bool=True):
        if ocultar_cursor:
            print(OCULTAR_CURSOR, end="", flush=True)
        tecla = msvcrt.getch().decode("utf-8").upper()
        if ocultar_cursor:
            print(MOSTRAR_CURSOR, end="", flush=True)
        if tecla == "\r":
            tecla = ""
        return tecla

    def exibir_mensagem(self, mensagem='', lin=15, col=2, wait_key=True):
        self.limpar_linha()
        self.posicionarCursor(lin, col)
        print(mensagem, end='')
        if wait_key:
            tecla = self.esperar_tecla()
            if tecla == '\r':
                tecla = ''
            return tecla
        return None

    def posicionarCursor(self, linha: int, coluna: int):
        sys.stdout.write(f"\033[{linha};{coluna}H")
    
    def limpar_linha(self, lin=15, col=2):
        self.posicionarCursor(lin, col)
        print(' ' * 70, end='')

    def marcar_tabuleiro(self, sign, lin, col):
        self.posicionarCursor(lin, col)
        print(sign, end='')

    def iniciar(self):
        while True:
            self.desenhar_tabuleiro()
            self.board = ['','','','','','','','','']
            self.board[4] = self.peca_computador
            info = self.coordenadas.get('4')
            self.marcar_tabuleiro(self.peca_computador, info['lin'], info['col'])
            self.make_list_of_free_fields()
            human_turn = True
            while len(self.free):
                if human_turn:
                    self.enter_move()
                    winner = self.victory_for(self.peca_humano)
                else:
                    self.draw_move()
                    winner = self.victory_for(self.peca_computador)
                if winner != None:
                    break
                human_turn = not human_turn
                self.make_list_of_free_fields()
            self.limpar_linha()
            if winner is None:
                self.exibir_mensagem('Partida empatada!!!')
            elif winner == 'eu':
                self.exibir_mensagem('Eu venci!!!')
            else:
                self.exibir_mensagem('Você venceu!!!')
            continuar = self.exibir_mensagem("Deseja jogar outra partida (S/N)? ")
            if continuar.upper() != 'S':
                break
            
    def desenhar_tabuleiro(self):
        for info in self.tabuleiro:
            self.exibir_mensagem(info['value'], info['lin'], info['col'], False)

    def enter_move(self):
        ok = False
        while not ok:
            self.limpar_linha()
            self.posicionarCursor(15, 2)
            print('Faça seu movimento: ', end='')
            self.posicionarCursor(15, 22)
            move = self.esperar_tecla()
            ok = move >= '1' and move <= '9'
            if not ok:
                self.exibir_mensagem("Má jogada - repita o movimento.")
                continue
            move = int(move) - 1
            sign = self.board[move]
            ok = sign not in [self.peca_humano, self.peca_computador]
            if not ok:
                self.exibir_mensagem("Já está ocupado. Escolha outro!")
                continue
        self.board[move] = self.peca_humano
        info = self.coordenadas.get(str(move))
        if info:
            self.marcar_tabuleiro(self.peca_humano, info['lin'], info['col'])

    def make_list_of_free_fields(self):
        self.free = []
        for i in range(len(self.board)):
            if self.board[i] == '':
                self.free.append(i)
    
    def victory_for(self, sign):
        if sign == self.peca_computador:
            who = 'eu'
        elif sign == self.peca_humano:
            who = 'você'
        for x, y, z in self.condicoes:
            if self.board[x] == sign and self.board[y] == sign and self.board[z] == sign:
                return who
        return None
    
    def draw_move(self):
        self.make_list_of_free_fields()
        cnt = len(self.free)
        if cnt > 0:
            this = randrange(cnt)
            posicao = self.free[this]
            self.board[posicao] = self.peca_computador
            info = self.coordenadas.get(str(posicao))
            self.marcar_tabuleiro(self.peca_computador, info['lin'], info['col'])
            

system('cls')
app = FinalProjectCisco()
app.iniciar()
            


