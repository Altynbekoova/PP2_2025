import pygame
import random

# Константы
WIDTH, HEIGHT = 600, 600  # Размер экрана
CELL = 30  # Размер клетки
FPS = 5  # Скорость игры

# Цвета еды: 1 - зеленая, 2 - синяя, 3 - красная
FOOD_COLORS = {1: (0, 255, 0), 2: (0, 0, 255), 3: (255, 0, 0)}

# Цвета игрового поля
WHITE, GRAY, RED, YELLOW, BLACK = (255, 255, 255), (200, 200, 200), (255, 0, 0), (255, 255, 0), (0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def draw_grid():
    """Рисуем шахматную доску"""
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            color = WHITE if (i + j) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (i * CELL, j * CELL, CELL, CELL))


class Point:
    """Координаты точки"""
    def __init__(self, x, y):
        self.x, self.y = x, y


class Snake:
    """Класс змейки"""
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0  # Направление движения
        self.growth = False

    def move(self):
        """Передвижение змейки"""
        if not self.growth:
            self.body.pop()
        self.growth = False
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        self.body.insert(0, new_head)

    def draw(self):
        """Рисуем змейку"""
        pygame.draw.rect(screen, RED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        """Проверяем, съела ли змейка еду"""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.growth = True
            food.randomize_position(self.body)

    def check_wall_collision(self):
        """Проверяем столкновение со стеной"""
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def check_self_collision(self):
        """Проверяем, врезалась ли змейка в себя"""
        head = self.body[0]
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])


class Food:
    """Класс еды"""
    def __init__(self):
        self.pos = Point(9, 9)
        self.weight = random.choice([1, 2, 3])  # Случайный вес еды
        self.timer = random.randint(30, 60)  # Время жизни еды (в кадрах)

    def draw(self):
        """Рисуем еду"""
        pygame.draw.rect(screen, FOOD_COLORS[self.weight], (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def update(self, snake_body):
        """Обновляем таймер еды"""
        self.timer -= 1
        if self.timer <= 0:
            self.randomize_position(snake_body)

    def randomize_position(self, snake_body):
        """Создаем новую еду в случайном месте"""
        while True:
            self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(part.x == self.pos.x and part.y == self.pos.y for part in snake_body):
                self.weight = random.choice([1, 2, 3])  # Новый вес
                self.timer = random.randint(30, 60)  # Новый таймер
                break


# Создание объектов
food = Food()
snake = Snake()

running = True
while running:
    screen.fill(BLACK)  # Очистка экрана
    draw_grid()  # Отрисовка сетки

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    # Движение змейки
    snake.move()

    # Проверка столкновений
    snake.check_collision(food)
    if snake.check_wall_collision() or snake.check_self_collision():
        print("Game Over!")
        running = False

    # Отрисовка
    snake.draw()
    food.draw()

    # Обновление таймера еды
    food.update(snake.body)

    # Вывод счета
    score = len(snake.body) - 3
    font = pygame.font.SysFont("Verdana", 20)
    screen.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()