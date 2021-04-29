import pygame
from game import Game

pygame.init()


# Fenetre PyGame

pygame.display.set_caption("L'arbre")
screen = pygame.display.set_mode((1080, 680))

# importe et charge arriere plan
background = pygame.image.load("assets/bg.jpg")
# charge Game
game = Game()


# Game Loop

running = True

while running:
    # draw l'arrière plan
    screen.blit(background, (0, -250))
    # draw joueur
    screen.blit(game.player.image, game.player.rect)

    # Update ecran

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.player.moveRight()
            elif event.key == pygame.K_LEFT:
                game.player.moveLeft()