import pygame
import sys

'''Путешествие cвета от Земли до Луны'''

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
EARTH_RADIUS = 6371000            # радиус Земли в метрах
MOON_RADIUS = 1737400             # радиус Луны в метрах
DISTANCE_EARTH_MOON = 384400000   # расстояние от Земли до Луны в метрах
SPEED_OF_LIGHT = 299792458        # скорость света в м/с

# Масштабирование
SCALE = 1e-6

# Параметры для отображения
earth_radius_px = EARTH_RADIUS * SCALE
moon_radius_px = MOON_RADIUS * SCALE
distance_px = DISTANCE_EARTH_MOON * SCALE

# Параметры окна
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption('Путешествие света от Земли до Луны')

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Инициализация шрифта
font = pygame.font.SysFont(None, 24)

# Расчет времени полета
travel_time = DISTANCE_EARTH_MOON / SPEED_OF_LIGHT

# Начальные параметры луча
beam_pos = 0
direction = 1

# Главный цикл игры
clock = pygame.time.Clock()
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обновление позиции луча
        beam_pos += direction * SPEED_OF_LIGHT * clock.get_time() / 1000.0

        # Смена направления при достижении Луны или Земли
        if beam_pos >= DISTANCE_EARTH_MOON:
            beam_pos = DISTANCE_EARTH_MOON
            direction = -1
        elif beam_pos <= 0:
            beam_pos = 0
            direction = 1

        # Очистка экрана
        screen.fill(BLACK)

        # Отображение Земли
        pygame.draw.circle(screen, BLUE, (WIDTH // 4, HEIGHT // 2), int(earth_radius_px))

        # Отображение Луны
        pygame.draw.circle(screen, GRAY, (3 * WIDTH // 4, HEIGHT // 2), int(moon_radius_px))

        # Отображение луча света
        beam_x = WIDTH // 4 + (3 * WIDTH // 4 - WIDTH // 4) * (beam_pos / DISTANCE_EARTH_MOON)
        pygame.draw.circle(screen, WHITE, (int(beam_x), HEIGHT // 2), 1)

        # Отображение текста со скоростью
        speed_text = f'Скорость: {SPEED_OF_LIGHT / 1000000:.3f} км/с'
        text_surface = font.render(speed_text, True, WHITE)
        screen.blit(text_surface, (int(beam_x) - text_surface.get_width() // 2, HEIGHT // 2 - 100))

        # Отображение фиксированного текста с расстоянием
        distance_text = f'Расстояние: {DISTANCE_EARTH_MOON / 1000000:.3f} км'
        distance_surface = font.render(distance_text, True, WHITE)
        screen.blit(distance_surface, (WIDTH // 2 - distance_surface.get_width() // 2, HEIGHT - 230))

        # Отображение фиксированной надписи сверху
        title_text = "Космос"
        title_surface = font.render(title_text, True, WHITE)
        screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 70))

        # Обновление дисплея
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(120)
        
except KeyboardInterrupt:
    pygame.quit()
    sys.exit()
