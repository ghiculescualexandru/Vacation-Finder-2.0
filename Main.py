import Classes as clss              # The classes used.
import Application as applc         # Functions for main operations.
import Messages as msg              # Messages for the terminal.
import Handler as hdlr              # Functions to handle main operations.
import tkinter as tk                # GUI.
import tkinter.ttk as tkttk         # ^
from tkinter import scrolledtext    # ^
import Text as txt                  # Messages for the GUI and lists for GUI.


def init_app():
    # Returns the singletone instance from the Application class.
    return applc.Application()


def init_db_file():
    # Returns the opened text file for the "database".
    return open("database.txt", "r")


def init_db():
    # Returns the modified application after adding
    # the commands read from the text file.
    db_file = init_db_file()
    app = init_app()

    for line in db_file:
        make_command_from_db(app, line.split(" "))

    return app


def make_command_from_db(app, line):
    # Makes the command from "line" into the application "app".
    if line[0] == "add":
        if line[1] == "zone":
            app.add_zone(clss.Zone(line[2]))
        elif line[1] == "sport":
            app.add_sport(clss.Sport(line[2], line[3], line[4], [line[5], line[6]]), line[7], line[8], line[9],
                          line[10])
        elif line[1] == "country":
            app.add_country(clss.Country(line[2]), line[3])
        elif line[1] == "region":
            app.add_region(clss.Region(line[2]), line[3], line[4])
        elif line[1] == "location":
            app.add_location(clss.Location(line[2]), line[3], line[4], line[5])


def handle_admin(app):
    # FOR TERMINAL. Handles basic admin input
    # calling for other functions to complete the input
    # and make commands.
    msg.display_admin_instructions()
    while True:
        db_file = open("database.txt", "a")
        action = input("Type the action: ")
        if action == "add sport":
            hdlr.handle_add_sport(app, db_file)
        elif action == "add location":
            hdlr.handle_add_location(app, db_file)
        elif action == "add region":
            hdlr.handle_add_region(app, db_file)
        elif action == "add country":
            hdlr.handle_add_country(app, db_file)
        elif action == "add zone":
            hdlr.handle_add_zone(app, db_file)
        elif action == "display database":
            app.display()
        elif action == "save database":
            db_file.close
        elif action == "instructions":
            msg.display_admin_instructions()
        elif action == "quit":
            msg.display_instructions()
            db_file.close()
            return


def handle_user(app):
    # FOR TERMINAL. Handles basic user input
    # calling for other functions to complete the input
    # and make commands.
    msg.display_user_instructions()
    while True:
        action = input("Type the action: ")
        if action == "search sport":
            hdlr.handle_search_sport(app)
        elif action == "search location":
            hdlr.handle_search_location(app)
        elif action == "search region":
            hdlr.handle_search_region(app)
        elif action == "search country":
            hdlr.handle_search_country(app)
        elif action == "search zone":
            hdlr.handle_search_zone(app)
        elif action == "display database":
            app.display()
        elif action == "instructions":
            msg.display_admin_instructions()
        elif action == "quit":
            msg.display_instructions()
            return


def handle_user_gui(app, action, args):
    # FOR GUI. Handles basic user input
    # calling for other functions to complete the input
    # and make commands.
    msg.display_user_instructions()
    if action == "search sport":
        return hdlr.handle_search_sport_gui(app, args)
    elif action == "search sports in location":
        return hdlr.handle_search_sports_in_location_gui(app, args)
    elif action == "search sports in region":
        return hdlr.handle_search_sports_in_region_gui(app, args)
    elif action == "search sports in country":
        return hdlr.handle_search_sports_in_country_gui(app, args)
    elif action == "search sports in zone":
        return hdlr.handle_search_sports_in_zone_gui(app, args)
    elif action == "display locations":
        return hdlr.handle_display_locations_gui(app, args)
    elif action == "display regions":
        return hdlr.handle_display_regions_gui(app, args)
    elif action == "display countries":
        return hdlr.handle_display_countries_gui(app, args)
    elif action == "display zones":
        return hdlr.handle_display_zones_gui(app, args)
    elif action == "instructions":
        return hdlr.handle_display_user_instructions()
    elif action == "quit":
        return


def handle_admin_gui(app, action, args):
    # FOR GUI. Handles basic admin input
    # calling for other functions to complete the input
    # and make commands.
    db_file = open("database.txt", "a")
    if action == "add sport":
        return hdlr.handle_add_sport_gui(app, db_file, args)
    elif action == "add location":
        return hdlr.handle_add_location_gui(app, db_file, args)
    elif action == "add region":
        return hdlr.handle_add_region_gui(app, db_file, args)
    elif action == "add country":
        return hdlr.handle_add_country_gui(app, db_file, args)
    elif action == "add zone":
        return hdlr.handle_add_zone_gui(app, db_file, args)
    elif action == "display locations":
        return hdlr.handle_display_locations_gui(app, args)
    elif action == "display regions":
        return hdlr.handle_display_regions_gui(app, args)
    elif action == "display countries":
        return hdlr.handle_display_countries_gui(app, args)
    elif action == "display zones":
        return hdlr.handle_display_zones_gui(app, args)
    elif action == "instructions":
        return hdlr.handle_display_admin_instructions()
    elif action == "quit":
        return


def main():
    # Main function FOR TERMINAL. It is commented
    # below in order to use the GUI.
    app = init_db()
    msg.display_welcome()
    msg.display_instructions()

    while True:
        input_str = input("Type here: ")
        if input_str == "admin":
            handle_admin(app, "")
        elif input_str == "user":
            handle_user(app, "")
        elif input_str == "quit":
            break


def init_frame():
    # Returns the initial frame where
    # you choose admin or user.
    window = tk.Tk()
    window.title("Vacation Finder 1.0")
    window.geometry('300x150')
    return window


def gui():
    # Main function FOR GUI. It handles
    # everything regarding user interface, using
    # texts from Text.py and functions from Handler.py

    # Welcome message for the initial frame where you choose between user and admin.
    welcome_msg = tk.Label(window, text="Welcome!", font=("Arial Bold", 20))
    welcome_msg.grid(column=0, row=0)
    # Basic instructions for the initial frame.
    instructions = tk.Label(window, text="You must choose between\n->>> user and admin.", anchor='e', justify=tk.CENTER,
                            font=("Arial", 10))
    instructions.grid(column=0, row=1)

    def exit_btn_clicked():
        # When the exit button is pressed,
        # the program exits successfully.
        exit(0)

    def back_to_menu_clicked():
        # When the back-to-menu button is pressed,
        # it resets to the initial frame with user and admin.
        for widget in window.winfo_children():
            widget.destroy()
        window.geometry('300x150')
        gui()

    def user_btn_clicked():
        # New frame when user is chosen.
        window.geometry('950x500')
        user_btn.destroy()
        admin_btn.destroy()
        # New welcome message for the user and instructions.
        welcome_msg.configure(text="You are now an user!", fg="#61bf5c")
        instructions.configure(text=txt.user_instructions, anchor='e', justify=tk.LEFT,
                               font=("Arial", 12))
        # Combobox to choose the action to be done.
        dropdown = tkttk.Combobox(window)
        dropdown['values'] = txt.user_instructions_list
        # Lists for the action types.
        displays = txt.display_instructions
        search_sports = txt.search_instructions

        dropdown.grid(column=0, row=2)

        def handle_user_command(eventObject):
            # Function when using the combobox.
            command = dropdown.get()
            args = []
            # If the command is for display.
            if command in displays:
                res = handle_user_gui(app, command, [])
                if res == None:
                    print("'res' is None.")
                else:
                    output = scrolledtext.ScrolledText(window, width=40, height=9, font=(8))
                    output.insert(tk.INSERT, res)
                    output.grid(column=3, row=1)
            # If the command is for searching sport or location/region/country/zone.
            elif command in search_sports:
                name = tk.Entry(window, width=10)
                name.insert(0, "name")
                ordering = tk.Entry(window, width=10)
                ordering.insert(0, "ordering")

                def search_command_clicked():
                    args.append(name.get())
                    args.append(ordering.get())
                    res = handle_user_gui(app, command, args)
                    output = scrolledtext.ScrolledText(window, width=40, height=9, font=(8))
                    output.insert(tk.INSERT, res)
                    output.grid(column=3, row=1)

                search_btn = tk.Button(window, text="search", command=search_command_clicked)
                search_btn.grid(column=1, row=2)

                name.grid(column=1, row=3)
                ordering.grid(column=1, row=4)

        dropdown.bind("<<ComboboxSelected>>", handle_user_command)

    def admin_btn_clicked():
        # New frame when admin is chosen.
        window.geometry('950x500')
        user_btn.destroy()
        admin_btn.destroy()
        # New welcome message for the admin and instructions.
        welcome_msg.configure(text="You are now admin!", fg="#d17b7b")
        instructions.configure(text=txt.admin_instructions, anchor='e', justify=tk.LEFT,
                               font=("Arial", 12))
        # Combobox to choose the action to be done.
        dropdown = tkttk.Combobox(window)
        dropdown['values'] = txt.admin_instructions_list
        output = scrolledtext.ScrolledText()
        # Lists for the action types.
        displays = txt.display_instructions
        add_commands = txt.add_instructions

        dropdown.grid(column=0, row=2)

        def handle_admin_command(eventObject):
            # Function when using the combobox.
            command = dropdown.get()
            to_add = None
            args = []
            my_widgets = []
            # If the command is for display.
            if command in displays:
                res = handle_admin_gui(app, command, [])
                if res is None:
                    print("'res' is None.")
                else:
                    global output
                    output = scrolledtext.ScrolledText(window, width=40, height=8, font=(8))
                    output.insert(tk.INSERT, res)
                    output.grid(column=3, row=1)
            # If the command is for adding a sport or location/region/country/zone.
            elif command in add_commands:
                to_add = command.split(" ")[1]
                for widget in window.winfo_children():
                    if isinstance(widget, tk.Entry) and widget != dropdown:
                        widget.destroy()
                if to_add == "sport":
                    sport = tk.Entry(window, width=12)
                    sport.insert(0, "sport-name")
                    sport.config(fg="black")

                    type = tk.Entry(window, width=12)
                    type.insert(0, "sport-type")
                    type.config(fg="black")

                    cost = tk.Entry(window, width=12)
                    cost.insert(0, "cost-per-day")
                    cost.config(fg="black")

                    start = tk.Entry(window, width=12)
                    start.insert(0, "start-date")
                    start.config(fg="black")

                    finish = tk.Entry(window, width=12)
                    finish.insert(0, "finish-date")
                    finish.config(fg="black")

                    location = tk.Entry(window, width=12)
                    location.insert(0, "location")
                    location.config(fg="black")

                    region = tk.Entry(window, width=12)
                    region.insert(0, "region")
                    region.config(fg="black")

                    country = tk.Entry(window, width=12)
                    country.insert(0, "country")
                    country.config(fg="black")

                    zone = tk.Entry(window, width=12)
                    zone.insert(0, "zone")
                    zone.config(fg="black")

                    sport.grid(row=3, column=1)
                    type.grid(row=4, column=1)
                    cost.grid(row=5, column=1)
                    start.grid(row=6, column=1)
                    finish.grid(row=7, column=1)
                    location.grid(row=8, column=1)
                    region.grid(row=9, column=1)
                    country.grid(row=10, column=1)
                    zone.grid(row=11, column=1)
                elif to_add == "location":
                    location = tk.Entry(window, width=12)
                    location.insert(0, "location")
                    location.config(fg="black")

                    region = tk.Entry(window, width=12)
                    region.insert(0, "region")
                    region.config(fg="black")

                    country = tk.Entry(window, width=12)
                    country.insert(0, "country")
                    country.config(fg="black")

                    zone = tk.Entry(window, width=12)
                    zone.insert(0, "zone")
                    zone.config(fg="black")

                    location.grid(row=3, column=1)
                    region.grid(row=4, column=1)
                    country.grid(row=5, column=1)
                    zone.grid(row=6, column=1)
                elif to_add == "region":
                    region = tk.Entry(window, width=12)
                    region.insert(0, "region")
                    region.config(fg="black")

                    country = tk.Entry(window, width=12)
                    country.insert(0, "country")
                    country.config(fg="black")

                    zone = tk.Entry(window, width=12)
                    zone.insert(0, "zone")
                    zone.config(fg="black")

                    region.grid(row=3, column=1)
                    country.grid(row=4, column=1)
                    zone.grid(row=5, column=1)
                elif to_add == "country":
                    country = tk.Entry(window, width=12)
                    country.insert(0, "country")

                    zone = tk.Entry(window, width=12)
                    zone.insert(0, "zone")

                    country.grid(row=3, column=1)
                    zone.grid(row=4, column=1)
                elif to_add == "zone":
                    zone = tk.Entry(window, width=12)
                    zone.insert(0, "zone")

                    zone.grid(row=3, column=1)

                def add_command_clicked():
                    if to_add == "sport":
                        args.append((sport.get(), sport))
                        args.append((type.get(), type))
                        args.append((cost.get(), cost))
                        args.append((start.get(), start))
                        args.append((finish.get(), finish))
                        args.append((location.get(), location))
                        args.append((region.get(), region))
                        args.append((country.get(), country))
                        args.append((zone.get(), zone))
                    elif to_add == "location":
                        args.append((location.get(), location))
                        args.append((region.get(), region))
                        args.append((country.get(), country))
                        args.append((zone.get(), zone))
                    elif to_add == "region":
                        args.append((region.get(), region))
                        args.append((country.get(), country))
                        args.append((zone.get(), zone))
                    elif to_add == "country":
                        args.append((country.get(), country))
                        args.append((zone.get(), zone))
                    elif to_add == "zone":
                        args.append((zone.get(), zone))

                    real_args = []
                    for a in args:
                        real_args.append(a[0])
                        my_widgets.append(a[1])
                    for widg in my_widgets:
                        widg.destroy()
                    add_btn.config(state=tk.DISABLED)
                    handle_admin_gui(app, command, real_args)

                add_btn = tk.Button(window, text="add", command=add_command_clicked)
                add_btn.grid(column=1, row=2)

        dropdown.bind("<<ComboboxSelected>>", handle_admin_command)

    user_btn = tk.Button(window, text="user", command=user_btn_clicked, width=7, bg="#b7ffb3")
    admin_btn = tk.Button(window, text="admin", command=admin_btn_clicked, width=7, bg="#f79292")
    user_btn.grid(column=0, row=2)
    admin_btn.grid(column=0, row=3)

    back_to_menu = tk.Button(window, text="Back to menu", command=back_to_menu_clicked, bg="#ccf1ff")
    back_to_menu.grid(column=1, row=0)

    exit_btn = tk.Button(window, text="Exit", command=exit_btn_clicked, bg="#ccf1ff")
    exit_btn.grid(column=2, row=0)

    window.mainloop()


# main()
window = init_frame()
app = init_db()
gui()
