import json
import urllib2
import sys


def weather(city):
    # web service call to get the weather forecast and the temperature
    data = json.load(urllib2.urlopen('http://localhost:8080/weather/'+city))
    # print the weather forecast and temperatura if we get data, otherwise No data found
    if (len(data) > 1):
        print 'Weather forecast in ' + city + ' is ' + data['weather']
        print 'Temperature: ' + str(data['temp']) + ' degrees'
    else:
        print 'No data found for ' + city

# check at least one argument (if there's more arguments we discard)
if (len(sys.argv) > 1):
    weather(sys.argv[1])
else:
    print 'You must specify the city'
