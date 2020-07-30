import Messages as msg  # Messages for the terminal.
import Classes as clss  # The classes used.
import Text as txt      # Messages for the GUI and lists for GUI.
import tkinter as tk    # GUI.


### Add functions FOR TERMINAL. ###
def handle_add_sport(app, db_file):
    msg.display_add_sport_instructions()
    name = input("name: ")
    type = input("type: ")
    cost = input("cost-per-day: ")
    start = input("start-date: ")
    finish = input("finish-date: ")
    period = [start, finish]
    location = input("location: ")
    region = input("region: ")
    country = input("country: ")
    zone = input("zone: ")
    app.add_sport(clss.Sport(name, type, cost, period), location, region, country, zone)
    db_file.write(
        "\nadd sport " + name + " " + type + " " + cost + " " + start + " " + finish + " " + location + " " + region +
        " " + country + " " + zone)


def handle_add_location(app, db_file):
    msg.display_add_location_instructions()
    location = input("location: ")
    region = input("region: ")
    country = input("country: ")
    zone = input("zone: ")
    app.add_location(clss.Location(location), region, country, zone)
    db_file.write("\nadd location " + location + " " + region + " " + country + " " + zone)


def handle_add_region(app, db_file):
    msg.display_add_region_instructions()
    region = input("region: ")
    country = input("country: ")
    zone = input("zone: ")
    app.add_region(clss.Region(region), country, zone)
    db_file.write("\nadd region " + region + " " + country + " " + zone)


def handle_add_country(app, db_file):
    msg.display_add_country_instructions()
    country = input("country: ")
    zone = input("zone: ")
    app.add_country(clss.Country(country), zone)
    db_file.write("\nadd country " + country + " " + zone)


def handle_add_zone(app, db_file):
    msg.display_add_zone_instructions()
    zone = input("zone: ")
    app.add_zone(clss.Zone(zone))
    db_file.write("\nadd zone " + zone)


### Search functions FOR TERMINAL. ###
def handle_search_sport(app):
    msg.display_search_sport_instructions()
    sport = input("name of sport: ")
    ordering = input("do you want to sort the results by price? Type in 'ascending'/'descending'/'none': ")
    app.display_one_sport(sport, ordering)


def handle_search_location(app):
    msg.display_search_location_instructions()
    location = input("name of location: ")
    ordering = input("do you want to sort the results by price? Type in 'ascending'/'descending'/'none': ")
    app.display_sports_from_location(location, ordering)


def handle_search_region(app):
    msg.display_search_region_instructions()
    region = input("name of region: ")
    ordering = input("do you want to sort the results by price? Type in 'ascending'/'descending'/'none': ")
    app.display_sports_from_region(region, ordering)


def handle_search_country(app):
    msg.display_search_country_instructions()
    country = input("name of country")
    ordering = input("do you want to sort the results by price? Type in 'ascending'/'descending'/'none': ")
    app.display_sports_from_country(country, ordering)


def handle_search_zone(app):
    msg.display_search_zone_instructions()
    zone = input("zone: ")
    ordering = input("do you want to sort the results by price? Type in 'ascending'/'descending'/'none': ")
    app.display_sports_from_zone(zone, ordering)


### Search functions FOR GUI. ###
def handle_search_sport_gui(app, args):
    return app.display_one_sport(args[0], args[1])


def handle_search_sports_in_location_gui(app, args):
    return app.display_sports_from_location(args[0], args[1])


def handle_search_sports_in_region_gui(app, args):
    return app.display_sports_from_region(args[0], args[1])


def handle_search_sports_in_country_gui(app, args):
    return app.display_sports_from_country(args[0], args[1])


def handle_search_sports_in_zone_gui(app, args):
    return app.display_sports_from_zone(args[0], args[1])


### DISPLAY FUNCTIONS FOR GUI. ################################
def handle_display_locations_gui(app, args):
    return app.display_locations()


def handle_display_regions_gui(app, args):
    return app.display_regions()


def handle_display_countries_gui(app, args):
    return app.display_countries()


def handle_display_zones_gui(app, args):
    return app.display_zones()


### Add functions FOR GUI. ###
def handle_add_sport_gui(app, db_file, args):
    app.add_sport(clss.Sport(args[0], args[1], args[2], [args[3], args[4]]), args[5], args[6], args[7], args[8])
    db_file.write(
        "\nadd sport " + args[0] + " " + args[1] + " " + args[2] + " " + args[3] + " " + args[4] + " " + args[5] + " " +
        args[6] + " " + args[7] + " " + args[8])


def handle_add_location_gui(app, db_file, args):
    app.add_location(clss.Location(args[0]), args[1], args[2], args[3])
    db_file.write(
        "\nadd location " + args[0] + " " + args[1] + " " + args[2] + " " + args[3])


def handle_add_region_gui(app, db_file, args):
    app.add_region(clss.Region(args[0]), args[1], args[2])
    db_file.write(
        "\nadd region " + args[0] + " " + args[1] + " " + args[2])


def handle_add_country_gui(app, db_file, args):
    app.add_country(clss.Country(args[0]), args[1])
    db_file.write(
        "\nadd country " + args[0] + " " + args[1])


def handle_add_zone_gui(app, db_file, args):
    app.add_zone(clss.Zone(args[0]))
    db_file.write(
        "\add zone " + args[0]
    )


### Pop-ups FOR GUI. ###
def handle_display_user_instructions():
    window = tk.Tk()
    window.title("User Instructions")
    window.geometry('500x200')
    instructions = tk.Label(window, text=txt.user_instructions_detailed, anchor='e', justify=tk.LEFT)
    instructions.grid(column=0, row=0)


def handle_display_admin_instructions():
    window = tk.Tk()
    window.title("User Instructions")
    window.geometry('500x200')
    instructions = tk.Label(window, text=txt.admin_instructions_detailed, anchor='e', justify=tk.LEFT)
    instructions.grid(column=0, row=0)
