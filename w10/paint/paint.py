import pygame

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")


colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
current_color = colorRED


THICKNESS = 5


drawing = False
tool = "rectangle"  
prevX, prevY = 0, 0


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


clock = pygame.time.Clock()


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            prevX, prevY = event.pos

     
        if event.type == pygame.MOUSEMOTION and drawing:
            currX, currY = event.pos
            if tool == "eraser":
                pygame.draw.circle(screen, colorWHITE, (currX, currY), THICKNESS)

       
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            currX, currY = event.pos
            if tool == "rectangle":
                pygame.draw.rect(screen, current_color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif tool == "circle":
                radius = int(((currX - prevX)**2 + (currY - prevY)**2)**0.5)
                pygame.draw.circle(screen, current_color, (prevX, prevY), radius, THICKNESS)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rectangle"
                print("Selected: Rectangle")
            if event.key == pygame.K_c:
                tool = "circle"
                print("Selected: Circle")
            if event.key == pygame.K_e:
                tool = "eraser"
                print("Selected: Eraser")

            
            if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS and THICKNESS > 1:
                THICKNESS -= 1

            
            if event.key == pygame.K_1:
                current_color = colorRED
                print("Color: Red")
            if event.key == pygame.K_2:
                current_color = colorBLUE
                print("Color: Blue")
            if event.key == pygame.K_3:
                current_color = colorBLACK
                print("Color: Black")

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()