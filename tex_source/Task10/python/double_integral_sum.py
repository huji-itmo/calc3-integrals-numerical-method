import math
from sys import stderr


def get_tagged_partition_from_square(
    delta: float,
    include_boarders: bool,
    is_inside_func,
    x_left: float,
    x_right,
    y_bottom: float,
    y_upper: float,
) -> list[tuple[float, float]]:
    if x_right < x_left or y_bottom > y_upper:
        print("wrong square boarder parameters.", file=stderr)

    horizontal_points_count: int = math.floor((x_right - x_left) / delta)
    vertical_points_count: int = math.floor((y_upper - y_bottom) / delta)
    tags = list[tuple[float, float]]()  # оснащение

    for i in range(vertical_points_count - 1):
        for j in range(horizontal_points_count - 1):
            left_upper_point = (x_left + j * delta, y_upper - i * delta)
            right_upper_point = (x_left + (j + 1) * delta, y_upper - i * delta)
            left_bottom_point = (x_left + j * delta, y_upper - (i + 1) * delta)
            right_bottom_point = (x_left + (j + 1) * delta, y_upper - (i + 1) * delta)

            points_inside: list[bool] = map(
                is_inside_func,
                [
                    left_upper_point,
                    right_upper_point,
                    left_bottom_point,
                    right_bottom_point,
                ],
            )
            if not all(points_inside) and not (include_boarders and any(points_inside)):
                # square is outside of the shape or on a boarder when boarders not allowed
                continue

            # at the center of a square
            x1, y1 = left_upper_point
            x2, y2 = right_bottom_point
            tag = (
                (x1 + x2) / 2,
                (y1 + y2) / 2,
            )
            tags.append(tag)

    return tags


def get_double_integral_sum(
    delta: float, func, tags: list[tuple[float, float]]
) -> float:
    measure = delta * delta  # square with the sides of delta

    return sum([func(xy) * measure for xy in tags])
