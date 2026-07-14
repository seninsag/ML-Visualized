from ml.dataset import Dataset


def Easy():

    red_points = [
        (-2.2, 1.6, 0),
        (0.0, 1.8, 0),
        (2.2, 1.5, 0),
    ]

    blue_points = [
        (-2.2, -1.6, 0),
        (0.0, -1.8, 0),
        (2.2, -1.5, 0),
    ]

    return Dataset(
        red_points=red_points,
        blue_points=blue_points,
    )