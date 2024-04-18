import pytest
from textsprite import TextSprite

@pytest.fixture
def sample_text_sprite():
    return TextSprite(0, 0)

def test_text_sprite_creation(sample_text_sprite):
    assert sample_text_sprite.x == 0
    assert sample_text_sprite.y == 0

def test_set_text_method(sample_text_sprite):
    sample_text_sprite.setText('Test')
    assert sample_text_sprite.text == 'Test'

def test_set_color_method(sample_text_sprite):
    sample_text_sprite.setColor((255, 0, 0))
    assert sample_text_sprite.color == (255, 0, 0)

def test_set_size_method(sample_text_sprite):
    sample_text_sprite.setSize(30)
    assert sample_text_sprite.font.get_height() == 30