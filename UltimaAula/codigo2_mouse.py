import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    done = False
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    while True:
        pressed = pygame.key.get_pressed()
        alt_head = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctr_head = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]

        for event in pygame.event.get():
            match event.key:
                case pygame.K_r: mode = 'red'
                case pygame.K_g: mode = 'green'
                case pygame.K_b: mode = 'blue'

            if event.type == pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 1: radius = min(200, radius + 1)
                    case 3: radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
        
        screen.fil((0, 0, 0))
        i = 0
        
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()
        clock.tick(60)

    def drawLineBetween(screen, index, start, end, width, color_mode):
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))

        match color_mode:
            case 'blue': color = (c1, c2, c2)
            case 'red': color=(c2, c1, c1)
            