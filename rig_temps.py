#!/usr/bin/env python

import requests
from config import *


def get_panel_temperature(panel):
    url = 'http://{}.ethosdistro.com/?json=yes'.format(panel)
    r = requests.get(url)
    data = r.json()

    temps = []

    for rig, rig_data in data['rigs'].iteritems():
        rig_temps_raw = rig_data['temp']
        cards = (len(rig_temps_raw) + 1)/6
        rig_temps = []

        # print rig

        for card in range(cards):
            rig_temps.append(rig_temps_raw[:2])
            # temps.append(this_temp[:2])
            rig_temps_raw = rig_temps_raw[6:]

        rig_temps = map(int, rig_temps)
        rig_temp = reduce(lambda x, y: x + y, rig_temps) / float(len(rig_temps))
        rig_temp = round(rig_temp, 2)

        loc = rig_data['rack_loc']
        if loc == '':
            loc = rig

        print "Rig {}:  {} Cards   --   Temp: {}".format(loc, cards, rig_temp)

        temps.append(rig_temp)

    # temps = map(int, temps)
    panel_temperature = reduce(lambda x, y: x + y, temps) / float(len(temps))
    panel_temperature = round(panel_temperature, 2)

    # print "-"*20
    # print "Temperature of {} : {}".format(panel, panel_temperature)


def main():
    panels = PANELS

    print ""

    for panel in panels:
        # print "Panel: {}".format(panel)
        print "-"*20
        get_panel_temperature(panel)

    print ""
    print ""


if __name__ == '__main__':
    main()
