import pygame
import random


pygame.init()

# Размеры окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Runner Game")

#изображение
image_background = pygame.image.load('resources/AnimatedStreet.png')
image_player = pygame.image.load('resources/Player.png')
image_enemy = pygame.image.load('resources/Enemy.png')
image_coin = pygame.image.load('resources/Coin.png')

#размер монеты
image_coin = pygame.transform.scale(image_coin, (50, 50))

# Загрузка звуков
pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)  # Фоновая музыка зациклена
sound_crash = pygame.mixer.Sound('resources/crash.wav')
sound_coin = pygame.mixer.Sound('resources/coin.mp3')  # MP3 пусть остается

# Шрифты и текст
font_large = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
image_game_over = font_large.render("Game Over", True, "black")

# Частота кадров
FPS = 60
clock = pygame.time.Clock()

# цвет
WHITE = (255, 255, 255)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        # чтобы не вышел с экрана 
        self.rect.clamp_ip(screen.get_rect())

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = random.randint(5, 10)
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.reset_position()

# Класс монеты 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.weight = random.choice([1, 2, 5])  # 1, 2 или 5 очков за монету
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -50)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.reset_position()

# "Game Over"
def show_game_over():
    screen.fill("red")
    screen.blit(image_game_over, (WIDTH // 2 - image_game_over.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.mixer.music.stop()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# текст
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Главная функция
def main():
    player = Player()
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()

    # первый враг
    enemies.add(Enemy())

    # Создаем 2 монеты
    for _ in range(2):
        coins.add(Coin())

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player, *enemies, *coins)

    coin_count = 0  # Количество монет
    speed_increase_timer = 0  # Таймер для увеличения скорости

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move()

        # Обновляем машинки
        for entity in all_sprites:
            entity.move()

        # врезался ли игрок
        if pygame.sprite.spritecollideany(player, enemies):
            sound_crash.play()
            show_game_over()
            return

        # собрили ли мы ионеты 
        coins_collected = pygame.sprite.spritecollide(player, coins, True)
        for coin in coins_collected:
            sound_coin.play()
            coin_count += coin.weight  # Добавляем вес монеты к счету
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

        # скорость меняется каждые 10 монет
        if coin_count % 10 == 0 and coin_count > 0:
            for enemy in enemies:
                enemy.speed += 0.3

        # показываем фото
        screen.blit(image_background, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        # показывем счет 
        draw_text(f"Score: {coin_count * 10}", font_small, WHITE, 10, 10)
        draw_text(f"Coins: {coin_count}", font_small, WHITE, WIDTH - 100, 10)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()