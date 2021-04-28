import pygame
pygame.init()

# Fenetre PyGame

pygame.display.set_caption("L'arbre")
screen = pygame.display.set_mode((1080, 680))

# init
background = pygame.image.load("assets/bg.jpg")


# Game Loop

running = True


while running:
    #applique l'arrière plan
    screen.blit(background, (0, -250))

    #Update ecran
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()