from ml.dataset import Dataset


def XOR():

    red_points = [
        (-2.0, 1.2, 0),
        (-0.8, 2.0, 0),
        (1.2, 0.8, 0),
    ]

    blue_points = [
        (-1.5, -1.4, 0),
        (0.8, -0.8, 0),
        (2.0, 1.8, 0),
    ]

    return Dataset(
        red_points=red_points,
        blue_points=blue_points,
    )