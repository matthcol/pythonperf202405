import pytest
from point import Point

def test_translate():
    pt = Point(2.5, 1.25)
    pt.translate(1.5, -0.5)
    assert pt.x == 4.0, "x"
    assert pt.y == 0.75, "y"

@pytest.mark.parametrize(
    ["x1", "y1", "x2", "y2", "expected_distance"],
    [
        (1.0, 2.0, 4.0, 6.0, 5.0),
        (1.5, 2.25, 5.5, -0.75, 5.0),
    ],
    ids=[
        "integer coordinates",
        "decimal exact coordinates",
    ]
)
def test_distance(x1, y1, x2, y2, expected_distance):
    pt1 = Point(x1, y1)
    pt2 = Point(x2, y2)
    actual_distance = pt1.distance(pt2)
    assert expected_distance == actual_distance