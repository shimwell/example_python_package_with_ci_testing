from example_package_for_flf import fits


def test_triangle_fit():

    this_should_fit = fits(
        apothem_radius=10,
        side_length=6,
        number_of_sides=3,
    )
    assert this_should_fit is True
