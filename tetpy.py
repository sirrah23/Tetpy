class TetrisGame(object):

        active_piece = None
        spawn_zone = None  # Will use this later

        # Initialize the tetris game with a WIDTH x HEIGHT tetris board
        def __init__(self, WIDTH, HEIGHT):
                self.WIDTH = WIDTH
                self.HEIGHT = HEIGHT
                self.board = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

        def new_active_piece(self):
                self.active_piece = LinePiece()

        def get_direction(self):
                return (1, 0)

        def draw(self):
                self.board = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]  # Clear board
                for coordinate in self.active_piece.coordinates:
                        self.board[coordinate[0]][coordinate[1]] = 1  # Draw piece onto board

        def __str__(self):
                result = ""
                for row in self.board:
                        for col in row:
                                result += str(col)
                                result += ' '
                        result += '\n'
                return result

        def __repr__(self):
                return self.__str__()

        def run_iteration(self):
                if self.active_piece is None:
                        self.new_active_piece()
                else:
                        direction = self.get_direction()
                        self.active_piece.update(direction)
                self.draw()


class Tetromino(object):

        def update(self, direction):
                new_coordinates = []
                for coordinate in self.coordinates:
                        new_coordinates.append(tuple(x + y for x, y in zip(coordinate, direction)))
                self.coordinates = new_coordinates


class LinePiece(Tetromino):
        def __init__(self):
                self.coordinates = [(0, 4), (0, 5), (0, 6), (0, 7)]
                self.origin = (0, 6)


def main():
        TG = TetrisGame(14, 16)
        print TG
        TG.run_iteration()
        print TG
        TG.run_iteration()
        print TG
        TG.run_iteration()
        print TG
        TG.run_iteration()
        print TG
        TG.run_iteration()
        print TG

if __name__ == '__main__':
        main()
