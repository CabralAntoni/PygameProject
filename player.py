import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.maxHealth = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 450

    def moveRight(self):
        self.rect.x += self.velocity

    def moveLeft(self):
        self.rect.x -= self.velocity