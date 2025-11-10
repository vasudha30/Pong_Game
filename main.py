# Entry point to run the Pong game.
import pygame
import sys
from .paddle import Paddle
from .ball import Ball

WIDTH, HEIGHT = 800, 500
FPS = 60

def draw_center_line(surf):
    for y in range(0, HEIGHT, 20):
        pygame.draw.rect(surf, (255,255,255), (WIDTH//2 - 1, y, 2, 10))

def main():
    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong - modular")
    clock = pygame.time.Clock()
    left = Paddle(20, HEIGHT//2 - 90//2)
    right = Paddle(WIDTH - 20 - 10, HEIGHT//2 - 90//2)
    ball = Ball(WIDTH, HEIGHT)
    score_left = 0
    score_right = 0
    font = pygame.font.SysFont('Arial', 30)

    running = True
    while running:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            left.move(-left.speed)
        if keys[pygame.K_s]:
            left.move(left.speed)
        if keys[pygame.K_UP]:
            right.move(-right.speed)
        if keys[pygame.K_DOWN]:
            right.move(right.speed)

        scorer = ball.update(left.rect, right.rect)
        if scorer == 'left':
            score_left += 1
            ball.reset()
        elif scorer == 'right':
            score_right += 1
            ball.reset()

        WIN.fill((0,0,0))
        draw_center_line(WIN)
        left.draw(WIN)
        right.draw(WIN)
        ball.draw(WIN)
        score_surf = font.render(f"{score_left}   {score_right}", True, (255,255,255))
        WIN.blit(score_surf, (WIDTH//2 - score_surf.get_width()//2, 10))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
