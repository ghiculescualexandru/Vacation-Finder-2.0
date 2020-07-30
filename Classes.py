class Sport:
    def __init__(self):
        self.name = str("no name")
        self.type = str("none")
        self.cost_per_day = int(-1)
        self.period = list([])

    def __init__(self, _name, _type, _cost_per_day, _period):
        self.name = str(_name)
        self.type = str(_type)
        self.cost_per_day = int(_cost_per_day)
        self.period = list(_period)

    def cheaper(self, sport):
        if self.cost_per_day < sport.cost_per_day:
            return True
        else:
            return False

    def display(self):
        if len(self.period) == 0:
            print("Sport has no details about timeline or cost.")
            return "Sport has no details about timeline or cost."
        else:
            print(self.type.capitalize() + " sport " + self.name.capitalize() + " with cost per day: " + \
                  str(self.cost_per_day) + ", period: " + self.period[0] + "-" + self.period[1])
            return self.type.capitalize() + " sport " + self.name.capitalize() + " with cost per day: " + \
                   str(self.cost_per_day) + ", period: " + self.period[0] + "-" + self.period[1]


class Location:
    def __init__(self):
        self.name = "no name"
        self.sports_list = []
        self.sports_num = 0

    def __init__(self, _name):
        self.name = _name
        self.sports_list = []
        self.sports_num = 0

    def add_sport(self, sport):
        self.sports_list.append(sport)
        self.sports_num += 1

    def display_sports(self):
        i = int(1)
        for sport in self.sports_list:
            print("-------- " + str(i), end='. ')
            sport.display()
            i += 1

    def display(self):
        print("Location " + self.name.capitalize() + " with " + str(self.sports_num) + " sports. " + "It has the "
                                                                                                     "following "
                                                                                                     "sports: ")
        self.display_sports()


class Region:
    def __init__(self):
        self.name = "no name"
        self.locations_list = []
        self.locations_num = 0

    def __init__(self, _name):
        self.name = _name
        self.locations_list = []
        self.locations_num = 0

    def add_location(self, location):
        for l in self.locations_list:
            if l.name == location.name:
                return
        self.locations_list.append(location)
        self.locations_num += 1

    def add_sport(self, sport, _location):
        found = False
        for location in self.locations_list:
            if location.name == _location:
                found = True
                location.add_sport(sport)

        if not found:
            tmp = Location(_location)
            tmp.add_sport(sport)
            self.add_location(tmp)

    def display_locations(self):
        i = int(1)
        for location in self.locations_list:
            print("------ " + str(i), end='. ')
            location.display()
            i += 1

    def display(self):
        print("Region \"" + self.name + "\" with " + str(self.locations_num) + " locations: ")
        self.display_locations()


class Country:
    def __init__(self):
        self.name = "no name"
        self.regions_list = []
        self.regions_num = 0

    def __init__(self, _name):
        self.name = _name
        self.regions_list = []
        self.regions_num = 0

    def add_region(self, region):
        for r in self.regions_list:
            if r.name == region.name:
                return
        self.regions_list.append(region)
        self.regions_num += 1

    def add_location(self, location, _region):
        found = False
        for region in self.regions_list:
            if region.name == _region:
                found = True
                region.add_location(location)

        if not found:
            tmp = Region(_region)
            tmp.add_location(location)
            self.add_region(tmp)

    def add_sport(self, sport, _location, _region):
        found_region = False
        found_location = False

        for region in self.regions_list:
            if region.name == _region:
                found_region = True
                for location in region.locations_list:
                    if location.name == _location:
                        found_location = True
                        location.add_sport(sport)

        if not found_region:
            self.add_region(Region(_region))
            self.add_sport(sport, _location, _region)
        elif not found_location:
            self.add_location(Location(_location), _region)
            self.add_sport(sport, _location, _region)

    def display_regions(self):
        i = int(1)
        for region in self.regions_list:
            print("---- " + str(i), end='. ')
            region.display()
            i += 1

    def display(self):
        print("Country \"" + self.name + "\" with " + str(self.regions_num) + " regions: ")
        self.display_regions()


class Zone:
    def __init__(self):
        self.name = "no name"
        self.countries_list = []
        self.countries_num = 0

    def __init__(self, _name):
        self.name = _name
        self.countries_list = []
        self.countries_num = 0

    def add_country(self, country):
        for c in self.countries_list:
            if c.name == country.name:
                return
        self.countries_list.append(country)
        self.countries_num += 1

    def add_region(self, region, _country):
        found = False
        for country in self.countries_list:
            if country.name == _country:
                found = True
                country.add_region(region)

        if not found:
            tmp = Country(_country)
            tmp.add_region(region)
            self.add_country(tmp)

    def add_location(self, location, _region, _country):
        found_country = False
        found_region = False
        for country in self.countries_list:
            if country.name == _country:
                found_country = True
                for region in country.regions_list:
                    if region.name == _region:
                        found_region = True
                        region.add_location(location)

        if not found_country:
            self.add_country(Country(_country))
            self.add_location(location, _region, _country)
        elif not found_region:
            self.add_region(Region(_region, _country))
            self.add_sport(location, _region, _country)

    def add_sport(self, sport, _location, _region, _country):
        found_country = False
        found_region = False
        found_location = False
        for country in self.countries_list:
            if country.name == _country:
                found_country = True
                for region in country.regions_list:
                    if region.name == _region:
                        found_region = True
                        for location in region.locations_list:
                            if location.name == _location:
                                found_location = True
                                location.add_sport(sport)

        if not found_country:
            self.add_country(Country(_country))
            self.add_sport(sport, _location, _region, _country)
        elif not found_region:
            self.add_region(Region(_region), _country)
            self.add_sport(sport, _location, _region, _country)
        elif not found_location:
            self.add_location(Location(_location), _region, _country)
            self.add_sport(sport, _location, _region, _country)

    def display_countries(self):
        i = int(1)
        for country in self.countries_list:
            print("-- " + str(i), end='. ')
            country.display()
            i += 1

    def display(self):
        print("Zone \"" + self.name + "\" has " + str(self.countries_num) + " countries." + \
              "It has the following countries: ")
        self.display_countries()
