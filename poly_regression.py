"""CSC110 Fall 2020 Final Project, Polynomial Regression

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
from matplotlib import pyplot as plt


def polynomial_regression(points: Tuple[List, List], title: str) -> None:
    """  Displays a graph showing the polynomial regression with degree 5 .
        Requires a tuple with a list of x values and a list of y values.

        Preconditions:
            - points[0] != []
            - points[1] != []
            - len(points[0]) == len(points[1])
    """
    x = points[0]
    y = points[1]
    poly_fit = np.poly1d(np.polyfit(x, y, 5))

    # Plot data
    xx = np.linspace(1970, 2018, 1000)
    plt.plot(xx, poly_fit(xx), c='r', linestyle='-')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Carbon Emissions (Metric Tonnes)')
    plt.axis([1970, 2018, 0, 7000])
    plt.grid(True)
    plt.scatter(x, y)
    plt.show()


def polynomial_prediction(points: Tuple[List, List], country: str) -> str:
    """ Requires a tuple with a list of x values and a list of y values, and string of country name
    Returns a string that contains  the predicted values for 2021, 2025, and 2050

    Preconditions:
            - points[0] != []
            - points[1] != []
            - len(points[0]) == len(points[1])
    >>> points = all_data_points[Canada]
    >>> polynomial_prediction(points, "Canada")
    'Projected emissions for Canada in 2021: 645.4273681640625. projected emissions for Canada \
    in 2025: 797.228515625. projected emissions for Canada in 2050: 11505.441650390625'
    """

    x = points[0]
    y = points[1]
    # creates polynomial model
    poly_fit = np.poly1d(np.polyfit(x, y, 5))

    string = "Projected emissions for " + country + " in 2021: " + str(poly_fit(2021)) + \
             ". projected emissions for " + country + " in 2025: " + \
             str(poly_fit(2025)) + ". projected emissions for " + country +\
             " in 2050: " + str(poly_fit(2050))
    return string


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['numpy', 'python_ta.contracts', 'mathplotlib', 'plotly', 'matplotlib'],
        'allowed-io': [],
        'disable': ['R1705']
    })

    import python_ta.contracts

    import doctest

    doctest.testmod()
