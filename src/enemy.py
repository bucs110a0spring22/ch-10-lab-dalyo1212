import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
        """
        in this function the x and y function were given a random variable
        """
        # rand_move = random.randint(-1,1)
        if self.rect.x > 0 and self.rect.y > 0:
          self.rect.x -= 1
          self.rect.y -= 1
        if self.rect.x == 0 or self.rect.y == 0:
          self.rect.x = random.randrange(1, 600)
          self.rect.y = random.randrange(1, 400)