import matplotlib.pyplot as plt


def construct_polyline(points):
    x_coords, y_coords = zip(*points)

    plt.plot(x_coords, y_coords, marker="o")

    plt.title("Polyline from List of Points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.axhline(
        0, color="black", linewidth=0.5, label="OX (X-axis)"
    )  # Horizontal line (OY)
    plt.axvline(
        0, color="black", linewidth=0.5, label="OY (Y-axis)"
    )  # Vertical line (OX)

    plt.grid(True)
    plt.show()


import matplotlib.pyplot as plt


def plot_tagged_partition(
    polyline_points: list[tuple[float, float]],
    tagging_points: list[tuple[float, float]],
    path: str,
):
    x_coords, y_coords = zip(*polyline_points)

    plt.plot(
        x_coords, y_coords, marker="o", linestyle="-", color="blue", label="Polyline"
    )

    if tagging_points:
        tag_x, tag_y = zip(*tagging_points)
        plt.scatter(
            tag_x, tag_y, marker="x", color="red", s=100, label="Tagging Points"
        )

    plt.axhline(0, color="black", linewidth=0.5)  # Horizontal line (OY)
    plt.axvline(0, color="black", linewidth=0.5)  # Vertical line (OX)

    plt.title("Polyline with Tagging Points for Partition")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.legend()

    plt.grid(True)
    plt.savefig(path)
