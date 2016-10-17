import pygame

WIDTH, HEIGHT = 40, 40
DELAY = 500


pygame.init()
screen = pygame.display.set_mode((560, 800))
done = False

y = 30

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((0,0,0)) # Black
        y += HEIGHT
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(80 , y, WIDTH, HEIGHT))  # Rect arguments - x, y, width, height
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(120, y, WIDTH, HEIGHT))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(160, y, WIDTH, HEIGHT))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(200, y, WIDTH, HEIGHT))
        pygame.display.flip()
        pygame.time.delay(DELAY)