# Simple app that will pull the information from the DFES website via RSS feed, and format it for easy reading.
# Currently setup for North Metro, but can be changed extremely easily by simply changing the URL

import feedparser
import numpy as np
import os, sys

CAP_FEED = feedparser.parse("https://www.emergency.wa.gov.au/data/message_regions_MetroNorthCoastal.rss")
ALL_INCIDENT = feedparser.parse("https://www.emergency.wa.gov.au/data/incident_FCAD_regions_METRONORTHCOASTAL.rss")


warnings = []
for i in range(len(CAP_FEED.entries)):
    warnings.append({"URL": CAP_FEED.entries[i].link,"Title": CAP_FEED.entries[i].title, "Time": CAP_FEED.entries[i].published})

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
    print(bcolors.HEADER + (str(ascii) * 50) + bcolors.ENDC + '\n')

def main():

    print (bcolors.HEADER,"======",(CAP_FEED['feed']['title']),"======",bcolors.ENDC)
    print (bcolors.HEADER,"======",(ALL_INCIDENT['feed']['title']),"======",bcolors.ENDC)
    print ("\nPresented By" , (CAP_FEED['feed']['link'] + "\n"))

    # First we want to print the WARNINGS

    if len(warnings) < 2:
        print("There is only one warning currently\n")
        breaker("=")
        print(bcolors.FAIL + "Title: " + bcolors.ENDC + warnings[0]["Title"])
        print(bcolors.FAIL + "URL: " + bcolors.ENDC+  warnings[0]["URL"])
        print(bcolors.FAIL + "Published: " + bcolors.ENDC +  warnings[0]["Time"])

    if len(warnings) >= 2:
        for i in range(int(len(warnings))):
            print("There are" + str(len(all_updates)) + "warnings currently\n")
            breaker("=")
            print(bcolors.FAIL + "Title: " + bcolors.ENDC + warnings[i]["Title"])
            print(bcolors.FAIL + "URL: " + bcolors.ENDC+  warnings[i]["URL"])
            print(bcolors.FAIL + "Published: " + bcolors.ENDC +  warnings[i]["Time"])

    # Check how many entries there are and display either one item, or multiple
    if len(all_updates) < 2:
        print("There is only one incident currently\n")
        breaker("=")
        print(bcolors.FAIL + "Title: " + bcolors.ENDC + all_updates[0]["Title"])
        print(bcolors.FAIL + "URL: " + bcolors.ENDC+  all_updates[0]["URL"])
        print(bcolors.FAIL + "Published: " + bcolors.ENDC +  all_updates[0]["Time"])

    if len(all_updates) >= 2:
        for i in range(int(len(all_updates))):
            print("There are" + str(len(all_updates)) + "incidents currently\n")
            breaker("=")
            print(bcolors.FAIL + "Title: " + bcolors.ENDC + all_updates[0]["Title"])
            print(bcolors.FAIL + "URL: " + bcolors.ENDC+  all_updates[0]["URL"])
            print(bcolors.FAIL + "Published: " + bcolors.ENDC +  all_updates[0]["Time"])

main()