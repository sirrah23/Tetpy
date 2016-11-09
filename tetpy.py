import random

class TetrisGame(object):
        """This is the game of tetris being played. Accounts for keeping track
        of the board, the current active piece, and updates to the state of the
        game."""
        active_piece = None
        gameover = False
        clean_board_flag = False # Flag that lets us know whether or not we
                                 # should search the board for complete lines
                                 # to eliminate
        gravity_count = 0 # Current iteration until the next gravity application
        gravity_max = 75  # Apply gravity every X moves

        def __init__(self, WIDTH, HEIGHT):
                """ Initialize the tetris game with a WIDTH x HEIGHT tetris
                board. The board will start clean, filled completely with
                zeroes.
                """
                self.WIDTH = WIDTH
                self.HEIGHT = HEIGHT
                self.board = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
                self.moves = []  # List of moves to process

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
                """This function will create a new active piece for the tetris
                game to use."""
                self.active_piece = random.choice(PIECES)()
                # TODO: Add a shift-up or two to conform to tetris rules. Not critical.
                if self.game_is_over():
                        self.gameover = True

        def draw(self):
                """Clears the board of the active piece, keeping all the
                blocked squares as they are, and then redraws the active piece,
                wherever it may be."""
                # TODO: Optimize this at some point, maybe when we start deleting rows
                for y in range(self.HEIGHT):
                        for x in range(self.WIDTH):
                                if self.board[y][x] != 2:
                                        self.board[y][x] = 0

                for coordinate in self.active_piece.coordinates:
                        self.board[coordinate[0]][coordinate[1]] = 1  # Draw piece onto board

        # Determine if the current piece is within the board or not
        def active_within_sides(self):
                """Determine if the position of the currently active piece
                extend past the sides of the board. This will be called after
                we attempt to move the active piece somewhere new."""
                if not self.active_piece:
                        return False
                within_board = True
                for coordinate in self.active_piece.coordinates:
                        within_board = within_board and coordinate[1] >= 0 and coordinate[1] < self.WIDTH
                        if not within_board:
                                break
                return within_board

        def run_iteration(self):
                """Everytime this function is called we move the tetris board
                from state X to state X+1, accounting for any inputs from an
                exteral source."""
                if self.gameover:
                        return
                if self.clean_board_flag:
                        self.clean_board()
                if self.active_piece is None:
                        self.new_active_piece()
                else:
                        """
                        TODO: Clean up code so it doesn't have to do this old_coordinate stuff.
                        There is probably a more elegant way to do this, but I can't think of one
                        at the moment.
                        """
                        old_coordinates = self.active_piece.coordinates
                        old_origin = self.active_piece.origin
                        self.process_moves() # Move the piece to the left, right, and rotate
                        if not self.active_within_sides() or self.occupied(self.active_piece.coordinates):
                                self.active_piece.coordinates = old_coordinates
                                self.active_piece.origin = old_origin
                        if not self.above_bottom(self.active_piece.coordinates) or self.occupied(self.active_piece.coordinates):
                                self.pacify(old_coordinates)
                                self.new_active_piece()
                        # Default gravity movement, for active pieces, always happens
                        old_coordinates = self.active_piece.coordinates
                        old_origin = self.active_piece.origin
                        self.apply_gravity() # Move the piece down
                        if not self.above_bottom(self.active_piece.coordinates) or self.occupied(self.active_piece.coordinates):
                                self.pacify(old_coordinates)
                                self.new_active_piece()
                self.draw()

        def occupied(self, coordinates):
                """If any coordinate in a list of coordinates is occupied,
                return True, else return False."""
                for coordinate in coordinates:
                        if self.board[coordinate[0]][coordinate[1]] == 2:
                                return True
                return False

        def above_bottom(self, coordinates):
                """ If any of the coordinates from a list extend past the
                height of the board, return False, else return True."""
                for coordinate in coordinates:
                        if coordinate[0] >= self.HEIGHT:
                                return False
                return True

        def pacify(self, coordinates):
                """Fill given list of coordinates with a passive blocker."""
                for coordinate in coordinates:
                        self.board[coordinate[0]][coordinate[1]] = 2
                self.clean_board_flag = True

        def process_moves(self):
                """Process all the moves in the list of moves"""
                # TODO : Might want to set a limit on how many moves we process at any transition.
                MOVES = {"LEFT": (self.active_piece.move_left, None),
                         "RIGHT": (self.active_piece.move_right, None),
                         "ROTATE": (self.active_piece.rotate, None),
                         "SPACE" : (self.active_piece.zoom, self)
                }
                for move in self.moves:
                        move_to_perform, argument = MOVES.get(move, lambda : None)
                        if not argument:
                                move_to_perform()
                        else:
                                move_to_perform(argument)
                self.moves = []  # Get rid of moves we just processed

        def apply_gravity(self):
                """Apply gravity to the board, move the active piece down."""
                self.gravity_count += 1
                if self.gravity_count == self.gravity_max:
                        self.active_piece.update((1,0))
                self.gravity_count = self.gravity_count %  self.gravity_max

        def clean_board(self):
                """Search the board for any complete lines and eliminate them from the board"""
                i = self.HEIGHT - 1  # Start from the bottom...not that it really matters 
                lines_to_delete = []
                while i >= 0:
                        flagged_for_delete = True
                        # Scan each line and see if is filled
                        for square in self.board[i]:
                                # Line not completely filled, stop checking
                                if square != 2:
                                        flagged_for_delete = False
                                        break
                        # Add line to list of lines to delete
                        if flagged_for_delete:
                                lines_to_delete.append(i)
                        i-= 1
                # Delete lines that are filled
                lines_to_delete.sort(reverse=True)  # Reverse list, otherwise deleting will cause indices to shift
                for line in lines_to_delete:
                        del self.board[line]
                for _ in range(len(lines_to_delete)):
                        # Replace deleted lines
                        self.board.insert(0,[0 for x in range(self.WIDTH)])
                self.clean_board_flag = False

        def game_is_over(self):
                """Called when spawning a new piece. If the spawn point is occupied then the game is over."""
                if self.occupied(self.active_piece.coordinates):
                        return True
                return False


class Tetromino(object):
        def update(self, direction):
                # TODO : Consider making it so that self.origin could contain floats. This would
                # require type casting the coordinates to ints upon addition.
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

        def move_left(self):
                self.update((0,1))

        def move_right(self):
                self.update((0,-1))

        def zoom(self, TG):
                """Given the context of a tetris game, zoom the current tetris piece to the bottom of the board.
                If any blocked squares are hit along the way then stop there."""
                while TG.above_bottom(self.coordinates) and not TG.occupied(self.coordinates):
                        old_coordinates = self.coordinates
                        self.update((1,0))
                self.coordinates = old_coordinates



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

PIECES = [LinePiece, TeePiece, SquarePiece, JPiece, LPiece, SPiece, ZPiece]

def main():
        """
        TG = TetrisGame(14,16)
        TG.run_iteration()
        TG.moves += ["ROTATE","ROTATE", "ROTATE", "RIGHT"]
        TG.run_iteration()
        TG.moves += ["ROTATE","LEFT", "LEFT", "LEFT"]
        TG.run_iteration()
        print TG
        """
        pass

if __name__ == '__main__':
        main()
