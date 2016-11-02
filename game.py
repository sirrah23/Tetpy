import pygame
from tetpy import *

BLOCK_WIDTH, BLOCK_HEIGHT = 40, 40
GAME_WIDTH, GAME_HEIGHT = 14, 20
TG = None

pygame.init()
screen = pygame.display.set_mode((BLOCK_WIDTH*GAME_WIDTH, BLOCK_HEIGHT*GAME_HEIGHT))
done = False

def game_initialize():
    global TG
    TG = TetrisGame(GAME_WIDTH, GAME_HEIGHT)
    TG.run_iteration()

def game_render():
    TG.run_iteration()
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            #TODO: Define colors like RED and BLUE
            if TG.board[y][x] == 1:  # Active piece
                pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x*BLOCK_WIDTH, y*BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT))  # Rect arguments - x, y, width, height
            if TG.board[y][x] == 2:  # Inactive pieces
                pygame.draw.rect(screen, (128, 0, 255), pygame.Rect(x*BLOCK_WIDTH, y*BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT))  # Rect arguments - x, y, width, height

def game_process_key(TG, key):
    if key == "UP":
        TG.moves += ["ROTATE"]
    elif key == "LEFT":
        TG.moves += ["LEFT"]
    elif key == "RIGHT":
        TG.moves += ["RIGHT"]

def game_over(TG):
    return TG.gameover

game_initialize()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        game_process_key(TG,"UP")
                    if event.key == pygame.K_DOWN:
                        game_process_key(TG,"DOWN")
                    if event.key == pygame.K_RIGHT:
                        game_process_key(TG,"LEFT")
                    if event.key == pygame.K_LEFT:
                        game_process_key(TG,"RIGHT")
        screen.fill((0,0,0)) # Black
        game_render()
        if game_over(TG):
            done = True
        pygame.display.flip()

# TODO: Display a GAME OVER screen?
