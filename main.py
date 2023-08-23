# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

# Path to initial background image
bg_img_path = "./pirates-2023-hy2/assets/floor_1.png" 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bg_img_path = "./pirates-2023-hy2/assets/floor_2.png"
    if keys[pygame.K_s]:
        bg_img_path = "./pirates-2023-hy2/assets/floor_1.png"

    # fill the screen with a color to wipe away anything from last frame
    bg_img = pygame.image.load(bg_img_path)
    bg_img = pygame.transform.scale(bg_img,(screen_width, screen_height))
    screen.blit(bg_img, (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

#End Game
pygame.quit()
