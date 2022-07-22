from example_package_for_flf import fits


def test_enlarged_side_hex():

    this_should_not_fit = fits(
        apothem_radius=10,
        side_length=11.548,
        number_of_sides=6,
    )
    assert this_should_not_fit is False

def test_enlarged_side_hex_2():

    this_should_not_fit = fits(
        apothem_radius=1,
        side_length=1,
        number_of_sides=6,
    )
    assert this_should_not_fit is False

def test_enlarged_side_hex_3():

    this_should_not_fit = fits(
        apothem_radius=10,
        side_length=1,
        number_of_sides=6,
    )
    assert this_should_not_fit is True