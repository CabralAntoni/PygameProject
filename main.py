import pygame

pygame.init()

class Game :

    def __init__(self):
        self.player = Player()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.maxHealth = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 450


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
