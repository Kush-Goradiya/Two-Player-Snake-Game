import pygame
import random


pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

screen_width = 900
screen_height = 600

# creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
# Game Title
pygame.display.set_caption("SNAKE vs SNAKE")
pygame.display.update()

# game specific variables
exit_game = False
game_over = False
snake1_x = 45
snake1_y = 55
snake2_x = 685
snake2_y = 55
velocity1_x = 0
velocity1_y = 0
velocity2_x = 0
velocity2_y = 0
food_x = random.randint(20, screen_width/2)
food_y = random.randint(20, screen_height/2)
score1 = 0
score2 = 0
init_velocity1 = 5
init_velocity2 = 5
snake1_size = 20
snake2_size = 20
food_size = 10
fps = 60
food_radius = 8

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen1(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])
def text_screen2(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake1(gameWindow, color, snk1_list, snake1_size):
    for x,y in snk1_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake1_size, snake1_size])
def plot_snake2(gameWindow, color, snk2_list, snake2_size):
    for a,b in snk2_list:
        pygame.draw.rect(gameWindow, color, [a, b, snake2_size, snake2_size])

snk1_list = []
snk1_length = 1
snk2_list = []
snk2_length = 1

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
    # player 1 controls
            if event.key == pygame.K_RIGHT:
                velocity1_x = init_velocity1
                velocity1_y = 0
            if event.key == pygame.K_LEFT:
                velocity1_x = -init_velocity1
                velocity1_y = 0
            if event.key == pygame.K_UP:
                velocity1_y = -init_velocity1
                velocity1_x = 0
            if event.key == pygame.K_DOWN:
                velocity1_y = init_velocity1
                velocity1_x = 0
    # player 2 controls
            if event.key == pygame.K_d:
                velocity2_x = init_velocity2
                velocity2_y = 0
            if event.key == pygame.K_a:
                velocity2_x = -init_velocity2
                velocity2_y = 0
            if event.key == pygame.K_w:
                velocity2_Y = -init_velocity2
                velocity2_X = 0
            if event.key == pygame.K_s:
                velocity2_Y = init_velocity2
                velocity2_X = 0

    snake1_x = snake1_x + velocity1_x
    snake1_y = snake1_y + velocity1_y
    snake2_x = snake2_x + velocity2_x
    snake2_y = snake2_y + velocity2_y

    if abs(snake1_x - food_x) < 12 and abs(snake1_y - food_y) < 12:
        score1 += 1
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)
        snk1_length += 5
    if abs(snake2_x - food_x) < 12 and abs(snake2_y - food_y) < 12:
        score2 += 1
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)
        snk2_length += 5
    gameWindow.fill(black)
    # print score on game window
    text_screen1("Player 1: " + str(score1 * 10), blue, 5, 5)
    text_screen2("Player 2: " + str(score2 * 10), blue, 650, 5)
    pygame.draw.circle(gameWindow, white, [food_x, food_y], food_radius)

    head1 = []
    head1.append(snake1_x)
    head1.append(snake1_y)
    snk1_list.append(head1)
    head2 = []
    head2.append(snake2_x)
    head2.append(snake2_y)
    snk2_list.append(head2)

    if len(snk1_list) > snk1_length:
        del snk1_list[0]
    if len(snk2_list) > snk2_length:
        del snk2_list[0]
    #pygame.draw.rect(gameWindow, green, [snake_x, snake_y, snake_size, snake_size])
    plot_snake1(gameWindow, green, snk1_list, snake1_size)
    pygame.display.update()
    clock.tick(fps)
    plot_snake2(gameWindow, blue, snk2_list, snake2_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
