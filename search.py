import json
import urllib2
import web

# only response for urls like /weather/city
urls = (
    '/weather/(.*)', 'get_weather_by_city'
)

app = web.application(urls, globals())

# ask internet source for the weather forecast and temperature
# and if we get response then create a json object else empty object


class get_weather_by_city:
    def GET(self, city):
        urlWeather = 'http://api.openweathermap.org/data/2.5/weather?q='
        try:
            response = urllib2.urlopen(urlWeather+city)
            data = json.load(response)
            result = {'weather': str(data['weather'][0]['description']), 'temp': round(data['main']['temp']-273.15, 2)}
            return json.dumps(result)
        except:
            return json.dumps({})

# run the server
if __name__ == "__main__":
    app.internalerror = web.debugerror
    app.run()
