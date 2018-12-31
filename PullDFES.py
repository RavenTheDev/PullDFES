# Simple app that will pull the information from the DFES website via RSS feed, and format it for easy reading.
# Currently setup for North Metro, but can be changed extremely easily by simply changing the URL@@

import feedparser
import time

print('Pulling Array Information. Please wait ... \n')
feed_incidents = feedparser.parse("https://www.emergency.wa.gov.au/data/message.rss")
arrayIncidents = []
for i in range(len(feed_incidents.entries)):
    arrayIncidents.append({"URL": feed_incidents.entries[i].link,"Title": feed_incidents.entries[i].title, "Time": feed_incidents.entries[i].published})
print('Incidents                ' + u'\u2713')

feed_prescribed_burns = feedparser.parse('https://www.dpaw.wa.gov.au/management/fire/prescribed-burning/burns/burns-planned-for-lighting-today?format=feed')
arrayPrescribedBurns = []
for i in range(len(feed_prescribed_burns.entries)):
    arrayIncidents.append({"URL": feed_prescribed_burns.entries[i].link,"Title": feed_prescribed_burns.entries[i].title, "Time": feed_prescribed_burns.entries[i].published})
print('Prescribed Burns         ' + u'\u2713')

feed_fireDangerWarnings = feedparser.parse('https://www.emergency.wa.gov.au/data/message_FDR.rss')
arrayFireDangerRatings = []
for i in range(len(feed_fireDangerWarnings.entries)):
    arrayFireDangerRatings.append({"URL": feed_fireDangerWarnings.entries[i].link,"Title": feed_fireDangerWarnings.entries[i].title, "Time": feed_fireDangerWarnings.entries[i].published})
print('Fire Danger Ratings      ' + u'\u2713')

feed_firebans = feedparser.parse('https://www.emergency.wa.gov.au/data/message_TFB.rss')
arrayFirebans = []
for i in range(len(feed_firebans.entries)):
    arrayFirebans.append({"URL": feed_firebans.entries[i].link,"Title": feed_firebans.entries[i].title, "Time": feed_firebans.entries[i].published})
print('Firebans                 ' + u'\u2713')

feed_weatherWarningsWA = feedparser.parse('http://www.bom.gov.au/fwo/IDZ00060.warnings_wa.xml')
arrayWeatherWarningsWA = []
for i in range(len(feed_weatherWarningsWA.entries)):
    arrayWeatherWarningsWA.append({"URL": feed_weatherWarningsWA.entries[i].link,"Title": feed_weatherWarningsWA.entries[i].title, "Time": feed_weatherWarningsWA.entries[i].published})
print('Weather Warnings         ' + u'\u2713 \n')

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

def displayFeed(arrayInput):
    arrayCount =0 # Set this to 0 as a Counter to start with

    # Increment the number in ArrayCount if the items are valid, to get the number of items
    for values in range(0,len(arrayInput)):
        if 'https://www.emergency.wa.gov.au/#map' in arrayInput[values]["URL"]:
            arrayCount +=1

    # If there is only 1 item in the list

    if arrayCount == 0 :
        print('There are no incidents \n')

    elif arrayCount == 1 :
        breaker("=")
        print(bcolors.OKBLUE + "There is only one item currently" + bcolors.ENDC)
        breaker("=")
        print('')
        breaker("=")
        print(bcolors.FAIL + "Title: " + bcolors.ENDC + arrayInput[0]["Title"])
        print(bcolors.FAIL + "URL: " + bcolors.ENDC+  arrayInput[0]["URL"])
        print(bcolors.FAIL + "Published: " + bcolors.ENDC +  arrayInput[0]["Time"])
        breaker("=")

    elif arrayCount > 1:
        print(bcolors.WARNING + "There are " + str(arrayCount) + " items currently" + bcolors.ENDC)
        breaker("=")
        for i in range(0,arrayCount):
            if "https://www.emergency.wa.gov.au/#map" in arrayInput[i]["URL"]:
                print(bcolors.FAIL + "URL: " + bcolors.ENDC+  arrayInput[i]["URL"])
                print(bcolors.FAIL + "Title: " + bcolors.ENDC + arrayInput[i]["Title"])
                print(bcolors.FAIL + "Published: " + bcolors.ENDC +  arrayInput[i]["Time"])
                breaker("-")

breaker("=")
displayFeed(arrayIncidents)