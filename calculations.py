"""CSC110 Fall 2020 Final Project, Linear Regression

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of Professors and TA's
teaching CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult the owners.

This file is Copyright (c) 2020 Carson, Kowan, Girish, Howard
"""
from typing import List, Tuple
import numpy as np
import linear_regression


def rmse_polynomial_regression(points: Tuple[List, List]) -> float:
    """The same as rmse_linear_regression but for polynomial regression lines instead
    """
    # Getting the polynomial line
    x_coordinates = points[0]
    y_coordinates = points[1]
    poly_fit = np.poly1d(np.polyfit(x_coordinates, y_coordinates, 5))

    sum_so_far = 0
    for point_num in range(0, len(x_coordinates)):
        # line_value means the value y for the linear regression line
        # basically finding y for y = a + bx
        line_value = poly_fit(x_coordinates[point_num])
        # adding the squared residual value
        sum_so_far = sum_so_far + (y_coordinates[point_num] - line_value) ** 2

    return (sum_so_far / len(x_coordinates)) ** 0.5


def rmse_linear_regression(points: Tuple[List, List]) -> float:
    """Root Mean Squared Error method used to calculate the error of regression lines
    Basically a measure of how far the regression line data points are from the actual points
    This is calculated by squaring the residuals (distance from linear regression and actual point),
    finding the average, and taking the square root of that value
    """
    # Separating x and y coordinates
    x_coordinates = points[0]
    y_coordinates = points[1]
    # getting a and b for y = a + bx
    slope_values = linear_regression.simple_linear_regression(points)
    a = slope_values[0]
    b = slope_values[1]

    sum_so_far = 0
    for point_num in range(0, len(x_coordinates)):
        # line_value means the value y for the linear regression line
        # AKA finding y for y = a + bx
        line_value = b * x_coordinates[point_num] + a
        # adding the squared residual value
        sum_so_far = sum_so_far + (y_coordinates[point_num] - line_value) ** 2
    # Finding the average, and finding the square root
    return (sum_so_far / len(x_coordinates)) ** 0.5


def iroc(year: int, data: Tuple[List, List]) -> int:
    """Calculates the instantaneous rate of change
    IROC is the derivative at a point
    Preconditions:
        - year_start >= min(x)
        - year_end <= max(x)
        - year_start < year_end
    """
    # Getting the polynomial line
    x = data[0]
    y = data[1]
    poly_fit = np.poly1d(np.polyfit(x, y, 5))

    return (poly_fit(year + 0.001) - poly_fit(year)) / 0.001


def aroc(year_start: int, year_end: int, points: Tuple[List, List]) -> int:
    """Calculates the average rate of change
    AROC is delta x over delta y
    It is basically the slope from point_a to point_b
    Preconditions:
        - year_start >= min(x)
        - year_end <= max(x)
        - year_start < year_end
    """
    # Getting the polynomial line
    x_coordinates = points[0]
    y_coordinates = points[1]
    poly_fit = np.poly1d(np.polyfit(x_coordinates, y_coordinates, 5))
    return (poly_fit(year_end) - poly_fit(year_start)) / (year_end - year_start)


def us_conversion(data: Tuple[list, list]) -> None:
    """Converts data from imperial  tonnes to metric tonnes"""
    for x in range(0, len(data[0])):
        data[1][x] = data[1][x] * 1.01605


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'plotly.graph_objects',
                          'extraction', 'numpy', 'linear_regression'],
        'allowed-io': [],
        'disable': ['R1705']
    })

    import python_ta.contracts
    import doctest

    doctest.testmod()
