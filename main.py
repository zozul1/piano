import pygame

pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 200

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
white_pressed_color = (128, 128, 128)  # Цвет для нажатых белых клавиш
black_pressed_color = (64, 64, 64)  # Цвет для нажатых черных клавиш

# Звуки для белых клавиш
note_c = pygame.mixer.Sound('zvuk-notyi-si.mp3')
note_d = pygame.mixer.Sound('zvuk-notyi-do.mp3')
note_e = pygame.mixer.Sound('zvuk-notyi-re.mp3')
note_f = pygame.mixer.Sound('zvuk-notyi-fa.mp3')
note_g = pygame.mixer.Sound('zvuk-notyi-lya.mp3')
note_a = pygame.mixer.Sound('zvuk-notyi-sol.mp3')
note_b = pygame.mixer.Sound('zvuk-notyi-mi.mp3')

# Звуки для черных клавиш
note_cs = pygame.mixer.Sound('vibriruyuschiy-zvuk-notyi-re-3-oktava.mp3')
note_ds = pygame.mixer.Sound('zvuk-notyi-do-vo-vtoroy-oktave.mp3')
note_fs = pygame.mixer.Sound('vibriruyuschiy-zvuk-notyi-lya-4-oktava.mp3')
note_gs = pygame.mixer.Sound('elektronnyiy-instrument-zvonkiy-blizkiy.mp3')
note_as = pygame.mixer.Sound('elektronnyiy-instrument-nizkiy-priglushennyiy-udar-dalekiy.mp3')

# Состояние клавиш
white_key_states = {
    pygame.K_a: False,
    pygame.K_s: False,
    pygame.K_d: False,
    pygame.K_f: False,
    pygame.K_g: False,
    pygame.K_h: False,
    pygame.K_j: False
}

black_key_states = {
    pygame.K_w: False,
    pygame.K_e: False,
    pygame.K_t: False,
    pygame.K_y: False,
    pygame.K_u: False
}

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Піаніно')

# Клавиши
def draw_piano_keys():
    key_width = screen_width // 10
    key_height = screen_height

    white_key_colors = [white] * 7
    black_key_colors = [black] * 5

    key_mapping = {
        pygame.K_a: 0,
        pygame.K_s: 1,
        pygame.K_d: 2,
        pygame.K_f: 3,
        pygame.K_g: 4,
        pygame.K_h: 5,
        pygame.K_j: 6
    }

    for key, color in key_mapping.items():
        x = color * key_width
        if white_key_states.get(key, False):
            pygame.draw.rect(screen, white_pressed_color, (x, 0, key_width, key_height))
        else:
            pygame.draw.rect(screen, white_key_colors[color], (x, 0, key_width, key_height))

    for i, color in enumerate(black_key_colors):
        x = i * key_width * 2 + key_width
        key = pygame.K_w + i * 2
        if black_key_states.get(key, False):
            pygame.draw.rect(screen, black_pressed_color, (x, 0, key_width, key_height // 2))
        else:
            pygame.draw.rect(screen, color, (x, 0, key_width, key_height // 2))

# Буквы на клавишах
def draw_piano_keys():
    key_width = screen_width // 10
    key_height = screen_height

    white_key_colors = [white] * 7
    black_key_colors = [black] * 5

    key_mapping = {
        pygame.K_a: 0,
        pygame.K_s: 1,
        pygame.K_d: 2,
        pygame.K_f: 3,
        pygame.K_g: 4,
        pygame.K_h: 5,
        pygame.K_j: 6
    }

    text_vertical_offset = 20

    for key, index in key_mapping.items():
        x = index * key_width
        if white_key_states.get(key, False):
            pygame.draw.rect(screen, white_pressed_color, (x, 0, key_width, key_height))
        else:
            pygame.draw.rect(screen, white_key_colors[index], (x, 0, key_width, key_height))
        font = pygame.font.Font(None, 36)
        label = chr(key)
        text = font.render(label, True, black)
        text_rect = text.get_rect(center=(x + key_width // 2, key_height // 2 + text_vertical_offset))
        screen.blit(text, text_rect)

    for i, label in enumerate(["W", "E", "T", "Y", "U"]):
        x = i * key_width * 2 + key_width
        key = pygame.K_w + i * 2
        if black_key_states.get(key, False):
            pygame.draw.rect(screen, black_pressed_color, (x, 0, key_width, key_height // 2))
        else:
            pygame.draw.rect(screen, black_key_colors[i], (x, 0, key_width, key_height // 2))
        font = pygame.font.Font(None, 36)
        text = font.render(label, True, white)
        text_rect = text.get_rect(center=(x + key_width // 2, key_height // 4 + text_vertical_offset))
        screen.blit(text, text_rect)

# Цикл программы
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in white_key_states:
                note = None
                if event.key == pygame.K_a:
                    note = note_c
                elif event.key == pygame.K_s:
                    note = note_d
                elif event.key == pygame.K_d:
                    note = note_e
                elif event.key == pygame.K_f:
                    note = note_f
                elif event.key == pygame.K_g:
                    note = note_g
                elif event.key == pygame.K_h:
                    note = note_a
                elif event.key == pygame.K_j:
                    note = note_b

                if note:
                    note.play()
                white_key_states[event.key] = True
            elif event.key in black_key_states:
                note = None
                if event.key == pygame.K_w:
                    note = note_cs
                elif event.key == pygame.K_e:
                    note = note_ds
                elif event.key == pygame.K_t:
                    note = note_fs
                elif event.key == pygame.K_y:
                    note = note_gs
                elif event.key == pygame.K_u:
                    note = note_as

                if note:
                    note.play()
                black_key_states[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in white_key_states:
                white_key_states[event.key] = False
            elif event.key in black_key_states:
                black_key_states[event.key] = False

    screen.fill(white)
    draw_piano_keys()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
