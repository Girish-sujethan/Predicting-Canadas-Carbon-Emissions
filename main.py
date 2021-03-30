"""CSC110 Fall 2020 Final Project, Main File

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of Professors and TA's
teaching CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult the owners.

This file is Copyright (c) 2020 Carson, Kowan, Girish, Howard
"""
from typing import Dict, Tuple, List
import extraction
import linear_regression
import poly_regression
import threeD_graph
import calculations


def run_project() -> dict:
    """ This is the main function that runs everything."""
    all_files = [
        'Canada_-_CO2_emissions.csv',
        'China_-_CO2_emissions.csv',
        'Japan_-_CO2_emissions.csv',
        'Mexico_-_CO2_emissions.csv',
        'United_Kingdom_-_CO2_emissions.csv',
        'United_States_of_America_-_CO2_emissions_2.csv',
        'Niger_-_CO2_emissions.csv'
    ]

    all_data = get_all(all_files)
    all_point_data = convert_all(all_data)
    # Dear ta! data = run_project() will make the data variable contain a dict
    # this dict contains all data from all countries
    # The other functions in other files require points: Tuple[List, List]
    # This is simply data['country'] where country is the name of the country of data you wanna use
    # I hope this can help you with testing :)

    # Converts american units (imperial) to metric
    # The error below is a bug. us_conversion does its job
    calculations.us_conversion(all_point_data['United States'])
    # plots linear regression graphs for every country
    for data in all_point_data:
        linear_regression.run_example(all_point_data[data], data)
        # Can't run polynomial regression all at the same time because it lags and overlaps
    # Please use the magnifier button to zoom in and see the trend better for polynomial
    poly_regression.polynomial_regression(all_point_data['Canada'], 'Canada: Degree 5 polynomial regression')
    # creates a 3D scatter plot graph that shows GDP per capita vs CO2 emissions
    threeD_graph.call_3d_graph(all_point_data['Canada'][0], all_point_data['Canada'][1])
    compare_canada(all_point_data)
    # Output predicted values for the years of 2021,2025, and 2050
    # Uses polynomial regression of degree 5 to obtain values
    # Dear TA, sometimes plotly takes a long time to load.
    # While plotly loads, clicking the url and pressing enter
    # instantly loads the graph
    return all_point_data

# HELPER FUNCTIONS Below


def compare_canada(all_data: dict) -> None:
    """This function creates a linear regression for all
    data points in all countries excluding Canada
    """
    global_data_x = []
    global_data_y = []

    can_data = all_data.pop('Canada', None)

    for key, value in all_data.items():
        global_data_x = global_data_x + list(value)[0]
        global_data_y = global_data_y + list(value)[1]

    global_data = (global_data_x, global_data_y)
    linear_regression.run_example(global_data, "All countries data excluding Canada")

    all_data['Canada'] = can_data


def get_all(filenames: List[str]) -> List[Dict[str, List[Tuple[int, float]]]]:
    """ Return a list of dicts mapping country name to a List of tuples

    the tuples contain year and amount of carbon emissions

    Preconditions:
        - filenames != []
        - every element of filenames exists in the datasets folder
    """
    storage = list()
    for data in filenames:
        storage.append(extraction.get_data('datasets/' + data))

    return storage


def convert_all(data: List[Dict[str, List[Tuple[int, float]]]]) -> \
        Dict[str, Tuple[List[int], List[float]]]:
    """ Return a a dict mapping country names to a tuple of a list of years and list of emissions

        This function is used to format data so that it can be plotted on a graph.
        They years represent the x and the emissions represent the y.

        Preconditions:
            - data != []
    """
    stored_data = dict()
    for dict_set in data:
        current_dict = [country for country in dict_set][0]
        stored_data[current_dict] = ([year[0] for year in dict_set[current_dict]],
                                     [emission[1] for emission in dict_set[current_dict]])
    return stored_data



