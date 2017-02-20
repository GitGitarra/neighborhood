from location import *
import csv


class Locations:

    locations = []

    @classmethod
    def add_location(cls, loc):
        cls.locations.append(loc)

    @classmethod
    def get_city_name(cls):
        cities = []
        for loc in cls.locations:
            if loc.commune_type == '4':
                cities.append(loc.get_name())
        longest_names = sorted(cities, key=len)[-3:]
        return longest_names

    @classmethod
    def get_statistic(cls):
        county_type = []
        for location in cls.locations:
            county_type.append(location.type_name)
        count_types = {i:county_type.count(i) for i in county_type}
        statistic = []
        for key, value in count_types.items():
            statistic.append([key, value])
        return statistic


        # wojewodztwo = 0
        # powiat = 0
        # gmina_miejska1 = 0
        # gmina_wiejska2 = 0
        # gmina_miejsko_wiejska3 = 0
        # miasto4 = 0
        # obszar_wiejski5 = 0
        # miasto_na_prawach_powiatu = 0
        # delegatura9 = 0
        #
        # for loc in cls.locations:
        #     if loc.county == '':
        #         wojewodztwo += 1
        #     elif loc.county != '' and loc.commune == '':
        #         powiat += 1
        #     elif loc.commune_type == '1':
        #         gmina_miejska1 += 1
        #     elif loc.commune_type == '2':
        #         gmina_wiejska2 += 1
        #     elif loc.commune_type == '3':
        #         gmina_miejsko_wiejska3 += 1
        #     elif loc.commune_type == '4':
        #         miasto4 += 1
        #     elif loc.commune_type == '5':
        #         obszar_wiejski5 += 1
        #     elif loc.commune_type == '9':
        #         delegatura9 += 1
        #     if loc.county != '' and loc.commune == '' and loc.name.istitle():
        #         miasto_na_prawach_powiatu += 1
        #     # print(loc.province, loc.county, loc.commune, loc.commune_type, loc.name, loc.type_name)
        #
        # statistic_list = [[wojewodztwo, 'wojewódźtwo'], [powiat, 'powiaty'], [gmina_miejska1, 'gmina miejska'],
        #                   [gmina_wiejska2,'gmina wiejska'], [gmina_miejsko_wiejska3, 'gmina miejsko-wiejska'],
        #                   [obszar_wiejski5, 'obszar wiejski'], [miasto4, 'miasto'],
        #                   [miasto_na_prawach_powiatu, 'miasto na prawach powiatu'], [delegatura9, 'delegatura']]
        #
        # return statistic_list

    @classmethod
    def count_commune(cls):
        powiat = []
        for loc in cls.locations:
            if loc.county == '01' and loc.commune != '':
                powiat.append(loc.name)
        # print(len(powiat))
        for loc in cls.locations:
            if loc.commune != '':
                print(loc.county, loc.name)

    @classmethod
    def largest_numb_of_communities(cls):
        county = []
        for location in cls.locations:
            county.append(location.county)
        count_commune = {i:county.count(i) for i in county}
        # print(count_commune)
        # print(max(count_commune, key=count_commune.get))
        county_numb = (max(count_commune, key=count_commune.get))
        for loc in cls.locations:
            if loc.county == county_numb and loc.commune == '':
                max_communities_name = loc.name
        return max_communities_name

    @classmethod
    def many_categories(cls):
        loc = []
        for location in cls.locations:
            loc.append(location.name)
        count_loc = {i:loc.count(i) for i in loc}

        loc_names_list = []
        for k, v in count_loc.items():
            # print(k, v)
            if v >= 2:
                # print(k)
                loc_names_list.append(k)
        print(len(loc_names_list))

        return sorted(loc_names_list)

    @classmethod
    def search(cls, search_phrase):
        search_result = []
        for loc in cls.locations:
            if search_phrase in loc.name:
                search_result.append([loc.name, loc.type_name])
        search_result = sorted(search_result, key=lambda x: (x[0].lower(), x[1]))
        return search_result

    # c2.sort(key=lambda row: (row[2], row[1]))

    @classmethod
    def make_list_of_objects(cls):
        table = cls.read_csv()
        for row in table:
            loc_obj = Location(row[0], row[1], row[2], row[3], row[4], row[5])
            cls.add_location(loc_obj)


    @staticmethod
    def read_csv():
        locations_list = []
        with open('malopolska.csv') as csvfile:
            next(csvfile, None)
            readcsv = csv.reader(csvfile, delimiter='\t')

            for row in readcsv:
                locations_list.append(row)

        return locations_list




# read_csv()



