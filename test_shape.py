from core import fits


def test_triangle_fit():

    this_should_fit = fits(
        apothem_radius=10,
        side_length=6,
        number_of_sides=3,
    )
    assert this_should_fit is True


def test_enlarged_side_hex():

    this_should_not_fit = fits(
        apothem_radius=10,
        side_length=11.548,
        number_of_sides=6,
    )
    assert this_should_not_fit is False
