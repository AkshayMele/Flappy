import unittest
import pygame
from flappy import game_main, GamePipe  # Replace with the actual filename

class TestFlappyMovement(unittest.TestCase):
    def test_flappy_movement(self):
        flappy = Flappy()
        initial_position = flappy.rect.y
        flappy.update({pygame.K_SPACE: False})  # Simulate no key pressed
        self.assertTrue(flappy.rect.y > initial_position)  # Flappy should move down due to gravity
        flappy.update({pygame.K_SPACE: True})  # Simulate space key pressed
        self.assertTrue(flappy.rect.y < initial_position)  # Flappy should move up due to flapping

if __name__ == '__main__':
    unittest.main()