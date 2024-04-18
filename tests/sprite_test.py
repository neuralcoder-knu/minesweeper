import pytest
from sprite import Sprite

@pytest.fixture
def sample_sprite():
    return Sprite(0, 0)

def test_sprite_creation(sample_sprite):
    assert sample_sprite.x == 0
    assert sample_sprite.y == 0
