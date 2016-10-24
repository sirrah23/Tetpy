class TetrisGame(object):

        active_piece = None

        # Initialize the tetris game with a WIDTH x HEIGHT tetris board
        def __init__(self, WIDTH, HEIGHT):
                self.WIDTH = WIDTH
                self.HEIGHT = HEIGHT
                self.board = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

        def new_active_piece(self):
                self.active_piece = LinePiece()

        def get_direction(self):
                return (0, 1)

        def draw(self):
                self.board = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]  # Clear board
                for coordinate in self.active_piece.coordinates:
                        self.board[coordinate[0]][coordinate[1]] = 1  # Draw piece onto boar

        # Determine if the current piece is within the board or not
        def active_within_board(self):
                if not self.active_piece:
                        return False
                within_board = True
                for coordinate in self.active_piece.coordinates:
                        within_board = within_board and coordinate[0] >= 0\
                                        and coordinate[0] < self.HEIGHT and coordinate[1] >= 0 and\
                                        coordinate[1] < self.WIDTH
                        if not within_board:
                                break
                return within_board


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
                        # Try to move the piece and if it fails don't move
                        direction = self.get_direction()
                        old_coordinates = self.active_piece.coordinates
                        old_origin = self.active_piece.origin
                        self.active_piece.update(direction)
                        if not self.active_within_board():
                                self.active_piece.coordinates = old_coordinates
                                self.active_piece.origin = old_origin
                self.draw()


class Tetromino(object):

        def update(self, direction):
                new_coordinates = []
                for coordinate in self.coordinates:
                        new_coordinates.append(tuple(x + y for x, y in zip(coordinate, direction)))
                self.coordinates = new_coordinates
                self.origin = tuple(x + y for x, y in zip(self.origin, direction))

        # Rotate the tetromino 90 degrees clockwise
        def rotate(self):
                # shift points to origin
                coordinates = [(x-self.origin[0],y-self.origin[1]) for x,y in self.coordinates]
                # Perform 90 degree rotation relative to origin
                coordinates = [(y ,-x) for x, y in coordinates]
                # shift points back to original position
                coordinates = [(x+self.origin[0],y+self.origin[1]) for x,y in coordinates]
                self.coordinates = coordinates


class LinePiece(Tetromino):
        def __init__(self):
                # Coordinates are (y,x) coordinate pairs
                self.coordinates = [(0, 4), (0, 5), (0, 6), (0, 7)]
                self.origin = (0, 6)


def main():
        pass

if __name__ == '__main__':
        main()
