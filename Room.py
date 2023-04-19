import pygame

Screen_Dimensions = pygame.display.set_mode((1920,1880))

class Room1:
    def __init__(self, Room1image):
        self.background = pygame.image.load(Room1image)
        self.Scaled_Background = pygame.transform.scale(self.background, (1950, 1000))
        Screen_Dimensions.blit(self.Scaled_Background, (0, 0))


