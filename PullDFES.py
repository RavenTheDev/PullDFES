# Simple app that will pull the information from the DFES website via RSS feed, and format it for easy reading.
# Currently setup for North Metro, but can be changed extremely easily by simply changing the URL@@

import feedparser
import numpy as np
import os, sys

ALL_INCIDENT = feedparser.parse("https://www.emergency.wa.gov.au/data/incident_FCAD_regions_METRONORTHCOASTAL.rss")

all_updates = []
for i in range(len(ALL_INCIDENT.entries)):
    all_updates.append({"URL": ALL_INCIDENT.entries[i].link,"Title": ALL_INCIDENT.entries[i].title, "Time": ALL_INCIDENT.entries[i].published})

class bcolors:
    ''' This sets up the formatting of text colors '''

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def breaker(ascii):
    print(bcolors.HEADER + (str(ascii) * 50) + bcolors.ENDC)

def starter():
    print(bcolors.HEADER + "|" + bcolors.ENDC)

def main():

    print (bcolors.HEADER + "====== " + (ALL_INCIDENT['feed']['title'])," ======" + bcolors.ENDC)
    print ("\nPresented By " + bcolors.UNDERLINE + (ALL_INCIDENT['feed']['link'] + bcolors.ENDC + "\n"))

    # Check how many entries there are and display either one item, or multiple
    
    if len(all_updates) < 2:
        breaker("=")
        print(bcolors.OKBLUE + "There is only one incident currently" + bcolors.ENDC)
        breaker("=")
        print('')
        breaker("=")
        print(bcolors.FAIL + "Title: " + bcolors.ENDC + all_updates[0]["Title"])
        print(bcolors.FAIL + "URL: " + bcolors.ENDC+  all_updates[0]["URL"])
        print(bcolors.FAIL + "Published: " + bcolors.ENDC +  all_updates[0]["Time"])
        breaker("=")

    if len(all_updates) > 1:
        print(bcolors.WARNING + "There are " + str(len(all_updates)) + " incidents currently\n" + bcolors.ENDC)
        for i in range(int(len(all_updates))):
            breaker("-")
            print(bcolors.FAIL + "Title: " + bcolors.ENDC + all_updates[i]["Title"])
            print(bcolors.FAIL + "URL: " + bcolors.ENDC+  all_updates[i]["URL"])
            print(bcolors.FAIL + "Published: " + bcolors.ENDC +  all_updates[i]["Time"])
            breaker("-")

main()