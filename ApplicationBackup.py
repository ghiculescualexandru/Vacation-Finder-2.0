import Classes as clss  # The classes used.

# This code.py is used when the administrator wants to
# add a new sport/location/region/country/zone. Because
# a hierarchy is used, in order to add a sport you must
# know its location, region, country and zone. If one of
# those is unknown, then it is automatically added using
# the functions below.

found_zone = found_country = found_region = found_location = False
backup_zone = clss.Zone("")
backup_country = clss.Country("")
backup_region = clss.Region("")
backup_location = clss.Location("")


def reset_backup():
    global found_zone
    global found_country
    global found_region
    global found_location
    found_zone = found_country = found_region = found_location = False

    global backup_zone
    global backup_country
    global backup_region
    global backup_location
    backup_zone = clss.Zone("")
    backup_country = clss.Country("")
    backup_region = clss.Region("")
    backup_location = clss.Location("")


def add_sport_no_backup(app, _zone, _country, _region, _location, sport):
    tmp_zone = clss.Zone(_zone)
    tmp_country = clss.Country(_country)
    tmp_region = clss.Region(_region)
    tmp_location = clss.Location(_location)

    tmp_location.add_sport(sport)
    tmp_region.add_location(tmp_location)
    tmp_country.add_region(tmp_region)
    tmp_zone.add_country(tmp_country)
    app.zones_list.append(tmp_zone)
    app.zones_num += 1


def add_sport_zone_backup(backup_zone, _country, _region, _location, sport):
    tmp_country = clss.Country(_country)
    tmp_region = clss.Region(_region)
    tmp_location = clss.Location(_location)

    tmp_location.add_sport(sport)
    tmp_region.add_location(tmp_location)
    tmp_country.add_region(tmp_region)

    backup_zone.add_country(tmp_country)


def add_sport_country_backup(backup_country, _region, _location, sport):
    tmp_region = clss.Region(_region)
    tmp_location = clss.Location(_location)

    tmp_location.add_sport(sport)
    tmp_region.add_location(tmp_location)

    backup_country.add_region(tmp_region)


def add_sport_region_backup(backup_region, _location, sport):
    tmp_location = clss.Location(_location)
    tmp_location.add_sport(sport)

    backup_region.add_location(tmp_location)


def add_location_no_backup(app, _zone, _country, _region, location):
    tmp_zone = clss.Zone(_zone)
    tmp_country = clss.Country(_country)
    tmp_region = clss.Region(_region)

    tmp_region.add_location(location)
    tmp_country.add_region(tmp_region)
    tmp_zone.add_country(tmp_country)
    app.zones_list.append(tmp_zone)
    app.zones_num += 1


def add_location_zone_backup(backup_zone, _country, _region, location):
    tmp_country = clss.Country(_country)
    tmp_region = clss.Region(_region)

    tmp_region.add_location(location)
    tmp_country.add_region(tmp_region)

    backup_zone.add_country(tmp_country)


def add_location_country_backup(backup_country, _region, location):
    tmp_region = clss.Region(_region)
    tmp_region.add_location(location)

    backup_country.add_region(tmp_region)


def add_region_no_backup(app, _zone, _country, region):
    tmp_zone = clss.Zone(_zone)
    tmp_country = clss.Country(_country)

    tmp_country.add_region(region)
    tmp_zone.add_country(tmp_country)

    app.zones_list.append(tmp_zone)
    app.zones_num += 1


def add_region_zone_backup(backup_zone, _country, region):
    tmp_country = clss.Country(_country)
    tmp_country.add_region(region)

    backup_zone.add_country(tmp_country)
