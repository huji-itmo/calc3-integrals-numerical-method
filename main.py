import time

from integral_config import f_1, f_2, natural_parametrization_path
from vector_line_integral_sum import get_vector_line_integral_sum_results
from latex import get_latex_table

def get_full_results(delta: float) -> dict[str, float]:
    start_time = time.time()  # Start timing
    results = get_vector_line_integral_sum_results(delta, natural_parametrization_path, f_1, f_2)
    end_time = time.time()  # End timing

    execution_time = end_time - start_time

    results["время выполнения"] = execution_time;
    return results;

if __name__ == "__main__":
    results = list[dict[str, float]]()

    for delta in [0.1, 0.01, 0.001]:
        results.append(get_full_results(delta))

    with open("output/table.tex", "w") as file:
        file.write(get_latex_table(results))
