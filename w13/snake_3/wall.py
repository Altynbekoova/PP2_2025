
import pygame

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

class GameObject:
    def __init__(self, points, color, tile_width):
        self.points = points
        self.color = color
        self.tile_width = tile_width

class Wall(GameObject):
    def __init__(self, level, tile_width):
        super().__init__([], (255, 0, 0), tile_width)
        self.level = level
        self.load_level()

    def load_level(self):
        self.points = []  # ← Очищаем стены перед загрузкой нового уровня
        with open(f"levels/level{self.level}.txt", "r") as f:
            for row, line in enumerate(f):
                for col, c in enumerate(line):
                    if c == '#':
                        self.points.append(Point(col * self.tile_width, row * self.tile_width))

    def next_level(self):
        self.points = []
        self.level = (self.level + 1) % 2
        self.load_level()

    def check_collision(self, head_location):
        # Проверка, не находится ли голова змейки в точке стены
        for point in self.points:
            if point.X == head_location.X and point.Y == head_location.Y:
                return True  # Столкновение произошло
        return False  # Столкновения нет
    
