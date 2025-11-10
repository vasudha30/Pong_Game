import pygame
from .game_utils import clamp

PADDLE_W, PADDLE_H = 10, 90

class Paddle:
    """Paddle class handles position and drawing. Kept minimal for clarity."""
    def __init__(self, x, y, speed=6):
        self.rect = pygame.Rect(x, y, PADDLE_W, PADDLE_H)
        self.speed = speed

    def move(self, dy):
        self.rect.y += dy
        self.rect.y = clamp(self.rect.y, 0, 500 - PADDLE_H)

    def draw(self, surf, color=(255,255,255)):
        pygame.draw.rect(surf, color, self.rect)
