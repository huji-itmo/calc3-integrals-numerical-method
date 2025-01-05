import math

def get_polyline_points(
    delta: float, natural_parametrization_path
) -> list[tuple[float, float]]:
    # в идеале нас нужна натуральная параметризация
    result = []

    t = 0
    x, y = natural_parametrization_path(t)
    while not math.isnan(x) or not math.isnan(y):
        result.append((x, y))
        t += delta
        x, y = natural_parametrization_path(t)

    return result


def get_tags_polyline(
    polyline_points: list[tuple[float, float]]
) -> list[tuple[float, float]]:

    integration_points = list[tuple[float, float]]()

    for i in range(len(polyline_points) - 1):
        x_curr, y_curr = polyline_points[i]
        x_next, y_next = polyline_points[i + 1]

        integration_points.append(((x_curr + x_next) / 2, (y_curr + y_next) / 2))

    return integration_points


def calculate_vector_line_integral_sum(
    polyline_points: list[tuple[float, float]],
    tagging_points: list[tuple[float, float]],
    x_func,
    y_func,
) -> float:
    integral_sum = 0

    for i in range(len(tagging_points)):
        # for x, and then for y
        x_curr, y_curr = polyline_points[i]
        x_next, y_next = polyline_points[i + 1]
        delta_x = x_next - x_curr
        delta_y = y_next - y_curr

        integral_sum += x_func(tagging_points[i]) * delta_x
        integral_sum += y_func(tagging_points[i]) * delta_y

    return integral_sum
