import pytest
from circle import Circle
from point import Point

def test_init_radius_negative_or_null():
    radius = -1
    p = Point()
    with pytest.raises(ValueError, match=r"radius must be > 0: .*"):
        c = Circle("C", center=p, radius=radius)