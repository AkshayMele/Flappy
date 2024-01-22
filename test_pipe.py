import unittest
import pygame
from flappy import game_main, GamePipe  # Replace with the actual filename

class TestPipeSpawning(unittest.TestCase):
    def test_pipe_spawning(self):
        game_pipes = pygame.sprite.Group()
        initial_pipe_count = len(game_pipes)
        game_main()  # Run the game
        new_pipe_count = len(game_pipes)
        self.assertTrue(new_pipe_count > initial_pipe_count)  # New pipes should be added during the game

if __name__ == '__main__':
    unittest.main()