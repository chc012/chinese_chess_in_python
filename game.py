"""
Main entry for the Chinese Chess game. For game rule, please see README.
"""
__author__ = "Tony Chang"

import os
from tkinter import *
from abc import ABC, abstractmethod

ASSET_PATH = "assets"
BOARD_IMG = "board.jpg"

SPEED = 10
SCR_SIZE = (SCR_WIDTH, SCR_HEIGHT) = (900 + 300, 1000)
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT) = (int(SCR_WIDTH / 4 * 3), SCR_HEIGHT)
PIECE_SIZE = (PIECE_WIDTH, PIECE_HEIGHT) = \
        (min(int(BOARD_WIDTH / 9 * 0.98), int(BOARD_HEIGHT / 10 * 0.98)), ) * 2
BORDER_WIDTH = 20

WHITE = "#fff"

# TODO
class Board():
    def __init__(self):


    pass


# TODO
class Piece(ABC):
    """Abstract chess pieces, set up initialization and taking."""
    def __init__(self, piece, position):
        self.image, self.rect = load_image(piece, PIECE_SIZE)
        self.position = position

    @abstractmethod
    def move(self):
        """How the specific piece will move according to Chinese Chess rules."""
        pass

    def die(self, opponent):
        """Die from opponent's attack."""

        pass


# TODO
class Pawn():
    pass


# TODO
class King():
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
        """Make window, board, pieces, map."""
        self.window = Tk()
        self.window.title("Chinese Chess")
        self.window.iconbitmap("icon.ico")
        self.window.geometry(str(SCR_WIDTH) + 'x' + str(SCR_HEIGHT))

        self.board = Canvas(window, width=BOARD_WIDTH, height=BOARD_HEIGHT, bg=WHITE,
                            bd=BORDER_WIDTH)
        board.pack()
        bg = PhotoImage(file=BOARD_IMG)
        self.board_img = self.board.create_image(BOARD_WIDTH, BOARD_HEIGHT, image=bg)

        self.pieces = {
            pawns: _make_pieces(Pawn, 10),
            kings: _make_pieces(King, 2),
            guards: _make_pieces(Guard),
            ministers: _make_pieces(Minister),
            cannons: _make_pieces(Cannon),
            knights: _make_pieces(Knight),
            chariots: _make_pieces(Chariot)
        }

        self.map = [[" "]*9]*10
        for piece_list in self.pieces:
            for piece in piece_list:
                self.map[piece.x][piece.y] = piece.icon


    def _make_pieces(self, ctor, piece_num=4):
        """Helper method for pieces dictionary, construct set of pieces."""
        icon_list = [None] * piece_num
        for i in range(0, piece_num/2):
            icon_list[i] = ctor('b', i+1)
            icon_list[i+piece_num/2] = ctor('r', i+1)
        return icon_list


    def play(self):




        top.mainloop()
