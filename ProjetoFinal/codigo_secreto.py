#P125 - Autor:Brian
# "Criar código (cheat) que habilita um jogo OBS:. codigo 12345678"
# Revisor - Nathan
import pygame
import random

def iniciar_game():
    pygame.init()
    
    branco = (255, 255, 255)
    amarelo = (255, 255, 102)
    preto = (0, 0, 0)
    vermelho = (213, 50, 80)
    verde = (0, 255, 0)
    azul = (50, 153, 213)

    largura = 600
    altura = 400

    tamanho_bloco = 20
    velocidade = 10

    fonte = pygame.font.SysFont("bahnschrift", 25)
    placar_fonte = pygame.font.SysFont("comicsansms", 35)

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Jogo da Cobrinha')

    def mostrar_pontuacao(pontos):
        valor = placar_fonte.render(f"Pontuação: {pontos}", True, amarelo)
        tela.blit(valor, [10, 10])

    def desenhar_cobra(tamanho_bloco, lista_cobra):
        for x in lista_cobra:
            pygame.draw.rect(tela, preto, [x[0], x[1], tamanho_bloco, tamanho_bloco])

    def mensagem_final(msg, cor, linha):
        texto = fonte.render(msg, True, cor)
        tela.blit(texto, [largura / 6 - 20, linha])

    def gameLoop():
        fim_de_jogo = False
        game_over = False

        x = largura / 2
        y = altura / 2
        x_mudanca = 0
        y_mudanca = 0

        lista_cobra = []
        comprimento_cobra = 1

        comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
        comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

        clock = pygame.time.Clock()

        while not fim_de_jogo:

            while game_over:
                tela.fill(azul)
                linha = altura / 3
                mensagem_final("Você perdeu!", vermelho, linha)
                linha = altura / 3 + 40
                mensagem_final("Pressione C para jogar novamente", branco, linha)
                linha = altura / 3 + 80
                mensagem_final("Ou Q para sair", branco, linha)
                mostrar_pontuacao(comprimento_cobra - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            fim_de_jogo = True
                            game_over = False
                            break
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fim_de_jogo = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_mudanca = -tamanho_bloco
                        y_mudanca = 0
                    elif event.key == pygame.K_RIGHT:
                        x_mudanca = tamanho_bloco
                        y_mudanca = 0
                    elif event.key == pygame.K_UP:
                        y_mudanca = -tamanho_bloco
                        x_mudanca = 0
                    elif event.key == pygame.K_DOWN:
                        y_mudanca = tamanho_bloco
                        x_mudanca = 0

            if x >= largura or x < 0 or y >= altura or y < 0:
                game_over = True

            x += x_mudanca
            y += y_mudanca
            tela.fill(azul)
            pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
            corpo_cobra = [x, y]
            lista_cobra.append(corpo_cobra)

            if len(lista_cobra) > comprimento_cobra:
                del lista_cobra[0]

            for bloco in lista_cobra[:-1]:
                if bloco == corpo_cobra:
                    game_over = True

            desenhar_cobra(tamanho_bloco, lista_cobra)
            mostrar_pontuacao(comprimento_cobra - 1)

            pygame.display.update()

            if x == comida_x and y == comida_y:
                comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
                comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
                comprimento_cobra += 1

            clock.tick(velocidade)

        pygame.quit()
        # quit()

    gameLoop()