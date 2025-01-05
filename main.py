import time

from double_integral_sum import (
    get_double_integral_sum,
    get_tagged_partition_from_square,
)
from integral_config import (
    f_1,
    f_2,
    greens_theorem_function,
    is_inside_the_shape,
    natural_parametrization_path,
)
from vector_line_integral_sum import (
    calculate_vector_line_integral_sum,
    get_polyline_points,
    get_tags_polyline,
)
from latex import get_latex_table


def get_results_vector_line(delta: float) -> dict[str, float]:
    start_time = time.time()  # Start timing
    polyline = get_polyline_points(delta, natural_parametrization_path)
    tagged_partion = get_tags_polyline(polyline)
    true_value = 0  # got by analytical method
    integral_value = calculate_vector_line_integral_sum(
        polyline, tagged_partion, f_1, f_2
    )
    results = {
        "\\delta": delta,
        "интегральная сумма": integral_value,
        "отклонение": integral_value - true_value,
    }
    end_time = time.time()  # End timing

    execution_time = end_time - start_time

    results["время выполнения"] = execution_time
    return results


def get_results_double_integral(delta: float, include_boarders) -> dict[str, float]:
    start_time = time.time()  # Start timing
    tags = get_tagged_partition_from_square(
        delta, include_boarders, is_inside_the_shape, -5, 5, -5, 5
    )
    integral_value = get_double_integral_sum(delta, greens_theorem_function, tags)
    true_value = 0  # got by analytical method
    results = {
        "\\delta": delta,
        "интегральная сумма": integral_value,
        "отклонение": integral_value - true_value,
    }
    end_time = time.time()  # End timing

    execution_time = end_time - start_time

    results["время выполнения"] = execution_time
    return results


def test(delta_list: list[float], func, file_path):
    results = list[dict[str, float]]()

    for delta in delta_list:
        results.append(func(delta))

    with open(file_path, "w") as file:
        file.write(get_latex_table(results))


if __name__ == "__main__":

    default_delta_list = [0.1, 0.01, 0.001]

    test(
        default_delta_list,
        get_results_vector_line,
        "output/table_vector_line_integral.tex",
    )
    test(
        default_delta_list,
        lambda delta: get_results_double_integral(delta, False),
        "output/table_double_integral_without_boarders.tex",
    )
    test(
        default_delta_list,
        lambda delta: get_results_double_integral(delta, True),
        "output/table_double_integral_with_boarders.tex",
    )
