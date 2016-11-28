import requests
import json

# Current conditions at that location


class CurrentCondition:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/conditions/q/{}{}".format(self.zipcode, '.json')

    def get_current_condition(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))


# cc = CurrentCondition(27713)
# cc.get_current_condition()

# 10 day forecast for that location


class TenDayForecast:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/forecast10day/q/{}{}".format(self.zipcode, '.json')

    def get_ten_day_forecast(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))

# td = TenDayForecast(27713)
# td.get_ten_day_forecast()

# Sunrise and sunset times


class SunRiseSunSet:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/astronomy/q/{}{}".format(self.zipcode, '.json')

    def get_sunrise_sunset(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))
        # results = r.json()
        # sun_phase = results["sun_phase"]
        # print("Sunrise = {}:{}\nSunset = {}:{}".format(
        #     sun_phase["sunrise"]["hour"],
        #     sun_phase["sunrise"]["minute"],
        #     sun_phase["sunset"]["hour"],
        #     sun_phase["sunset"]["minute"]))

# sr = SunRiseSunSet(27713)
# sr.get_sunrise_sunset()


# Any current weather alerts


class WeatherAlert:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/alerts/q/{}{}".format(self.zipcode, '.json')

    def get_weather_alert(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))

# wa = WeatherAlert(27713)
# wa.get_weather_alert()

# A list of all active hurricanes (anywhere)


class Hurricane:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/currenthurricane/q/{}{}".format(self.zipcode, '.json')

    def get_hurricanes(self):
        r = requests.get(self.url)
        print(json.dumps(r.json(), indent=4))

# if __name__ == "__main__":
