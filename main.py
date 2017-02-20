from locations_list import *
import ui
import sys


def main():
    Locations.make_list_of_objects()
    while True:
        ui.print_menu()
        option = ui.get_user_input('Choose option: ')
        if option == '1':
            ui.display_statistic()
            ui.get_user_input('\nPress any key to back.')
            continue
        elif option == '2':
            ui.display_3longest_city_names()
            ui.get_user_input('\nPress any key to back.')
            continue
        elif option == '3':
            ui.display_county_name()
            ui.get_user_input('\nPress any key to back.')
            continue
        elif option == '4':
            # print(Locations.many_categories())
            ui.dispaly_meny_categories_locations()
            ui.get_user_input('\nPress any key to back.')
            continue
        elif option == '5':
            ui.dispaly_searching()
            ui.get_user_input('\nPress any key to back.')

        elif option == '0':
            sys.exit()


if __name__ == '__main__':
        main()