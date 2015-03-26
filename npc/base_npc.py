import pygame, npc
from pygame.sprite import Sprite

SIZE = 20

class BaseNPC(Sprite):
    """
    Base NPC respresentation for which predators and prey extend from.
    """

    #active_NPCs =  pygame.sprite.LayeredUpdates()

    def __init__(self,
                 x_pos = 0,
                 y_pos = 0):

        Sprite.__init__(self)


        # Default Initialized values
        self.mode = "Neutral"
        self.health = 10
        self.speed = 10
        self.atk = 1
        self.type = "Base NPC"
        self.dir = 0
        
        
        # Required pygame parameters
        self.image = None
        self.rect = pygame.Rect(0,0,1,1)
        self.rect.x = x_pos
        self.rect.y = y_pos
        
        #if activate:
          #  self.activate()

    def set_npc_mode(self, mode):
        if mode == "Neutral":
            self.mode = "Neutral"
        if mode == "Fight":
            self.mode = "Fight"
        if mode == "Escape":
            self.mode = "Escape"



