"""CSC110 Fall 2020 Final Project, 3D graph

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of Professors and TA's
teaching CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult the owners.

This file is Copyright (c) 2020 Carson, Kowan, Girish, Howard
"""
import plotly.graph_objects as go
import numpy as np
import extraction


def call_3d_graph(x: list, y: list) -> None:
    """Creates a 3d scatter graph using plotly
        Requires a list of x values and a list of y values
        Creates a graph that compares GDP per capita to CO2 emissions
        Preconditions:
            - x != []
            - y != []
            - len(x) == len(y)
    """

    # Extracts the GDP data set
    z = extraction.get_gdp('datasets/Canada_GDP.csv')
    # creates a 3D figure
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
    fig.update_layout(title='Canada GDP per Capita vs CO2 emissions', scene=dict(xaxis_title='Years',
                                                                                 yaxis_title='Carbon Emission'
                                                                                             ' (Metric Tonnes)',
                                                                                 zaxis_title='GDP per Capita'))
    fig.show()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'plotly.graph_objects', 'extraction', 'numpy'],
        'allowed-io': [],
        'disable': ['R1705']
    })

    import python_ta.contracts
    import doctest
    doctest.testmod()
