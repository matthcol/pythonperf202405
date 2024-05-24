import pytest
from geo.data import Point

def test_translate():
    pt = Point(x=2.5, y=1.25)
    pt.translate(1.5, -0.5)
    assert pt.x == 4.0, "x"
    assert pt.y == 0.75, "y"

@pytest.mark.parametrize(
    ["x1", "y1", "x2", "y2", "expected_distance"],
    [
        (1.0, 2.0, 4.0, 6.0, 5.0),
        (1.5, 2.25, 5.5, -0.75, 5.0),
        (1.5E300, 2.25E300, 5.5E300, -0.75E300, 5.0E300),
        (1.5E-300, 2.25E-300, 5.5E-300, -0.75E-300, 5.0E-300),
    ],
    ids=[
        "integer coordinates",
        "decimal exact coordinates",
        "big scale",
        "tiny scale",
    ]
)
def test_distance(x1, y1, x2, y2, expected_distance):
    pt1 = Point(x=x1, y=y1)
    pt2 = Point(x=x2, y=y2)
    actual_distance = pt1.distance(pt2)
    assert expected_distance == actual_distance