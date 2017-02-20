from location import *
from locations_list import *
import ui
import sys


def main():
    Locations.make_list_of_objects()
    while True:
        ui.print_menu()
        option = ui.get_user_input('Choose option: ')
        if option == '1':
            # print(Locations.get_statistic())
            ui.display_statistic()
            ui.get_user_input('Press any key to back.')
            continue
        elif option == '2':
            # print(Locations.get_city_name())
            ui.display_3longest_city_names()
            ui.get_user_input('Press any key to back.')
            continue
        elif option == '3':
            # print(Locations.largest_numb_of_communities())
            ui.display_county_name()
            ui.get_user_input('Press any key to back.')
            continue
        elif option == '4':
            print(Locations.many_categories())
            ui.get_user_input('Press any key to back.')
            continue
        elif option == '5':
            ui.dispaly_searching()
            # print(Locations.search('no'))
            ui.get_user_input('Press any key to back.')

        elif option == '0':
            sys.exit()

    # # print(Locations.read_csv())
    # Locations.make_list_of_objects()
    # # print(Locations.locations)
    # print(Locations.get_city_name())
    # print(Locations.get_statistic())
    # # Locations.count_commune()
    # # print(Locations.serch('Nowy'))
    # # print(Locations.many_categories())
    # print(Locations.largest_numb_of_communities())



if __name__ == '__main__':
        main()