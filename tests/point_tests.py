import pytest
from point import Point

@pytest.fixture
def sample_point():
    return Point(0, 0, [], None)

def test_point_creation(sample_point):
    assert sample_point.x == 0
    assert sample_point.y == 0

def test_push_method(sample_point):
    sample_point.push()
    assert sample_point.open == True

def test_flag_method(sample_point):
    sample_point.p_flag()
    assert sample_point.flag == True

def test_get_surface_rect_method(sample_point):
    surface_rect = sample_point.get_surface_rect()
    assert surface_rect.width == sample_point.rect.width
    assert surface_rect.height == sample_point.rect.height * 0.1