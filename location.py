class Location:
    def __init__(self, province, county, commune, commune_type, name, type_name):
        self.province = province
        self.county = county
        self.commune = commune
        self.commune_type = commune_type
        self.name = name
        self.type_name = type_name

    def get_name(self):
        return '{}'.format(self.name)

    def get_commune_name(self):
        return '{}'.format(self.type_name)
