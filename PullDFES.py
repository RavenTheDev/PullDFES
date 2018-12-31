# Simple app that will pull the information from the DFES website via RSS feed, and format it for easy reading.
# Currently setup for North Metro, but can be changed extremely easily by simply changing the URL@@

import feedparser
import time
import os

print('\n Pulling Array Information. Please wait ... \n')
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
    '''This is a breaker that separates information based on the ASCII text of your choice'''
    print(bcolors.HEADER + (str(ascii) * 50) + bcolors.ENDC)

def displayFeed(arrayInput):
    ''' Displays the Feed depending on what array is specified'''
    arrayCount = 0 # Set this to 0 as a Counter to start with

    # Increment the number in ArrayCount if the items are valid, to get the number of items
    for values in range(0,len(arrayInput)):
        if '#map' in arrayInput[values]["URL"]:
            arrayCount +=1
        elif '#firedangerratings' in arrayInput[values]["URL"]:
            arrayCount +=1
        elif '#totalfirebans' in arrayInput[values]["URL"]:
            arrayCount +=1
        elif 'http://www.bom.gov.au/wa/warnings' in arrayInput[values]["URL"]:
            arrayCount +=1

    if arrayCount == 1 :
        breaker("=")
        print(bcolors.OKBLUE + "There is only one item currently" + bcolors.ENDC)
        breaker("=")
        print('')
        breaker("=")
        print(bcolors.FAIL + "Title: " + bcolors.ENDC + arrayInput[0]["Title"])
        print(bcolors.FAIL + "URL: " + bcolors.ENDC+  arrayInput[0]["URL"])
        print(bcolors.FAIL + "Published: " + bcolors.ENDC +  arrayInput[0]["Time"])
        breaker("=")
        arrayCount = 0

    elif arrayCount > 1:
        print(bcolors.WARNING + "There are " + str(arrayCount) + " items currently" + bcolors.ENDC)
        breaker("=")
        for i in range(0,arrayCount):
                print(bcolors.FAIL + "Title: " + bcolors.ENDC + arrayInput[i]["Title"])
                print(bcolors.FAIL + "URL: " + bcolors.ENDC+  arrayInput[i]["URL"])
                print(bcolors.FAIL + "Published: " + bcolors.ENDC +  arrayInput[i]["Time"])
                breaker("-")

    else:
        print('There are no incidents \n')

def clearscreen():
    '''Clear the screen depending on what OS you're running'''
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    clearscreen()
    ''' The Main Menu'''
    print('DFES and EMERGENCY SERVICES')
    breaker("=")
    print('1. Incidents')
    print('2. Prescribed Burns')
    print('3. Firebans')
    print('4. Weather Warnings')

    print('\nPlease select an option\n')
    userchoice = input('Please choose a menu item > ')
    try:
        userchoice = int(userchoice)
    except:
        pass

    clearscreen()

    if userchoice == 1:
        incidentmenu()
    
    elif userchoice == 2:
        prescribedBurnsMenu()

    elif userchoice == 3:
        firebansmenu()

    elif userchoice == 4:
        weatherwarningsWAmenu()
            
    else:
        print('Invalid Option')
        time.sleep(2)
        menu()

def incidentmenu():
    '''Display the Incident Menu'''
    displayFeed(arrayIncidents)
    print('Press any key to return to the main menu')
    input('> ')
    menu()

def prescribedBurnsMenu():
    ''' Display the Prescribed Burns menu '''
    displayFeed(arrayPrescribedBurns)
    print('Press any key to return to the main menu')
    input('> ')
    menu()

def firebansmenu():
    ''' Display the Fire Bans menu'''
    displayFeed(arrayFirebans)
    print('Press any key to return to the main menu')
    input('> ')
    menu()

def weatherwarningsWAmenu():
    ''' Display the Weather Warnings menu'''
    displayFeed(arrayWeatherWarningsWA)
    print('Press any key to return to the main menu')
    input('> ')
    menu()

menu()