import requests
import json
import os.path

# Current conditions at that location


class CurrentCondition:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/conditions/q/{}{}".format(self.zipcode, '.json')

    def get_current_condition(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))


cc = CurrentCondition(27713)
cc.get_current_condition()

# 10 day forecast for that location


class TenDayForecast:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/forecast10day/q/{}{}".format(self.zipcode, '.json')

    def get_ten_day_forecast():
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))

# Sunrise and sunset times


class SunriseSunset:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/astronomy/q/{}{}".format(self.zipcode, '.json')

    def get_sunrise_sunset():
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))


    # sr = SunriseSunset(27713)
    # sr.SunriseSunset()


# Any current weather alerts


class WeatherAlert:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = (
                    "http://api.wunderground.com/api/103c92d6094529b8/alerts/q/
                    {}{}".format(self.zipcode, '.json')
        )

    def get_weather_alert():
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))

# A list of all active hurricanes (anywhere)


class Hurricane:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = (
        "http://api.wunderground.com/api/103c92d6094529b8/currenthurricane/q/{}{}".format(self.zipcode, '.json')

    def get_hurricanes():
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))

if __name__ == "__main__":
