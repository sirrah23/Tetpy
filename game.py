import pygame
from tetpy import *

class GameLogic(object):
    def __init__(self, screen, BLOCK_WIDTH, BLOCK_HEIGHT, GAME_WIDTH, GAME_HEIGHT):
        self.screen = screen
        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.BLOCK_WIDTH = BLOCK_WIDTH
        self.BLOCK_HEIGHT = BLOCK_HEIGHT
        self.TG = TetrisGame(GAME_WIDTH, GAME_HEIGHT)
        self.BLUE = (0, 128, 255)
        self.PURPLE = (128, 0, 255)

    def game_render(self):
        self.TG.run_iteration()
        for y in range(self.GAME_HEIGHT):
            for x in range(self.GAME_WIDTH):
                #TODO: Define colors like RED and BLUE
                if self.TG.board[y][x] == 1:  # Active piece
                    pygame.draw.rect(self.screen, self.BLUE, pygame.Rect(x*self.BLOCK_WIDTH, y*self.BLOCK_HEIGHT, self.BLOCK_WIDTH, self.BLOCK_HEIGHT))  # Rect arguments - x, y, width, height
                if self.TG.board[y][x] == 2:  # Inactive pieces
                    pygame.draw.rect(self.screen, self.PURPLE, pygame.Rect(x*self.BLOCK_WIDTH, y*self.BLOCK_HEIGHT, self.BLOCK_WIDTH, self.BLOCK_HEIGHT))  # Rect arguments - x, y, width, height

    def game_process_key(self,key):
        if key == "UP":
            self.TG.moves += ["ROTATE"]
        elif key == "LEFT":
            self.TG.moves += ["LEFT"]
        elif key == "RIGHT":
            self.TG.moves += ["RIGHT"]

    def game_over(self):
        return self.TG.gameover

def main():
    BLOCK_WIDTH, BLOCK_HEIGHT = 40, 40
    GAME_WIDTH, GAME_HEIGHT = 14, 20

    pygame.init()
    screen = pygame.display.set_mode((BLOCK_WIDTH*GAME_WIDTH, BLOCK_HEIGHT*GAME_HEIGHT))
    done = False

    game_logic = GameLogic(screen, BLOCK_WIDTH, BLOCK_HEIGHT, GAME_WIDTH, GAME_HEIGHT)
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            game_logic.game_process_key("UP")
                        if event.key == pygame.K_DOWN:
                            game_logic.game_process_key("DOWN")
                        if event.key == pygame.K_RIGHT:
                            game_logic.game_process_key("LEFT")
                        if event.key == pygame.K_LEFT:
                            game_logic.game_process_key("RIGHT")
            screen.fill((0,0,0)) # Black
            game_logic.game_render()
            if game_logic.game_over():
                done = True
            pygame.display.flip()

    # TODO: Display a GAME OVER screen?

if __name__ == "__main__":
    main()
