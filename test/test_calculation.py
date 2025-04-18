from area_calculation.calculation import rectangle_area, triangle_area


def test_rectangle_of_different_dimmensions():
    assert rectangle_area(4,5) == 20

def test_rectangle_of_same_dimmensions():
    assert rectangle_area(5,5) == 25

def test_triangle_area():
    assert triangle_area(5,4) == 10