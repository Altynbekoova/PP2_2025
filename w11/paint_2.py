import pygame
import math

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Цвета
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
current_color = colorRED  # Текущий цвет рисования

# Толщина 
THICKNESS = 5

# рисования
drawing = False
tool = "rectangle"  # Инструмент по умолчанию
prevX, prevY = 0, 0  # Начальные координаты

# Функция прямоугольника
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            prevX, prevY = event.pos

        # Ластик
        if event.type == pygame.MOUSEMOTION and drawing:
            currX, currY = event.pos
            if tool == "eraser":
                pygame.draw.circle(screen, colorWHITE, (currX, currY), THICKNESS)

        # Окончание рисования
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            currX, currY = event.pos

            if tool == "rectangle":
                pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif tool == "circle":
                radius = int(math.sqrt((currX - prevX) ** 2 + (currY - prevY) ** 2))
                pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)
            elif tool == "square":
                side = min(abs(currX - prevX), abs(currY - prevY))
                pygame.draw.rect(screen, current_color, (prevX, prevY, side, side), THICKNESS)
            elif tool == "right_triangle":
                points = [(prevX, prevY), (currX, prevY), (prevX, currY)]
                pygame.draw.polygon(screen, current_color, points, THICKNESS)
            elif tool == "equilateral_triangle":
                height = abs(currY - prevY)
                base = height * (2 / math.sqrt(3))
                points = [(prevX, prevY), (prevX - base / 2, prevY + height), (prevX + base / 2, prevY + height)]
                pygame.draw.polygon(screen, current_color, points, THICKNESS)
            elif tool == "rhombus":
                half_diag_x = abs(currX - prevX) // 2
                half_diag_y = abs(currY - prevY) // 2
                points = [
                    (prevX, prevY - half_diag_y),
                    (prevX - half_diag_x, prevY),
                    (prevX, prevY + half_diag_y),
                    (prevX + half_diag_x, prevY)
                ]
                pygame.draw.polygon(screen, current_color, points, THICKNESS)

        # Горячие клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rectangle"
                print("Selected: Rectangle")
            elif event.key == pygame.K_c:
                tool = "circle"
                print("Selected: Circle")
            elif event.key == pygame.K_e:
                tool = "eraser"
                print("Selected: Eraser")
            elif event.key == pygame.K_s:
                tool = "square"
                print("Selected: Square")
            elif event.key == pygame.K_t:
                tool = "right_triangle"
                print("Selected: Right Triangle")
            elif event.key == pygame.K_y:
                tool = "equilateral_triangle"
                print("Selected: Equilateral Triangle")
            elif event.key == pygame.K_h:
                tool = "rhombus"
                print("Selected: Rhombus")

            # Изменение толщины
            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS and THICKNESS > 1:
                THICKNESS -= 1

            # Смена цвета
            elif event.key == pygame.K_1:
                current_color = colorRED
                print("Color: Red")
            elif event.key == pygame.K_2:
                current_color = colorBLUE
                print("Color: Blue")
            elif event.key == pygame.K_3:
                current_color = colorBLACK
                print("Color: Black")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()