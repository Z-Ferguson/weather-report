import requests
import json
import os.path

# Current conditions at that location


class CurrentCondition:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = http://api.wunderground.com/api/103c92d6094529b8/conditions/q/{}{}.format(self.zipcode, .json)

    def get_current_condition():
        r = requests.get(self.url)
        json.dumps(results, indent=4))


# 10 day forecast for that location


class TenDayForecast:
    pass

    def get_ten_day_forecast():
        pass

# Sunrise and sunset times


class SunriseSunset:
    pass

    def get_sunrise_sunset():
        pass

# Any current weather alerts


class WeatherAlert:
    pass

    def get_weather_alert():
        pass

# A list of all active hurricanes (anywhere)


class Hurricane:
    pass

    def get_hurricanes():
        pass


def get_weather_info():
    filename = "wunder_cache_weather.json"
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            results = json.loads(f.read())
    else:
        url = "http://api.wunderground.com/api/"
        r = requests.get(url)
        results = r.json()[" "]

        while r.json()[" "]:
            r = requests.get(r.json()[" "])
            results += r.json()[" "]

        with open(filename, "w") as f:
            f.write(json.dumps(results, indent=4))

    return results


def find_zipcode(where, weather):
    for person in weather:
        if person[" "].lower() == where.lower():
            print(person)


if __name__ == "__main__":
    weather = get_weather_info()
    find_zipcode(input("where would you like to look up? (zipcode) "), weather)
