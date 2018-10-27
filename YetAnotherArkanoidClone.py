"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
BACKGROUNDGRAY = (100, 100, 100)
WALLGRAY = (150, 150, 150)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUNDGRAY)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, WALLGRAY, [0, 0, 30, 500])
    pygame.draw.rect(screen, WALLGRAY, [480, 0, 30, 500])
    pygame.draw.rect(screen, WALLGRAY, [0, 0, 480, 30])

    pygame.draw.rect(screen, BLUE, [510, 100, 60, 25])
    pygame.draw.rect(screen, BLUE, [110, 100, 60, 200])
    pygame.draw.rect(screen, GREEN, [170, 100, 60, 200])
    pygame.draw.rect(screen, BLUE, [230, 100, 60, 200])
    pygame.draw.rect(screen, GREEN, [290, 100, 60, 200])
    pygame.draw.rect(screen, BLUE, [350, 100, 60, 200])


    pygame.draw.rect(screen, RED, [210, 450, 100, 15])
    pygame.draw.circle(screen, BLACK, [260, 420], 10)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()