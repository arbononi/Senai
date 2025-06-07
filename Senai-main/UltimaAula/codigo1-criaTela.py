import pygame
import os

_image_library = {}

# Solicitar tipo e tamanho do objeto ao usuário
# Checar se não será maior que a tela

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image=pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

tipoObjeto = 1
raios = 50
largura = 50
altura = 50

# Inicia o pygame
pygame.init()
# Cria uma tela com o tamanho especificado
screen = pygame.display.set_mode((1000, 750))

# Controla a finalização do jogo
done = False
if tipoObjeto == 1:
    x = (screen.get_height() - (raios // 2)) // 2
    y = (screen.get_width() - (raios // 2)) // 2
else:
    x = 500
    y = 375

frame = pygame.time.Clock()
fonte = pygame.font.SysFont("Consolas", 25)

verde = (0, 255, 0)
amarelo = (255, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
preto = (0, 0, 0)
corValue = 1
white_surface = pygame.Surface((200, 100))
white_surface.fill(branco)


# Fica no loop enquanto done for falso
# Fecha quando pressiona o X na tela

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     verde = not verde
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    if corValue == 4:
                        corValue = 1
                    else:
                        corValue += 1
                case pygame.K_1:
                    tipoObjeto = 1
                case pygame.K_2:
                    tipoObjeto = 2
                case pygame.K_PAGEDOWN:
                    if tipoObjeto == 1:
                        if raios > 0:
                            raios -= 10
                        else:
                            raios = 50
                    else:
                        if largura > 0:
                            largura -= 10
                        else:
                            largura = 50
                        if altura > 0:
                           altura -= 10
                        else:
                            altura = 50
                case pygame.K_PAGEUP:
                    if tipoObjeto == 1:
                        if raios > 0:
                            raios += 10
                        else:
                            raios = 50
                    else:
                        if largura > 0:
                            largura += 10
                        else:
                            largura = 50
                        if altura > 0:
                           altura += 10
                        else:
                            altura = 50
                           
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    if tipoObjeto == 2:
        if y < -altura:
            y = screen.get_height() + altura
        elif y > screen.get_height() + altura:
            y = -altura
        
        if x < -largura:
            x = screen.get_width() + largura
        elif x > screen.get_width() + largura:
            x = -largura
    else:
        if y < -raios:
            y = screen.get_height() + raios
        elif y > screen.get_height() + raios:
            y = -raios
        
        if x < -raios:
            x = screen.get_width() + raios
        elif x > screen.get_width() + raios:
            x = -raios

    match corValue:
        case 1:
            color = verde
        case 2:
            color = amarelo
        case 3:
            color = azul
        case 4:
            color = branco

    # limpa a tela antes de desenhar
    screen.fill(preto)
    screen.blit(white_surface, (100, 100))
    imagem = get_image("perfil.jpg");
    
    screen.blit(get_image("perfil.jpg"), (300, 275))

    if tipoObjeto == 2:
       pygame.draw.rect(screen, color, pygame.Rect(x, y, largura, altura))
    else:
       pygame.draw.circle(screen, color, (x, y), raios)

    texto = fonte.render("Senai na VEIA!", True, branco)
    textox = (screen.get_width() - texto.get_width()) // 2
    textoy = (screen.get_height() - texto.get_height()) // 2
    screen.blit(texto, [textox, textoy])

    # Atualiza a tela
    pygame.display.flip()
    frame.tick(200)