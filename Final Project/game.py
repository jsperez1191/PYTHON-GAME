import pygame
import random
import sys
'''
This is a simple shooting game.
User is the triangle at the bottom shooting and exploding the blocks coming down on him
You can virtually play forever!
You get one point when you explode a block and lose a point when the block reaches the bottom
You can close the game by the exit window button on the screen
'''
pygame.init()

# creating the size of game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bulls-I")

clock = pygame.time.Clock()

# create colors for users and enemies and bullets
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# creating the player
player_size = 50
player_x = 375
player_y = 540
player_speed = 6

# creating a list for bullets and the speed
bullets = []
bullet_speed = 8

# creating enemies and setting speed downwards
enemies = []
enemy_size = 40
enemy_speed = 2

explosions = []
game_over = False

# scoring system and the font
score = 0
font = pygame.font.SysFont(None, 36)

# loop will run forever until game is closed
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # shooting bullets
        if event.type == pygame.KEYDOWN:
            # space bar will shoot bullets
            if event.key == pygame.K_SPACE:
                #this will have bullets shoot through the middle of the block
                bullets.append([player_x + player_size // 2, player_y])

    # keys to move players
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # this will keep player inside the game window
    player_x = max(0, min(800 - player_size, player_x))

    # drawing player as a triangle
    top = (player_x + player_size // 2, player_y)

    left = (player_x, player_y + player_size)

    right = (player_x + player_size, player_y + player_size)

    pygame.draw.polygon(screen, (0, 150, 255), [top, left, right])

    # creating the shooting aspect with red bullets
    new_bullets = []

    for bullet in bullets:
        bullet[1] -= bullet_speed

        # this will check if you hit the enemy
        hit = False
        for enemy in enemies:
            if (enemy[0] < bullet[0] < enemy[0] + enemy_size and
                enemy[1] < bullet[1] < enemy[1] + enemy_size):
                # if hit the enemy is removed from screen and added to the score
                # create an explosion when enemies are hit
                explosions.append([enemy[0] + enemy_size // 2,
                                   enemy[1] + enemy_size // 2,
                                   5])

                # removes enemy and increases the score
                enemies.remove(enemy)
                score += 1

                hit_enemy = True
                break
        new_explosions = []

        for exp in explosions:
            x, y, radius = exp

            # circle explosion when enemies get hit
            pygame.draw.circle(screen, (255, 150, 0), (x, y), radius)

            # expands when hit
            radius += 3

            if radius < 40:
                new_explosions.append([x, y, radius])

        explosions = new_explosions
        if not hit and bullet[1] > 0:
            new_bullets.append(bullet)

        pygame.draw.rect(screen, RED, (bullet[0], bullet[1], 5, 10))

    bullets = new_bullets

    # randomly spawn enemies on screen moving downward
    if random.randint(1, 60) == 1:
        x = random.randint(0, 800 - enemy_size)
        enemies.append([x, 0])

    new_enemies = []

    for enemy in enemies:
        enemy[1] += enemy_speed

        # if the enemy blocks reach the bottom score minus 1
        if enemy[1] >= 600:
            score -= 1
            continue
        new_enemies.append(enemy)
        if score < 0:
            score = 0
        # green block enemies
        pygame.draw.rect(screen, GREEN, (enemy[0], enemy[1], enemy_size, enemy_size))

    enemies = new_enemies

    # scoring will be on top left of the game window
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()