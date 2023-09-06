import pytest
from jogo import calcula_colisao_chao


class MockSprite:
    def __init__(self, rect_bottom, rect_x, rect_width, speedY):
        self.rect = MockRect(rect_bottom, rect_x, rect_width)
        self.speedY = speedY

class MockRect:
    def __init__(self, bottom, x, width):
        self.bottom = bottom
        self.x = x
        self.width = width

def test_sprite_above_ground():
    sprite = MockSprite(700, 100, 50, 2)  
    calcula_colisao_chao(sprite)
    assert sprite.rect.bottom == 672
    assert sprite.speedY == 0

def test_sprite_below_ground():
    sprite = MockSprite(600, 100, 50, 2) 
    calcula_colisao_chao(sprite)
    assert sprite.rect.bottom == 600
    assert sprite.speedY == 2

