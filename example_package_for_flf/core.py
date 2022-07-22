import math


def fits(
    number_of_sides: int = 5,
    side_length: float = 1.0,
    apothem_radius: float = 0.5,
) -> bool:
    """Tells us if a shape fits or not

    Args:
        number_of_sides: as named
        side_length: the length of each side
        apothem_radius: radius

    Returns:
        bool: if the shape overlaps (False) or not (True)

    """

    available_angle = 2 * math.pi / number_of_sides

    angle_required = math.atan(side_length / apothem_radius) * 2

    return angle_required <= available_angle


if __name__ == "__main__":
    does_it_fit = fits()
    print(does_it_fit)
