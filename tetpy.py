class TetrisGame(object):
        active_piece = None
        direction = (-1, 0)
        gameover = False

        # Initialize the tetris game with a WIDTH x HEIGHT tetris board
        def __init__(self, WIDTH, HEIGHT):
                self.WIDTH = WIDTH
                self.HEIGHT = HEIGHT
                self.board = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

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

        def new_active_piece(self):
                # TODO: Throw error if new piece cannot be created (game over)
                self.active_piece = ZPiece()

        def draw(self):
                # TODO: Optimize this at some point, maybe when we start deleting rows
                for y in range(self.HEIGHT):
                        for x in range(self.WIDTH):
                                if self.board[y][x] != 2:
                                        self.board[y][x] = 0

                for coordinate in self.active_piece.coordinates:
                        self.board[coordinate[0]][coordinate[1]] = 1  # Draw piece onto board

        # Determine if the current piece is within the board or not
        def active_within_sides(self):
                if not self.active_piece:
                        return False
                within_board = True
                for coordinate in self.active_piece.coordinates:
                        within_board = within_board and coordinate[1] >= 0 and coordinate[1] < self.WIDTH
                        if not within_board:
                                break
                return within_board

        def run_iteration(self):
                if self.active_piece is None:
                        self.new_active_piece()
                else:
                        #TODO: Add user rotation here if requested...
                        #TODO: Get user input for left-right movement
                        if self.direction[1] != 0:
                                old_coordinates = self.active_piece.coordinates
                                old_origin = self.active_piece.origin
                                self.active_piece.update((0, direction[1]))
                                if not self.active_within_sides():
                                        self.active_piece.coordinates = old_coordinates
                                        self.active_piece.origin = old_origin
                        # Default gravity movement, for active pieces, always happens
                        old_coordinates = self.active_piece.coordinates
                        old_origin = self.active_piece.origin
                        self.active_piece.update((1, 0))
                        #TODO: Implement these new methods
                        if not self.above_bottom(self.active_piece.coordinates) or self.occupied(self.active_piece.coordinates):
                                self.pacify(old_coordinates)
                                self.new_active_piece()
                self.draw()

        def occupied(self, coordinates):
                # If any coordinate in a list of coordinates is occupied, return True, else return False
                for coordinate in coordinates:
                        if self.board[coordinate[0]][coordinate[1]] == 2:
                                return True
                return False

        def above_bottom(self, coordinates):
                # If any of the coordinates from a list extend past the height of the board, return False, else return True
                for coordinate in coordinates:
                        if coordinate[0] >= self.HEIGHT:
                                return False
                return True

        def pacify(self, coordinates):
                # Fill given list of coordinates with a passive blocker
                for coordinate in coordinates:
                        self.board[coordinate[0]][coordinate[1]] = 2


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

class TeePiece(Tetromino):
        def __init__(self):
                # Coordinates are (y,x) coordinate pairs
                self.coordinates = [(1, 4), (1, 5), (1, 6), (0, 5)]
                self.origin = (1, 5)

class SquarePiece(Tetromino):
        def __init__(self):
                # Coordinates are (y,x) coordinate pairs
                self.coordinates = [(0, 4), (0, 5), (1, 4), (1, 5)]
                self.origin = (1, 4)

        # Square pieces don't rotate...
        def rotate(self):
                pass

class JPiece(Tetromino):
        def __init__(self):
                # Coordinates are (y,x) coordinate pairs
                self.coordinates = [(1, 4), (1, 5), (1, 6), (2, 6)]
                self.origin = (1, 5)

class LPiece(Tetromino):
        def __init__(self):
                # Coordinates are (y,x) coordinate pairs
                self.coordinates = [(1, 4), (1, 5), (1, 6), (2, 4)]
                self.origin = (1, 5)

class SPiece(Tetromino):
        def __init__(self):
                # Coordinates are (y,x) coordinate pairs
                self.coordinates = [(2, 4), (2, 5), (1, 5), (1, 6)]
                self.origin = (1, 5)

class ZPiece(Tetromino):
        def __init__(self):
                # Coordinates are (y,x) coordinate pairs
                self.coordinates = [(1, 4), (1, 5), (2, 5), (2, 6)]
                self.origin = (1, 5)

def main():
#        TG = TetrisGame(14,16)
#        TG.run_iteration()
#        print TG
#        TG.run_iteration()
#        TG.active_piece.rotate()
#        TG.active_piece.rotate()
#        TG.active_piece.rotate()
#        TG.active_piece.rotate()
#        TG.draw()
#        print TG
        pass

if __name__ == '__main__':
        main()
