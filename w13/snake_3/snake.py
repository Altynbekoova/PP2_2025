import pygame
import random
import time
from sql import *
from color_palette import *
from wall import *

pygame.init()

create_tables()

username = input("Enter your username: ")
user_id, score, level = get_create_user(username)

HEIGHT = 720
WIDTH = 720

clock = pygame.time.Clock()
FPS = 5

count_food = 0
count_level = 1

color_index = 1
color_random = COLOR_BLUE

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font('game_bubble.ttf', 30)
font_endgame = pygame.font.Font('game_bubble.ttf', 80)
sound_food = pygame.mixer.Sound('food_eating.wav')

CELL = 30

coords_wall = [(10, 10), (11, 10), (10, 11), (11, 11)]
collided_with_wall = False

wall = Wall(count_level, CELL)
wall.load_level()  # Load the level immediately after creating the wall object

# Drawing the chessboard
def draw_chess_board(): 
    colors = [COLOR_GRAY, COLOR_WHITE]
    squares = (0, 0)
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            squares = (i, j)
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))
            for p in wall.points:
                if p.X // CELL == j and p.Y // CELL == i:
                    pygame.draw.rect(screen, (255, 0, 255), (j * CELL, i * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(3, 10), Point(4, 10), Point(5, 10)]
        self.dx = 1
        self.dy = 0 
        
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw_snake(self):
        head = self.body[0]
        pygame.draw.rect(screen, COLOR_RED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, COLOR_GREEN, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global FPS, count_food, count_level
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos()
            if color_index == 0:
                count_food += 3
            elif color_index == 1:
                count_food += 2
            elif color_index == 2:
                count_food += 1
            sound_food.play()
            if count_food % 5 == 0:
                count_level += 1
                FPS += 2
                wall.level = count_level
                wall.load_level()

    def check_collision_wall(self): 
        global collided_with_wall
        head = self.body[0]

    # Проверка выхода за границы экрана
        if head.x > WIDTH // CELL - 1 or head.x < 0 or head.y < 0 or head.y > HEIGHT // CELL - 1: 
            collided_with_wall = True
            return True

    # Проверка столкновения со стеной
        for point in wall.points:
            if head.x == point.X // CELL and head.y == point.Y // CELL:
                collided_with_wall = True
                return True

        return False

class Food:
    def __init__(self):
        self.pos = Point(12, 10)
        self.food_colors = [COLOR_PURPLE, COLOR_BLUE, COLOR_LIGHTBLUE]
        self.creation_time = time.time()
        self.food_lifetime = 5

    def generate_random_pos(self):
        temp_x = random.randint(0, WIDTH // CELL - 1)
        temp_y = random.randint(0, HEIGHT // CELL - 1)
        
        if all((segment.x != temp_x or segment.y != temp_y) for segment in snake.body):
            self.pos.x = temp_x
            self.pos.y = temp_y
            self.creation_time = time.time()
        else:
            self.generate_random_pos()

    def draw_food(self):
        pygame.draw.rect(screen, color_random, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_color(self):
        global color_index, color_random
        color_index = random.randint(0, 2)
        color_random = self.food_colors[color_index]

    def check_food_lifetime(self):
        if time.time() - self.creation_time > self.food_lifetime:
            return True
        return False

# Ensure that the snake's starting position doesn't overlap with the wall
snake = Snake()
if any(point in wall.points for point in snake.body):
    print("Error: Snake starts in a wall area!")
    running = False
else:
    food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

            # 🚨 Обработка паузы и сохранения
            if event.key == pygame.K_p:
                paused = True
                save_game(user_id, count_food, count_level)
                print("Игра поставлена на паузу. Прогресс сохранён!")

                # ждём, пока игрок не нажмёт другую клавишу
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.QUIT:
                            running = False
                            paused = False
                        elif pause_event.type == pygame.KEYDOWN:
                            paused = False  # выходим из паузы

    screen.fill(COLOR_BLACK)

    draw_chess_board()

    snake.move()
    snake.check_collision(food)

    if food.check_food_lifetime():
        food.generate_random_color()
        food.generate_random_pos()

    if not collided_with_wall:
        food.draw_food()
        snake.draw_snake()

    score_text = font.render(f"Score: {count_food}", True, COLOR_BLUE)
    level_text = font.render(f'Level: {count_level}', True, COLOR_RED)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (600, 10))

    if snake.check_collision_wall():
        save_game(user_id, count_food, count_level)
        print("💾 Прогресс сохранён при проигрыше.")
    
        running = False
        screen.fill(COLOR_GREEN)

        image_endgame_score = font_endgame.render("Total Score: " + str(count_food), True, COLOR_BLACK)
        image_endgame_score_rect = image_endgame_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        image_endgame_level = font_endgame.render("Level: " + str(count_level), True, COLOR_BLACK)
        image_endgame_level_rect = image_endgame_level.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        screen.blit(image_endgame_score, image_endgame_score_rect)
        screen.blit(image_endgame_level, image_endgame_level_rect)

        pygame.display.flip()

        time.sleep(5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()