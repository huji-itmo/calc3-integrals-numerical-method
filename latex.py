def get_latex_table(results: list[dict[str, float]]) -> str:
    if len(results) == 0:
        return

    width = len(results[0].keys())
    output = "\\begin{tabular}{|" + "|".join(["c"] * width) + "|}\n"

    # header for the table
    output += f"    \\hline\n"
    output += f"    {' & '.join(results[0].keys())}\\\\\n"
    output += f"    \\hline\n"

    for data in results:
        output += f"    {' & '.join( [str(round(x,6)) for x in data.values()] )}\\\\\n"
        output += f"    \\hline\n"

    output += "\\end{tabular}"
    return output
