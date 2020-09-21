"""
Main entry for the Chinese Chess game. For game rule, please see README.
"""
__author__ = "Tony Chang"

import pygame
import os
from abc import ABC, abstractmethod

ASSET_PATH = "assets"
BOARD = "board.jpg"

SPEED = 10
SCR_SIZE = (SCR_WIDTH, SCR_HEIGHT) = (1100, 1000)
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT) = ((SCR_WIDTH/11)*9, SCR_HEIGHT)
PIECE_SIZE = (PIECE_WIDTH, PIECE_HEIGHT) = (BOARD_WIDTH/9, BOARD_HEIGHT/10)

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.display.set_caption("Chinese Chess")

SCREEN = pygame.display.set_mode(SCR_SIZE)

# Sound effect
# TODO: find sounds
MOVE_SOUND = pygame.mixer.Sound(os.path.join(ASSET_PATH, "move.wav"))
TAKE_SOUND = pygame.mixer.Sound(os.path.join(ASSET_PATH, "take.wav"))
WIN_SOUND = pygame.mixer.Sound(os.path.join(ASSET_PATH, "win.wav"))

def load_image(path, size=(-1, -1)):
    """Set up picture and size conversion"""
    image = pygame.image.load(os.path.join(ASSET_PATH, path))
    image = image.convert()
    if size != (-1, -1):
        image = pygame.transform.scale(image, size)
    return (image, image.get_rect())


class Board():
    def __init__(self):
        self.image, self.rect = load_image(BOARD, BOARD_SIZE)

    pass

class Piece(ABC):
    """Abstract chess pieces, set up initialization and taking."""
    def __init__(self, piece, position):
        self.image, self.rect = load_image(piece, PIECE_SIZE)
        self.position = position

    @abstractmethod
    def move(self):
        pass


    pass

class Pawn():
    pass

class King():
    pass

class Guard():
    pass


class Minister():
    pass


class Cannon():
    pass


class Knight():
    pass


class Chariot():
    pass
