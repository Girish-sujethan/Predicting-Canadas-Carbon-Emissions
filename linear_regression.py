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
import random
from typing import List, Tuple
import plotly.graph_objects as go


def run_example(points: Tuple[List, List], title: str) -> tuple:
    """Creates a linear regression model using plotly

    The x and y values are isolated then graphed

    Preconditions:
        - points != ()
        - points[0] != []
        - points[1] != []
    """

    # Run simple linear regression to find the slope and the value it starts at (a and b)
    # a and b for y = a + bx
    slope_values = simple_linear_regression(points)
    a = slope_values[0]
    b = slope_values[1]

    # Plot the data and graph the regression line
    plot_points_and_regression(points,
                               a,
                               b,
                               title)

    return (a, b)


# Linear regression modified from assignment 1
def plot_points_and_regression(points: Tuple[List, List],
                               a: float, b: float, title: str) -> None:
    """Plot the given x- and y-coordinates and linear regression model using plotly.

    plot_points_and_regression is modified so it works when the x
    value starts at something other than 0
    """
    # Separate x and y values
    x_coordinates = points[0]
    y_coordinates = points[1]
    # Create max and min
    x_min = min(x_coordinates)
    x_max = max(x_coordinates)
    # Create a blank figure
    fig = go.Figure()
    # Create head title, x-axis title, and y-axis title
    fig.update_layout(title='Country: ' + title + ' Carbon Emissions', xaxis_title='Year',
                      yaxis_title='Carbon Emission (Metric Tonnes)')

    # Add the raw data
    fig.add_trace(go.Scatter(x=x_coordinates, y=y_coordinates, mode='markers', name='Data'))

    # Add the regression line
    fig.add_trace(go.Scatter(x=[x_min, x_max], y=[evaluate_line(a, b, 0, x_min),
                                                  evaluate_line(a, b, 0, x_max)],
                             mode='lines', name='Regression line'))
    # made it start at x_min and end at x_max so it doesn't start from 0
    # since the first year is already in the 1900's, and not 0
    # Display the figure in a web browser
    fig.show()


def simple_linear_regression(points: Tuple[List, List]) -> tuple:
    """Return a tuple containing slope and y intercept value

    slope is represented by a and y intercept is represented by b

    Preconditions:
        - points != ()
        - points[0] != []
        - points[1] != []
    """

    mean_x = sum(points[0]) / len(points[0])
    mean_y = sum(points[1]) / len(points[1])

    sum1 = sum([(x - mean_x) * (y - mean_y)
                for x in points[0]
                for y in points[1] if list.index(points[0], x)
                == list.index(points[1], y)])
    sum2 = sum([(x - mean_x) ** 2 for x in points[0]])

    b = sum1 / sum2
    a = mean_y - (b * mean_x)
    return (a, b)

# Evaluate line is from the assignment


def evaluate_line(a: float, b: float, error: float, x: float) -> float:
    """Evaluate the linear function y = a + bx for the given a, b, and x values
    with the given error term.

    >>> result = evaluate_line(5.0, 1.0, 0.5, 10.0)  # y = 5.0 + 1.0 * 10.0, with error 0.5
    >>> -0.5 <= result - 15.0 <= 0.5
    True
    """
    if error == 0:
        return a + b * x
    else:
        return a + b * x + random.uniform(-error, error)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'random', 'plotly.graph_objects'],
        'allowed-io': [],
        'disable': ['R1705']
    })

    import python_ta.contracts

    import doctest

    doctest.testmod()
