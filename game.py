import pygame
from tetpy import *

BLUE = (0, 128, 255)
PURPLE = (128, 0, 255)
BLACK = (0,0,0)

class GameLogic(object):
    def __init__(self, screen, BLOCK_WIDTH, BLOCK_HEIGHT, GAME_WIDTH, GAME_HEIGHT):
        self.screen = screen
        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.BLOCK_WIDTH = BLOCK_WIDTH
        self.BLOCK_HEIGHT = BLOCK_HEIGHT
        self.TG = TetrisGame(GAME_WIDTH, GAME_HEIGHT)

    def game_render(self):
        """Render the current game iteration to the user."""
        self.TG.run_iteration()
        for y in range(self.GAME_HEIGHT):
            for x in range(self.GAME_WIDTH):
                #TODO: Define colors like RED and BLUE
                if self.TG.board[y][x] == 1:  # Active piece
                    pygame.draw.rect(self.screen, BLUE, pygame.Rect(x*self.BLOCK_WIDTH, y*self.BLOCK_HEIGHT, self.BLOCK_WIDTH, self.BLOCK_HEIGHT))  # Rect arguments - x, y, width, height
                if self.TG.board[y][x] == 2:  # Inactive pieces
                    pygame.draw.rect(self.screen, PURPLE, pygame.Rect(x*self.BLOCK_WIDTH, y*self.BLOCK_HEIGHT, self.BLOCK_WIDTH, self.BLOCK_HEIGHT))  # Rect arguments - x, y, width, height

    def game_process_key(self,key):
        """Process user key inputs."""
        if key == "UP":
            self.TG.moves += ["ROTATE"]
        elif key == "LEFT":
            self.TG.moves += ["LEFT"]
        elif key == "RIGHT":
            self.TG.moves += ["RIGHT"]
        elif key == "SPACE":
            self.TG.moves += ["SPACE"]

    def game_over(self):
        """Set flag to mark game as over."""
        return self.TG.gameover

    def game_over_render(self):
        """Render the game over screen to the user."""
        statusImage = pygame.image.load("./assets/youlose.png")
        statusImage = pygame.transform.scale(statusImage, (300, 400))
        statusRect = statusImage.get_rect()
        statusRect.x = 150
        statusRect.y = (self.GAME_HEIGHT*self.BLOCK_HEIGHT) / 4
        self.screen.blit(statusImage, statusRect)
        pygame.display.flip()

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
                        if event.key == pygame.K_SPACE:
                            game_logic.game_process_key("SPACE")
            screen.fill(BLACK) # Black
            game_logic.game_render()
            if game_logic.game_over():
                done = True
            pygame.display.flip()

    game_logic.game_over_render()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

if __name__ == "__main__":
    main()
