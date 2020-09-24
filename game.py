"""
Main entry for the Chinese Chess game. For game rule, please see README.
"""
__author__ = "Tony Chang"

import tkinter as tk
from abc import ABC, abstractmethod
from playsound import playsound

ICON_IMG = "icon.ico"
BOARD_IMG = "assets/board.jpg"
PAWN_IMG_B = "assets/pawn_b.jpg"
PAWN_IMG_R = "assets/pawn_r.jpg"
KING_IMG_B = "assets/king_b.jpg"
KING_IMG_R = "assets/king_r.jpg"
HINT_IMG = "assets/hint.jpg"

MOVE_SOUND = "assets/move.wav"
TAKE_SOUND = "assets/take.wav"
WIN_SOUND = "assets/win.wav"

SCR_SIZE = (SCR_WIDTH, SCR_HEIGHT) = (900 + 300, 1000)
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT) = (int(SCR_WIDTH / 4 * 3), SCR_HEIGHT)
PIECE_SIZE = (PIECE_WIDTH, PIECE_HEIGHT) = \
        (min(int(BOARD_WIDTH / 9 * 0.98), int(BOARD_HEIGHT / 10 * 0.98)), ) * 2
BORDER_WIDTH = 20
ROW_LENGTH = 9
COL_LENGTH = 10

TITLE = "Chinese Chess"
BLACK_SIDE = 'b'
RED_SIDE = 'r'
HINT = 'H'

WHITE = "#fff"

# TODO
class Piece(ABC):
    """Abstract chess pieces, set up initialization and taking."""
    def __init__(self, board, map, faction, num):
        """General piece construction. The indicator is made up of a letter and a number, with the
        letter indicating faction and number indicating number within faction."""
        self.board = board
        self.map = map
        self.faction = faction
        self.num = num
        self.pos = (0, 0)
        if faction == RED_SIDE:
            self.pos[1] = 9


    @abstractmethod
    def hint(self):
        """Show the possible movement of specific piece."""
        pass


    @abstractmethod
    def move(self):
        """How the specific piece will move according to Chinese Chess rules."""
        pass





    def die(self):
        """Die from opponent's attack."""

        pass


# TODO
class Pawn(Piece):

    def __init__(self, board, map, faction, num):
        """Pawns are represented by 'P' on the map."""
        super().__init__(board, map, faction, num)
        self.icon = 'P' + self.faction + str(self.num)
        if self.faction == BLACK_SIDE:
            self.pos = ((num - 1) * 2, 3)
        else:
            self.pos = ((num - 1) * 2, 6)
        self.real_x = self.pos[0] + 1



    def hint(self):
        """Pawn can only go forward before reaching "the river"; it can go forward, left, and right
        beyond "the river"."""
        if self.faction == BLACK_SIDE:
            if self.pos[1] >= 5:
                if (self.pos[0] != 0) and (BLACK_SIDE not in self.map[self.pos[0]-1][self.pos[1]]):
                    self.map[self.pos[0] - 1][self.pos[1]] += HINT
                if (self.pos[0] != 8) and (BLACK_SIDE not in self.map[self.pos[0]+1][self.pos[1]]):
                    self.map[self.pos[0] + 1][self.pos[1]] += HINT
            if (self.pos[1] != 9) and (BLACK_SIDE not in self.map[self.pos[0]][self.pos[1] + 1]):
                self.map[self.pos[0]][self.pos[1] + 1] += HINT
        if self.faction == RED_SIDE:
            if self.pos[1] <= 4:
                if (self.pos[0] != 0) and (RED_SIDE not in self.map[self.pos[0]-1][self.pos[1]]):
                    self.map[self.pos[0] - 1][self.pos[1]] += HINT
                if (self.pos[0] != 8) and (RED_SIDE not in self.map[self.pos[0]+1][self.pos[1]]):
                    self.map[self.pos[0] + 1][self.pos[1]] += HINT
            if (self.pos[1] != 0) and (RED_SIDE not in self.map[self.pos[0]][self.pos[1] + 1]):
                self.map[self.pos[0]][self.pos[1] + 1] += HINT


    def move(self):
        pass



# TODO
class King(Piece):
    pass


# TODO
class Guard():
    pass


# TODO
class Minister():
    pass


# TODO
class Cannon():
    pass


# TODO
class Knight():
    pass


# TODO
class Chariot():
    pass


# TODO
class ChineseChess():
    """Main class. Set up game and run it."""
    # TODO: make a menu system
    def __init__(self):
        """Make window, board, map, and pieces; put pieces on map."""
        self.window = tk.Tk()
        self.window.title(TITLE)
        self.window.iconbitmap(ICON_IMG)
        self.window.geometry(str(SCR_WIDTH) + 'x' + str(SCR_HEIGHT))

        self.board = tk.Canvas(window, width=BOARD_WIDTH, height=BOARD_HEIGHT, bg=WHITE,
                            bd=BORDER_WIDTH)
        board.pack()
        bg = tk.PhotoImage(file=BOARD_IMG)
        self.board_img = self.board.create_image(BOARD_WIDTH, BOARD_HEIGHT, image=bg)

        self.map = [[" "] * COL_LENGTH] * ROW_LENGTH

        self.pieces = {
            pawns: _make_pieces(Pawn, 10),
            kings: _make_pieces(King, 2),
            guards: _make_pieces(Guard),
            ministers: _make_pieces(Minister),
            cannons: _make_pieces(Cannon),
            knights: _make_pieces(Knight),
            chariots: _make_pieces(Chariot)
        }

        for piece_list in self.pieces.keys():
            for piece in self.pieces[piece_list]:
                self.map[piece.pos[0]][piece.pos[1]] = piece.icon


    def _make_pieces(self, ctor, piece_num=4):
        """Helper method for pieces dictionary, construct set of pieces."""
        icon_list = [None] * piece_num
        for i in range(0, piece_num/2):
            icon_list[i] = ctor(self.board, self.map, BLACK_SIDE, i+1)
            icon_list[i+piece_num/2] = ctor(self.board, self.map, RED_SIDE, i+1)
        return icon_list


    def play(self):




        self.window.mainloop()
