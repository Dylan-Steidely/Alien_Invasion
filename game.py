import sys
import pygame
class AlienInvasion:
    """ Overall Class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game, and create game resources"""
        pygame.init()

        sel.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Alien Invasion")

        # Set Background color
        self.bg.color = (230,230,230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make The most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()