import unittest
import pygame
from flappy import game_main, Flappy, GamePipe, GameGround  # Replace with the actual filename

class TestCollisionDetection(unittest.TestCase):
    def test_collision_detection(self):
        flappy = Flappy()
        game_pipes = pygame.sprite.Group(GamePipe(100, 100, pipe_top_image, 'top'))
        game_ground = pygame.sprite.Group(GameGround(0, 520))
        flappy.rect.y = 90  # Set Flappy's position to collide with pipes
        flappy.sprite.is_alive = True  # Ensure Flappy is alive
        game_main()  # Run the game
        self.assertFalse(flappy.sprite.is_alive)  # Flappy should not be alive after collision

if __name__ == '__main__':
    unittest.main()