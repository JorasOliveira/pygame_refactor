import unittest
import pygame
import os
import sys

pygame.init()

# Import the Startscreen class (assuming it's defined in a separate module)
from jogo import Startscreen, Background, Jogador1, Jogador2, Bola, Campo, End_screen   # Replace 'your_module_name' with the actual module name

class TestStartscreen(unittest.TestCase):
    def setUp(self):
        # Create a Pygame screen for testing purposes (you can use a fake screen)
        self.screen = pygame.Surface((800, 600))

    def test_startscreen_creation(self):
        # Create a Startscreen object
        startscreen = Startscreen()

        # Check if the Startscreen object was created successfully
        self.assertIsInstance(startscreen, Startscreen)
        self.assertIsInstance(startscreen.image, pygame.Surface)
        self.assertIsInstance(startscreen, pygame.sprite.Sprite)

    def tearDown(self):
        # Quit Pygame to clean up resources
        pygame.quit()

class TestBackground(unittest.TestCase):
    def setUp(self):
        # Create a Pygame screen for testing purposes (you can use a fake screen)
        self.screen = pygame.Surface((800, 600))

    def test_startscreen_creation(self):
        # Create a Startscreen object
        back = Background()

        # Check if the Startscreen object was created successfully
        self.assertIsInstance(back, Background)
        self.assertIsInstance(back.image, pygame.Surface)
        self.assertIsInstance(back, pygame.sprite.Sprite)

    def tearDown(self):
        # Quit Pygame to clean up resources
        pygame.quit()


class TestJogador1(unittest.TestCase):
    def setUp(self):
        # Create a Pygame screen for testing purposes (you can use a fake screen)
        self.screen = pygame.Surface((800, 600))

    def test_startscreen_creation(self):
        # Create a Startscreen object
        jog1 = Jogador1(0, 0, 'block')

        # Check if the Startscreen object was created successfully
        self.assertIsInstance(jog1, Jogador1)
        self.assertIsInstance(jog1.image, pygame.Surface)
        self.assertIsInstance(jog1, pygame.sprite.Sprite)

    def tearDown(self):
        # Quit Pygame to clean up resources
        pygame.quit()


class TestJogador2(unittest.TestCase):
    def setUp(self):
        # Create a Pygame screen for testing purposes (you can use a fake screen)
        self.screen = pygame.Surface((800, 600))

    def test_startscreen_creation(self):
        # Create a Startscreen object
        jog2 = Jogador2(0, 0, 'block')

        # Check if the jog2 object was created successfully
        self.assertIsInstance(jog2, Jogador2)
        self.assertIsInstance(jog2.image, pygame.Surface)
        self.assertIsInstance(jog2, pygame.sprite.Sprite)

    def tearDown(self):
        # Quit Pygame to clean up resources
        pygame.quit()

class TestBola(unittest.TestCase):
    def setUp(self):
        # Create a Pygame screen for testing purposes (you can use a fake screen)
        self.screen = pygame.Surface((800, 600))

    def test_startscreen_creation(self):
        # Create a Startscreen object
        ball = Bola(0, 0, 'block')

        # Check if the Startscreen object was created successfully
        self.assertIsInstance(ball, Bola)
        self.assertIsInstance(ball.image, pygame.Surface)
        self.assertIsInstance(ball, pygame.sprite.Sprite)

    def tearDown(self):
        # Quit Pygame to clean up resources
        pygame.quit()


class TestCampo(unittest.TestCase):
    def setUp(self):
        # Create a Pygame screen for testing purposes (you can use a fake screen)
        self.screen = pygame.Surface((800, 600))

    def test_startscreen_creation(self):
        # Create a Startscreen object
        camp = Campo()

        # Check if the Startscreen object was created successfully
        self.assertIsInstance(camp, Campo)
        self.assertIsInstance(camp.image, pygame.Surface)
        self.assertIsInstance(camp, pygame.sprite.Sprite)

    def tearDown(self):
        # Quit Pygame to clean up resources
        pygame.quit()



class TestEnd_screen(unittest.TestCase):
    def setUp(self):
        # Create a Pygame screen for testing purposes (you can use a fake screen)
        self.screen = pygame.Surface((800, 600))

    def test_startscreen_creation(self):
        # Create a Startscreen object
        endscreen = End_screen()

        # Check if the Startscreen object was created successfully
        self.assertIsInstance(endscreen, End_screen)
        self.assertIsInstance(endscreen.image, pygame.Surface)
        self.assertIsInstance(endscreen, pygame.sprite.Sprite)

    def tearDown(self):
        # Quit Pygame to clean up resources
        pygame.quit()


if __name__ == '__main__':
    unittest.main()

