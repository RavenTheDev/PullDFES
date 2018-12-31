import feedparser
import time
import os

feed_weatherWarningsWA = feedparser.parse('http://www.bom.gov.au/fwo/IDZ00060.warnings_wa.xml')
arrayWeatherWarningsWA = []
for i in range(len(feed_weatherWarningsWA.entries)):
    arrayWeatherWarningsWA.append({"URL": feed_weatherWarningsWA.entries[i].link,"Title": feed_weatherWarningsWA.entries[i].title, "Time": feed_weatherWarningsWA.entries[i].published})
print('Weather Warnings         ' + u'\u2713 \n')

for each in range(0,len(arrayWeatherWarningsWA)):
    print(arrayWeatherWarningsWA[each]["URL"])
    print(arrayWeatherWarningsWA[each]["Title"])
    print(arrayWeatherWarningsWA[each]["Time"] + "\n")
