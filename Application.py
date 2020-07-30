import Classes as clss              # The classes used.
import ApplicationBackup as bckp    # Functions for adding sport/location/region/countries/zone
                                    # when some of the above do not exist yet.


class Application:
    # Singletone instance for the application.
    instance = None

    @staticmethod
    def get_instance():
        if Application.instance == None:
            Application()
        else:
            return Application.instance

    def __init__(self):
        if Application.instance != None:
            raise Exception("Singletone.")
        else:
            self.zones_list = []    # The application has a list of zones
            self.zones_num = 0      # and the number of zones.
            Application.instance = self

    ### Add methods. ###
    def add_zone(self, zone):
        # Add new zone.
        for z in self.zones_list:
            if z.name == zone.name:
                return
        self.zones_list.append(zone)
        self.zones_num += 1

    def add_country(self, country, _zone):
        # Add new country.
        found = False
        for zone in self.zones_list:
            if zone.name == _zone:
                found = True
                zone.add_country(country)

        if not found:
            tmp_zone = clss.Zone(_zone)
            tmp_zone.add_country(country)
            self.add_zone(tmp_zone)

    def add_region(self, region, _country, _zone):
        # Add new region.
        bckp.reset_backup()
        for zone in self.zones_list:
            if zone.name == _zone:
                bckp.found_zone = True
                bckp.backup_zone = zone
                for country in zone.countries_list:
                    if country.name == _country:
                        bckp.found_country = True
                        country.add_region(region)

        if not bckp.found_zone:
            bckp.add_region_no_backup(self, _zone, _country, region)
        elif not bckp.found_country:
            bckp.add_region_zone_backup(bckp.backup_zone, _country, region)

    def add_location(self, location, _region, _country, _zone):
        # Add new location.
        bckp.reset_backup()
        for zone in self.zones_list:
            if zone.name == _zone:
                bckp.found_zone = True
                bckp.backup_zone = zone
                for country in zone.countries_list:
                    if country.name == _country:
                        bckp.found_country = True
                        bckp.backup_country = country
                        for region in country.regions_list:
                            if region.name == _region:
                                bckp.found_region = True
                                region.add_location(location)

        if not bckp.found_zone:
            bckp.add_location_no_backup(self, _zone, _country, _region, location)
        elif not bckp.found_country:
            bckp.add_location_zone_backup(bckp.backup_zone, _country, _region, location)
        elif not bckp.found_region:
            bckp.add_location_country_backup(bckp.backup_country, _region, location)

    def add_sport(self, sport, _location, _region, _country, _zone):
        # Add new sport.
        bckp.reset_backup()
        for zone in self.zones_list:
            if zone.name == _zone:
                bckp.found_zone = True
                bckp.backup_zone = zone
                for country in zone.countries_list:
                    if country.name == _country:
                        bckp.found_country = True
                        bckp.backup_country = country
                        for region in country.regions_list:
                            if region.name == _region:
                                bckp.found_region = True
                                bckp.backup_region = region
                                for location in region.locations_list:
                                    if location.name == _location:
                                        bckp.found_location = True
                                        location.add_sport(sport)
                                        return

        if not bckp.found_zone:
            bckp.add_sport_no_backup(self, _zone, _country, _region, _location, sport)
        elif not bckp.found_country:
            bckp.add_sport_zone_backup(bckp.backup_zone, _country, _region, _location, sport)
        elif not bckp.found_region:
            bckp.add_sport_country_backup(bckp.backup_country, _region, _location, sport)
        elif not bckp.found_location:
            bckp.add_sport_region_backup(bckp.backup_region, _location, sport)

    ### Display basic methods. ###
    def display_zones(self):
        # Shows every zone with its details.
        i = int(1)
        for zone in self.zones_list:
            print(str(i), end='. ')
            zone.display()
            i += 1

    def display(self):
        self.display_zones()

    ### Search methods. ###
    ### Search for sport.
    def get_one_sport(self, _sport):
        # Returns a list with all details about a sport.
        sports = []
        for zone in self.zones_list:
            for country in zone.countries_list:
                for region in country.regions_list:
                    for location in region.locations_list:
                        for sport in location.sports_list:
                            if sport.name == _sport:
                                sport_details = {
                                    "zone": zone.name,
                                    "country": country.name,
                                    "region": region.name,
                                    "location": location.name
                                }
                                sports.append((sport, sport_details))

        return sports

    def get_one_sport_ordered(self, _sport, _ordering):
        # Returns an ordered or unordered list with a sport.
        sports = self.get_one_sport(_sport)
        if (_ordering == "ascending"):
            return sorted(sports, key=lambda x: x[0].cost_per_day)
        elif (_ordering == "descending"):
            return sorted(sports, key=lambda x: x[0].cost_per_day, reverse=True)

    def display_one_sport(self, _sport, _ordering):
        # Returns a string with all details about a sport.
        res = ""
        if (_ordering == "ascending"):
            sports = self.get_one_sport_ordered(_sport, _ordering)
        elif (_ordering == "descending"):
            sports = self.get_one_sport_ordered(_sport, _ordering)
        else:
            sports = self.get_one_sport(_sport)

        i = int(1)
        for sport in sports:
            print(str(i), end='. ')
            res += str(i) + ". "
            res += sport[0].display() + "\n"
            for detail in sport[1].items():
                print(detail[0] + ": " + detail[1])
                res += detail[0] + ": " + detail[1] + "\n"
            i += 1

        return res

    ### Search for location.
    def get_sports_from_location(self, _location):
        # Returns a list with all details about a location.
        sports = []
        for zone in self.zones_list:
            for country in zone.countries_list:
                for region in country.regions_list:
                    for location in region.locations_list:
                        if location.name == _location:
                            for sport in location.sports_list:
                                sports.append(sport)
        return sports

    def get_sports_from_location_ordered(self, _location, _ordering):
        # Returns an ordered or unordered list with a location.
        sports = self.get_sports_from_location(_location)
        if _ordering == "ascending":
            return sorted(sports, key=lambda x: x.cost_per_day)
        elif _ordering == "descending":
            return sorted(sports, key=lambda x: x.cost_per_day, reverse=True)

    def display_sports_from_location(self, _location, _ordering):
        # Returns a string with all details about a location.
        res = " "
        if _ordering == "ascending":
            sports = self.get_sports_from_location_ordered(_location, _ordering)
        elif _ordering == "descending":
            sports = self.get_sports_from_location_ordered(_location, _ordering)
        else:
            sports = self.get_sports_from_location(_location)

        i = int(1)
        for sport in sports:
            res += str(i) + '. '
            print(str(i), end='. ')
            res += sport.display() + '\n'
            i += 1

        print("res in application.py " + res)
        return res

    ### Search for region.
    def get_sports_from_region(self, _region):
        # Returns a list with all details about a region.
        sports = []
        for zone in self.zones_list:
            for country in zone.countries_list:
                for region in country.regions_list:
                    if region.name == _region:
                        for location in region.locations_list:
                            for sport in location.sports_list:
                                sports.append((sport, location.name))

        return sports

    def get_sports_from_region_ordered(self, _region, _ordering):
        # Returns an ordered or unordered list with a region.
        sports = self.get_sports_from_region(_region)
        if _ordering == "ascending":
            return sorted(sports, key=lambda x: x[0].cost_per_day)
        elif _ordering == "descending":
            return sorted(sports, key=lambda x: x[0].cost_per_day, reverse=True)

    def display_sports_from_region(self, _region, _ordering):
        # Returns a string with all details about a region.
        res = ""
        if _ordering == "ascending":
            sports = self.get_sports_from_region_ordered(_region, _ordering)
        elif _ordering == "descending":
            sports = self.get_sports_from_region_ordered(_region, _ordering)
        else:
            sports = self.get_sports_from_region(_region)

        i = int(1)
        for sport in sports:
            res += str(i) + '. '
            print(str(i), end='. ')
            res += sport[0].display() + '\n'
            res += sport[1] + '\n'
            print(sport[1])
            i += 1

        return res

    ### Search for country.
    def get_sports_from_country(self, _country):
        # Returns a list with all details about a country.
        sports = []
        for zone in self.zones_list:
            for country in zone.countries_list:
                if country.name == _country:
                    for region in country.regions_list:
                        for location in region.locations_list:
                            for sport in location.sports_list:
                                sport_details = {
                                    "region": region.name,
                                    "location": location.name,
                                }

                                sports.append((sport, sport_details))

        return sports

    def get_sports_from_country_ordered(self, _country, _ordering):
        # Returns an ordered or unordered list with a country.
        sports = self.get_sports_from_country(_country)
        if _ordering == "ascending":
            return sorted(sports, key=lambda x: x[0].cost_per_day)
        elif _ordering == "descending":
            return sorted(sports, key=lambda x: x[0].cost_per_day, reverse=True)

    def display_sports_from_country(self, _country, _ordering):
        # Returns a string with all details about a country.
        res = ""
        if _ordering == "ascending":
            sports = self.get_sports_from_country_ordered(_country, _ordering)
        elif _ordering == "descending":
            sports = self.get_sports_from_country_ordered(_country, _ordering)
        else:
            sports = self.get_sports_from_country(_country)

        i = int(1)
        for sport in sports:
            res += str(i) + '. '
            print(str(i), end='.')
            res += sport[0].display() + '\n'
            for details in sport[1].items():
                res += details[0] + " " + details[1] + '\n'
                print(details[0] + " " + details[1])
            i += 1

        return res

    ### Search for zone.
    def get_sports_from_zone(self, _zone):
        # Returns a list with all details about a zone.
        sports = []
        for zone in self.zones_list:
            if zone.name == _zone:
                for country in zone.countries_list:
                    for region in country.regions_list:
                        for location in region.locations_list:
                            for sport in location.sports_list:
                                sport_details = {
                                    "country": country,
                                    "region": region,
                                    "location": location
                                }

                                sports.append((sport, sport_details))

        return sports

    def get_sports_from_zone_ordered(self, _zone, _ordering):
        # Returns an ordered or unordered list with a zone.
        sports = self.get_sports_from_zone(_zone)
        if _ordering == "ascending":
            return sorted(sports, key=lambda x: x[0].cost_per_day)
        elif _ordering == "descending":
            return sorted(sports, key=lambda x: x[0].cost_per_day, reverse=True)

    def display_sports_from_zone(self, _zone, _ordering):
        # Returns a string with all details about a zone.
        res = ""
        if _ordering == "ascending":
            sports = self.get_sports_from_zone_ordered(_zone, _ordering)
        elif _ordering == "descending":
            sports = self.get_sports_from_zone_ordered(_zone, _ordering)
        else:
            sports = self.get_sports_from_zone(_zone)

        i = int(1)
        for sport in sports:
            res += str(i) + '. '
            print(str(i), end='. ')
            res += sport[0].display() + '\n'
            for detail in sport[1].items():
                res += detail[0] + ": " + detail[1] + '\n'
                print(detail[0] + ": " + detail[1])
            i += 1

        return res

    ###  DISPLAY LOCATIONS/REGIONS/COUNTRIES/ZONES.
    def get_all_locations(self):
        locations = []
        for zone in self.zones_list:
            for country in zone.countries_list:
                for region in country.regions_list:
                    for location in region.locations_list:
                        locations.append(location.name)

        return locations

    def display_locations(self):
        locations = self.get_all_locations()
        locations = list(dict.fromkeys(locations))
        res = ""
        i = int(1)
        for location in locations:
            res += str(i) + '. '
            res += location + '\n'
            i += 1
        return res

    def get_all_regions(self):
        regions = []
        for zone in self.zones_list:
            for country in zone.countries_list:
                for region in country.regions_list:
                    regions.append(region.name)

        return regions

    def display_regions(self):
        regions = self.get_all_regions()
        regions = list(dict.fromkeys(regions))
        res = ""
        i = int(1)
        for region in regions:
            res += str(i) + '. '
            res += region + "\n"
            i += 1
        return res

    def get_all_countries(self):
        countries = []
        for zone in self.zones_list:
            for country in zone.countries_list:
                countries.append(country.name)

        return countries

    def display_countries(self):
        countries = self.get_all_countries()
        countries = list(dict.fromkeys(countries))
        res = ""
        i = int(1)
        for country in countries:
            res += str(i) + '. '
            res += country + "\n"
            i += 1
        return res

    def display_zones(self):
        res = ""
        i = int(1)
        for zone in self.zones_list:
            res += str(i) + '. '
            res += zone.name + '\n'
            i += 1
        return res
