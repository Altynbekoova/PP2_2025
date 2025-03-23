import pygame
import random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30
screen = pygame.display.set_mode((HEIGHT, WIDTH))


# draw chess board
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"


class Snake:
    def __init__(self):
        # starting point snake
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # x
        self.dy = 0  # y
        self.growth = False

    def move(self):
        # move snake body
        if not self.growth:
            self.body.pop()  #delete last point, if don't eat food
        else:
            self.growth = False

        # add new point to snake body
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        self.body.insert(0, new_head)

    def draw(self):
        # snake head red
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        # snake body yellow
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        # check snake eat a food
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.growth = True  # snake grow
            food.randomize_position(self.body)  # new food

    def check_wall_collision(self):
        # check snake hit wall
        head = self.body[0]
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            return True
        return False

    def check_self_collision(self):
        # check snake hit itself
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])


class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        # draw food green
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def randomize_position(self, snake_body):
        # food don't be on snake body
        while True:
            self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(part.x == self.pos.x and part.y == self.pos.y for part in snake_body):
                break


FPS = 5
clock = pygame.time.Clock()


food = Food()
snake = Snake()


score = 0

# main code
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1

    # draw chess board
    draw_grid_chess()

    # snake movement
    snake.move()

    # check collision with food
    snake.check_collision(food)

    # hit snake itself
    if snake.check_wall_collision() or snake.check_self_collision():
        print("Game Over!")
        running = False

    # draw snake and food 
    snake.draw()
    food.draw()

    # score 
    score = len(snake.body) - 3
    font = pygame.font.SysFont("Verdana", 20)
    score_text = font.render(f"Score: {score}", True, colorBLACK)
    screen.blit(score_text, (10, 10))

    
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()