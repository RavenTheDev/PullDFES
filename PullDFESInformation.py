# Simple app that will pull the information from the DFES website via RSS feed, and format it for easy reading.
# Currently setup for North Metro, but can be changed extremely easily by simply changing the URL@@
import time
import functions as DFESFunctions #This holds all the custom DFESFunctions for the application

#===== Start of the Application =====
# First we are going to setup the application

DFESFunctions.clearscreen()
DFESFunctions.breaker('=')
print('Obtaining Data. Please Wait ...\n')
DFESFunctions.pullFireBans()
DFESFunctions.pullIncidents()
DFESFunctions.pullPrescribedBurns()
DFESFunctions.pullWeatherWarningsWA()
time.sleep(0.5)
DFESFunctions.mainMenu()