import pytest
from geo.data import Point, Polygon

# doc pytest fixtures
# https://docs.pytest.org/en/8.2.x/how-to/fixtures.html
# https://docs.pytest.org/en/8.2.x/reference/fixtures.html

@pytest.fixture
def pentagon_wikipedia() -> Polygon:
    return Polygon(
        Point.from_coords(1, 6),
        Point.from_coords(3, 1),
        Point.from_coords(7, 2),
        Point.from_coords(4, 4),
        Point.from_coords(8, 5),
        name="P"
    )  

def test_surface(pentagon_wikipedia: Polygon):
    actual_surface = pentagon_wikipedia.surface()
    assert 16.5 == actual_surface
    
def test_perimeter(pentagon_wikipedia: Polygon):
    actual_perimeter = pentagon_wikipedia.perimeter()
    assert pytest.approx(24.308, 1E-3) == actual_perimeter