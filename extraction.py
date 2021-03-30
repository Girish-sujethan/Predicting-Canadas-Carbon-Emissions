"""CSC110 Fall 2020 Final Project, Extraction File

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of Professors and TA's
teaching CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials
please consult the owners.

This file is Copyright (c) 2020 Carson, Kowan, Girish, Howard
"""

import csv
from typing import List, Tuple, Dict


def get_data(filename: str) -> Dict[str, List[Tuple[int, float]]]:
    """ Return a dictionary of of country to tuple.

    The tuple has two values, a year and carbon emission amount

    Preconditions:
        - files are csv files
        - files follow the format as Canada_-_CO2_emissions.csv file format
        - filename is a filepath that leads to a valid csv file outlined above
    """
    with open(filename) as file:
        reader = csv.reader(file)

        # get header for dates
        headers = next(reader)
        data = next(reader)
        country = data[3]

        # format data and return it
        country_data = {country: [(int(headers[pos]), float(data[pos]))
                                  for pos in range(4, len(headers))]}
    return country_data


def get_gdp(filename: str) -> List[float]:
    """ Return a list of a countries gdp from 1970 to 2018

        The list is ordered from 1970 to 2018 values

        Preconditions:
            - files are csv files
            - files follow the format as Canada_GDP.csv file format
            - filename is a filepath that leads to a valid csv file outlined above
    """
    gdp_so_far = []
    reversed_gdp_so_far = []

    with open(filename) as file:
        reader = csv.reader(file)

        # skip header
        next(reader)
        data = next(reader)
        while 1970 <= int(data[0]) <= 2018:
            gdp_so_far.append(data[1])
            data = next(reader)

    # flip the list so the last item is the first item
    while gdp_so_far != []:
        reversed_gdp_so_far.append(gdp_so_far.pop())

    return reversed_gdp_so_far


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'csv'],
        'allowed-io': ['get_gdp', 'get_data'],
        'disable': ['R1705']
    })

    import python_ta.contracts

    import doctest

    doctest.testmod()
