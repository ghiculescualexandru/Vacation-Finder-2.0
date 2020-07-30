### Texts and lists FOR GUI. ###

user_instructions: str = "  You have the following commands:\n" \
                         "  1.   search sport\n" \
                         "  2.   display locations\n" \
                         "  3.   display regions\n" \
                         "  4.   display countries\n" \
                         "  5.   display zones\n" \
                         "  6.   search sports in location\n" \
                         "  7.   search sports in region\n" \
                         "  8.   search sports in country\n" \
                         "  9.   search sports in zone\n" \
                         "  10. instructions (for details of other commands!)\n" \

user_instructions_detailed: str = "You have the following commands:\n" \
                                  "1.  search sport: find a sport with all its details anywhere\n" \
                                  "2.  display locations: shows all available locations\n" \
                                  "3.  display regions: shows all available regions\n" \
                                  "4.  display countries: shows all available countries\n" \
                                  "5.  display zones: shows all available zones\n" \
                                  "6.  search sports in location: shows all sports from the location, in a specified order\n" \
                                  "7.  search sports in region: shows all sports from the region, in a specified order\n" \
                                  "8.  search sports in country: shows all sports from the country, in a specified order\n" \
                                  "9.  search sports in zone: shows all sports from the zone, in a specified order:\n->('ascending'/'descinding'/'none')\n" \
                                  "10.instructions (for details of other commands!)\n" \

admin_instructions: str = " You have the following commands:\n" \
                          " 1.   add sport\n" \
                          " 2.   display locations\n" \
                          " 3.   display regions\n" \
                          " 4.   display countries\n" \
                          " 5.   display zones\n" \
                          " 6.   add location\n" \
                          " 7.   add region\n" \
                          " 8.   add country\n" \
                          " 9.   add zone\n" \
                          " 10. instructions (for details of other commands!)"

admin_instructions_detailed: str = "You have the following commands:\n" \
                                   "1.  add: fill the fields and add a new sport to the database\n" \
                                   "2.  display locations: shows all available locations\n" \
                                   "3.  display regions: shows all available regions\n" \
                                   "4.  display countries: shows all available countries\n" \
                                   "5.  display zones: shows all available zones\n" \
                                   "6.  add location: fill the fields and add a new location to the database\n" \
                                   "7.  add region: fill the fields and add a new region to the database\n" \
                                   "8.  add sports in country: fill the fields and add a new country to the database\n" \
                                   "9.  add sports in zone: fill the fields and add a new zone to the database\n" \
                                   "10. instructions (for details of other commands!)\n" \

user_instructions_list = ("search sport", "display locations",
                          "display regions", "display countries",
                          "display zones", "search sports in location",
                          "search sports in region", "search sports in country",
                          "search sports in zone", "instructions")

admin_instructions_list = ("add sport", "display locations",
                           "display regions", "display countries",
                           "display zones", "add location",
                           "add region", "add country",
                           "add zone", "instructions")

display_instructions = ("display locations", "display regions", "display countries", "display zones", "instructions")

search_instructions = ("search sport", "search sports in location",
                       "search sports in region", "search sports in country",
                       "search sports in zone")

add_instructions = ("add sport", "add location",
                    "add region", "add country",
                    "add zone")
