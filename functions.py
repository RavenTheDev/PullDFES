import os
import time
import feedparser
import requests

def printdebug(content):
    print(bcolors.WARNING + "           Debug[" + str(content) + "]" + bcolors.ENDC)

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
    # The reason for this is that it will pull all the correct items, plus redundant ones
    # So we need to cross reference it agains t the URL to ensure we only pull valid data
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
        print(bcolors.FAIL + "Title: " + bcolors.ENDC + arrayInput[0]["Title"])
        print(bcolors.FAIL + "URL: " + bcolors.ENDC+  arrayInput[0]["URL"])
        print(bcolors.FAIL + "Published: " + bcolors.ENDC +  arrayInput[0]["Time"])
        breaker("=")
        

    elif arrayCount > 1:
        breaker("=")
        print(bcolors.WARNING + "There are " + str(arrayCount) + " items currently" + bcolors.ENDC)
        breaker("=")
        for i in range(0,arrayCount):
                print(bcolors.FAIL + "Title: " + bcolors.ENDC + arrayInput[i]["Title"])
                print(bcolors.FAIL + "URL: " + bcolors.ENDC+  arrayInput[i]["URL"])
                print(bcolors.FAIL + "Published: " + bcolors.ENDC +  arrayInput[i]["Time"])
                breaker("-")
                print('')

    else:
        breaker("=")
        print(bcolors.OKBLUE + 'No Items to Show' + bcolors.ENDC)
        breaker("=")

def clearscreen():
    '''Clear the screen depending on what OS you're running'''
    os.system('cls' if os.name=='nt' else 'clear')

def mainMenu():
    
    ''' The Main Menu'''
    breaker('=')
    print('DFES and EMERGENCY SERVICES')
    print('Select option below')
    breaker("=")
    print('1. Incidents')
    print('2. Prescribed Burns')
    print('3. Firebans')
    print('4. Weather Warnings')
    print('0. Exit Application')

    print('\nPlease select an option\n')
    userchoice = input('Please choose a menu item > ')
    try:
        userchoice = int(userchoice)
    except:
        pass

    if userchoice == 1:
        incidentenu()
    
    elif userchoice == 2:
        prescribedBurnsMenu()

    elif userchoice == 3:
        firebansMenu()

    elif userchoice == 4:
        weatherWarningsWAMenu()

    elif userchoice == 0:
        clearscreen()
        quit
            
    else:
        print('Invalid Option')
        time.sleep(1)
        clearscreen()
        mainMenu()

def firebansMenu():
    ''' Display the Fire Bans menu'''
    clearscreen()
    displayFeed(arrayFirebans)
    print('Press any key to return to the main menu')
    input('> ')
    clearscreen()
    mainMenu()

def incidentenu():
    '''Display the Incident Menu'''
    clearscreen()
    displayFeed(arrayIncidents)
    print('Press any key to return to the main menu')
    input('> ')
    clearscreen()
    mainMenu()

def prescribedBurnsMenu():
    ''' Display the Prescribed Burns menu '''
    clearscreen()
    displayFeed(arrayPrescribedBurns)
    print('Press any key to return to the main menu')
    input('> ')
    clearscreen()
    mainMenu()

def weatherWarningsWAMenu():
    ''' Display the Weather Warnings menu'''
    clearscreen()
    displayFeed(arrayWeatherWarningsWA)
    print('Press any key to return to the main menu')
    input('> ')
    clearscreen()
    mainMenu()

def pullFireBans():
    ''' Pull Fire Ban Data from Website'''
    try:
        resp = requests.get('https://www.emergency.wa.gov.au/data/message_TFB.rss',timeout = 5.0)
        feed_firebans = feedparser.parse(resp)
        global arrayFirebans
        arrayFirebans = []
        for i in range(len(feed_firebans.entries)):
            arrayFirebans.append({"URL": feed_firebans.entries[i].link,"Title": feed_firebans.entries[i].title, "Time": feed_firebans.entries[i].published})
        print('Firebans                 ' + u'\u2713')
        return arrayFirebans

    except requests.ReadTimeout:
        print("Timeout getting data!")

def pullPrescribedBurns():
    try:
        resp = requests.get('https://www.dpaw.wa.gov.au/management/fire/prescribed-burning/burns/burns-planned-for-lighting-today?format=feed',timeout = 5.0)
        feed_burns = feedparser.parse(resp.text)
        global arrayPrescribedBurns
        arrayPrescribedBurns = []
        for i in range(len(feed_burns.entries)):
            arrayFirebans.append({"URL": feed_burns.entries[i].link,"Title": feed_burns.entries[i].title, "Time": feed_burns.entries[i].published})
        print('Prescribed Burns         ' + u'\u2713')
        return arrayPrescribedBurns

    except requests.ReadTimeout:
        print("Timeout getting data!")

def pullIncidents():
    try:
        resp = requests.get('https://www.emergency.wa.gov.au/data/message.rss',timeout = 5.0)
        feed_incidents = feedparser.parse(resp.text)
        global arrayIncidents
        arrayIncidents = []
        for i in range(len(feed_incidents.entries)):
            arrayIncidents.append({"URL": feed_incidents.entries[i].link,"Title": feed_incidents.entries[i].title, "Time": feed_incidents.entries[i].published})
        print('Incidents                ' + u'\u2713')
        return arrayIncidents

    except requests.ReadTimeout:
        print("Timeout getting data!")

def pullWeatherWarningsWA():
    try:
        resp = requests.get('http://www.bom.gov.au/fwo/IDZ00060.warnings_wa.xml', timeout = 5.0)
        feed_weatherWarningsWA = feedparser.parse(resp.text)
        global arrayWeatherWarningsWA
        arrayWeatherWarningsWA = []
        for i in range(len(feed_weatherWarningsWA.entries)):
            arrayWeatherWarningsWA.append({"URL": feed_weatherWarningsWA.entries[i].link,"Title": feed_weatherWarningsWA.entries[i].title, "Time": feed_weatherWarningsWA.entries[i].published})
        print('Weather Warnings         ' + u'\u2713 \n')
        return arrayWeatherWarningsWA

    except requests.ReadTimeout:
        print("Timeout getting data!")