import random
import math
import pygame
from pygame import mixer
import time

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Race Car Game")
icon = pygame.image.load('racecar-icon.png')
pygame.display.set_icon(icon)

# define FPS (Frame per second)
FPS = 30

# Create player car
player_x = 0
player_y = 0
player_speed_x = 0
player_speed_y = 0
player_image = pygame.image.load('racecar-red.png')


def init_player_car():
    global player_x, player_y
    player_x = 400 - 72
    player_y = 460


# Draw player car
def draw_player_car():
    screen.blit(player_image, (int(player_x), int(player_y)))


def update_player_car_position():
    global player_x, player_y
    player_x = player_x + player_speed_x
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

def update_enemy_car_position(i):
    global enemy_x, enemy_y, enemy_speed_x, enemy_speed_y
    enemy_x[i] += enemy_speed_x[i]
    enemy_y[i] += enemy_speed_y[i]


gameover_font = pygame.font.Font('freesansbold.ttf', 64)

def show_gameover_text():
    gameover_text = gameover_font.render("GAME OVER", True, (250, 250, 250))
    screen.blit(gameover_text, (200, 50))



current_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 600
textY = 10

def show_score(x, y):
    score = font.render("Score : " + str(current_score), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Define enemy cars
MAX_ENEMY_CARS = 20
level = 1
num_enemy_cars = 10
enemy_x = []
enemy_y = []
enemy_alive = []
enemy_speed_x = []
enemy_speed_y = []
enemy_image = []

for i in range(0, MAX_ENEMY_CARS):
    enemy_x.append(300 + random.randint(-300, 300))
    enemy_y.append(100 + random.randint(-100, 100))
    enemy_alive.append(True)
    enemy_speed_x.append(0)
    enemy_speed_y.append(2)
    n = random.randint(0, 2)
    if n == 0:
        enemy_image.append(pygame.image.load('racecar-green.png'))
    elif n == 1:
        enemy_image.append(pygame.image.load('racecar-blue.png'))
    else:
        enemy_image.append(pygame.image.load('racecar-gray.png'))

def enemies_home_in(enemy_x, player_x, enemy_speed_x):
    if enemy_x > player_x:
        enemy_speed_x == -2
    elif enemy_x < player_x:
        enemy_speed_x == 2
    else:
        enemy_speed_x == 0

def num_enemies_alive():
    num_alive = 0
    for i in range(0, num_enemy_cars):
        if enemy_alive[i]:
            num_alive += 1
    return num_alive

def clear_level(i):
    global num_enemy_cars
    for i in range(0, num_enemy_cars):
        enemy_x[i] = (400 + random.randint(-400, 400))
        enemy_y[i] = (100 + random.randint(-100, 100))
        enemy_alive[i] = True
    num_enemy_cars += 1
    enemy_x.append(400 + random.randint(-400, 400))
    enemy_y.append(100 + random.randint(-100, 100))
    enemy_speed_x.append(0)
    enemy_speed_y.append(2)
    enemy_alive.append(True)
    n = random.randint(0, 2)
    if n == 0:
        enemy_image.append(pygame.image.load('racecar-green.png'))
    elif n == 1:
        enemy_image.append(pygame.image.load('racecar-blue.png'))
    else:
        enemy_image.append(pygame.image.load('racecar-gray.png'))
    screen.blit(enemy_image[i], (int(enemy_x[i]), int(enemy_y[i])))




# Draw enemy car with index i
def draw_enemy_car(i):
    screen.blit(enemy_image[i], (int(enemy_x[i]), int(enemy_y[i])))
    #print('draw enemy car here')

# Update enemy car location here




#Detect collision (True means collide, False means okay)
def detect_crashing(enemy_x, enemy_y, player_x, player_y):
    distance = math.sqrt((enemy_x - player_x) * (enemy_x - player_x) + (enemy_y - player_y) * (enemy_y - player_y))
    if distance < 60:
        return True
    else:
        return False

# Game Loop
clock = pygame.time.Clock()
init_player_car()
running = True
gameover = False
while running:
    dt = clock.tick(FPS)

    # RGB = Red, Green, Blue
    screen.fill((0, 50, 50))

    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed_x = -3
            if event.key == pygame.K_RIGHT:
                player_speed_x = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed_x = 0
        # if event.type == pygame.KEYDOWN:
        # ...
        # if event.type == pygame.KEYUP:
        # ...

    # handle player movement
    update_player_car_position()
    draw_player_car()

    # handle enemy movement
    for i in range(0, num_enemy_cars):
        if enemy_alive[i]:
            draw_enemy_car(i)
            update_enemy_car_position(i)
            # enemies_home_in(enemy_x[i], player_x, enemy_speed_x[i])
            if enemy_y[i] > 600:
                current_score += 10
                enemy_alive[i] = False
            # detect collision
            collision = detect_crashing(enemy_x[i], enemy_y[i], player_x, player_y)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                enemy_alive[i] = False
                gameover = True
                show_gameover_text()

            else:
                if enemy_x[i] < 0:
                    enemy_speed_x[i] = 1
                if enemy_x[i] >= 0:
                    enemy_speed_x[i] = 0
                if enemy_y[i] > 736:
                    enemy_speed_x[i] = -1
                if enemy_x[i] <= 736:
                    enemy_speed_x[i] = 0
                enemy_y[i] = enemy_y[i] + enemy_speed_y[i]
        # update score or how much time elapsed
        show_score(textX, textY)
        # level up and show more enemy cars base on the level
        if num_enemies_alive() == 0:
            clear_level(i)

    # redraw the screen
    pygame.display.update()

    if gameover:
        time.sleep(5)
        pygame.quit
# end of while
pygame.quit()
