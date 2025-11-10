import pygame
from .game_utils import reflect_velocity

BALL_SIZE = 16

class Ball:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(width//2 - BALL_SIZE//2, height//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
        self.reset()

    def reset(self):
        self.rect.center = (self.width//2, self.height//2)
        # initial velocity
        self.vx = 5
        self.vy = 3

    def update(self, left_paddle_rect, right_paddle_rect):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # bounce top/bottom
        if self.rect.top <= 0 or self.rect.bottom >= self.height:
            self.vy = -self.vy

        # paddle collision
        if self.rect.colliderect(left_paddle_rect) and self.vx < 0:
            offset = (self.rect.centery - left_paddle_rect.centery) / (left_paddle_rect.height/2)
            self.vx, self.vy = reflect_velocity(self.vx, self.vy, offset*2)

        if self.rect.colliderect(right_paddle_rect) and self.vx > 0:
            offset = (self.rect.centery - right_paddle_rect.centery) / (right_paddle_rect.height/2)
            self.vx, self.vy = reflect_velocity(self.vx, self.vy, offset*2)

        # return scorer: 'left', 'right', or None
        if self.rect.left <= 0:
            return 'right'
        if self.rect.right >= self.width:
            return 'left'
        return None

    def draw(self, surf, color=(255,255,255)):
        pygame.draw.ellipse(surf, color, self.rect)
