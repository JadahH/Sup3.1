from area_calculation.calculation import rectangle_area


def test_rectangle_of_different_dimmensions():
    assert rectangle_area(4,5) == 20

def test_rectangle_of_same_dimmensions():
    assert rectangle_area(5,5) == 25