from location import *
from locations_list import *
from prettytable import PrettyTable
import os


def print_menu():
    # clear()
    print('''
    What would you like to do:

        (1) List statistics
        (2) Display 3 cities with longest names
        (3) Display county's name with the largest number of communities
        (4) Display locations, that belong to more than one category
        (5) Advanced search

        (0) Exit program
        ''')


def display_statistic():
    stat = PrettyTable()

    stat.field_names = ['MAŁOPOLSKA', '']
    rows = Locations.get_statistic()
    for item in rows:
        stat.add_row(item)
    stat.align['MAŁOPOLSKA'] = "l"
    stat.align[''] = "r"
    stat.sortby="MAŁOPOLSKA"
    stat.reversesort = True
    print(stat)


def display_3longest_city_names():
    print('Cities with the longest name in MAŁOPOLSKA:')
    names_list = Locations.get_city_name()
    for name in names_list:
        print('\n\t{}'.format(name))


def display_county_name():
    name = Locations.largest_numb_of_communities()
    print('The name of the county with the largest number of communities is: {}'.format(name))

def dispaly_searching():
    result = PrettyTable()
    result.field_names = ['LOCATION', 'TYPE']
    phrase = get_user_input('Searching for: ')
    rows = Locations.search(phrase)
    for row in rows:
        result.add_row(row)
    result.align = 'l'
    print(result)

def get_user_input(title):
    answer = input(title)
    return answer


def clear():
    """
    Clears screen for better display
    :return None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
