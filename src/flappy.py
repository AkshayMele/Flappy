import pygame
from sys import exit
import random

pygame.init()
game_clock = pygame.time.Clock()

# Game Window
window_height = 720
window_width = 551
game_window = pygame.display.set_mode((window_width, window_height))

# Game Images
flappy_images = [pygame.image.load("assets/Flappy.png"),]
background_image = pygame.image.load("assets/background.png")
floor_image = pygame.image.load("assets/ground.png")
pipe_top_image = pygame.image.load("assets/pipe_top.png")
pipe_bottom_image = pygame.image.load("assets/pipe_bottom.png")
game_over_img = pygame.image.load("assets/game_over.png")
start_img = pygame.image.load("assets/start.png")

# Game Variables
scrolling_speed = 1
flappy_start_position = (100, 250)
game_score = 0
game_font = pygame.font.SysFont('Pokemon GB', 16)
game_paused = True


class Flappy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = flappy_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = flappy_start_position
        self.image_index = 0
        self.velocity = 0
        self.flap = False
        self.is_alive = True

    def update(self, player_input):
        self.image = flappy_images[0]

        # Gravity and Flap
        self.velocity += 0.5
        if self.velocity > 7:
            self.velocity = 7
        if self.rect.y < 500:
            self.rect.y += int(self.velocity)
        if self.velocity == 0:
            self.flap = False

        # Rotate Flappy
        self.image = pygame.transform.rotate(self.image, self.velocity * -7)

        # Player Input
        if player_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.is_alive:
            self.flap = True
            self.velocity = -7


class GamePipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type

    def update(self):
        # Move Pipe
        self.rect.x -= scrolling_speed
        if self.rect.x <= -window_width:
            self.kill()

        # Score
        global game_score
        if self.pipe_type == 'bottom':
            if flappy_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if flappy_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                game_score += 1


class GameGround(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = floor_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground
        self.rect.x -= scrolling_speed
        if self.rect.x <= -window_width:
            self.kill()


def exit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Game Main Method
def game_main():
    global game_score

    # Instantiate Flappy
    flappy = pygame.sprite.GroupSingle()
    flappy.add(Flappy())

    # Setup Pipes
    pipe_timer = 0
    game_pipes = pygame.sprite.Group()

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    game_ground = pygame.sprite.Group()
    game_ground.add(GameGround(x_pos_ground, y_pos_ground))

    game_run = True
    while game_run:
        # Quit
        exit_game()

        # Reset Frame
        game_window.fill((0, 0, 0))

        # Player Input
        player_input = pygame.key.get_pressed()

        # Draw Background
        game_window.blit(background_image, (0, 0))
        
        # Spawn Ground
        if len(game_ground) <= 2:
            game_ground.add(GameGround(window_width, y_pos_ground))

        # Draw - Pipes, Ground and Flappy
        game_pipes.draw(game_window)
        game_ground.draw(game_window)
        flappy.draw(game_window)

        # Show Score
        score_text = game_font.render('SCORE: ' + str(game_score), True, pygame.Color(255, 255, 255))
        game_window.blit(score_text, (220, 20))

        # Update - Pipes, Ground and Flappy
        if flappy.sprite.is_alive:
            game_pipes.update()
            game_ground.update()
        flappy.update(player_input)

        # Collision Detection
        collision_pipes = pygame.sprite.spritecollide(flappy.sprites()[0], game_pipes, False)
        collision_ground = pygame.sprite.spritecollide(flappy.sprites()[0], game_ground, False)
        if collision_pipes or collision_ground:
            flappy.sprite.is_alive = False
            if collision_ground:
                game_window.blit(game_over_img, (window_width // 2 - game_over_img.get_width() // 2,
                                              window_height // 2 - game_over_img.get_height() // 2))
                if player_input[pygame.K_r]:
                    game_score = 0
                    break

        # Spawn Pipes
        if pipe_timer <= 0 and flappy.sprite.is_alive:
            x_top, x_bottom = 550, 550
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + pipe_bottom_image.get_height()
            game_pipes.add(GamePipe(x_top, y_top, pipe_top_image, 'top'))
            game_pipes.add(GamePipe(x_bottom, y_bottom, pipe_bottom_image, 'bottom'))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1

        game_clock.tick(60)
        pygame.display.update()


# Game Menu
def game_menu():
    global game_paused

    while game_paused:
        exit_game()

        # Draw Menu
        game_window.fill((0, 0, 0))
        game_window.blit(background_image, (0, 0))
        game_window.blit(floor_image, GameGround(0, 520))
        game_window.blit(flappy_images[0], (100, 250))
        game_window.blit(start_img, (window_width // 2 - start_img.get_width() // 2,
                                  window_height // 2 - start_img.get_height() // 2))

        # Player Input
        player_input = pygame.key.get_pressed()
        if player_input[pygame.K_SPACE]:
            game_main()

        pygame.display.update()


game_menu()
