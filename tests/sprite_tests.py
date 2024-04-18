import pytest
from sprite import Sprite

@pytest.fixture
def sample_sprite():
    return Sprite(0, 0)

def test_sprite_creation(sample_sprite):
    assert sample_sprite.x == 0
    assert sample_sprite.y == 0

def test_move_x_method(sample_sprite):
    sample_sprite.move_x(10)
    assert sample_sprite.x == 10

def test_move_y_method(sample_sprite):
    sample_sprite.move_y(-5)
    assert sample_sprite.y == -5
