import requests
import json

# Current conditions at that location


class CurrentCondition:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/conditions/q/{}{}".format(self.zipcode, '.json')

    def get_current_condition(self):
        results = requests.get(self.url)
        return ("Location: {}\nTemp(F): {}F\nWind: {}\nWeather: {}\nHumidity: {}\n"
                .format(results.json()["current_observation"]["display_location"]
                        ["full"],
                        results.json()["current_observation"]["temp_f"],
                        results.json()["current_observation"]["wind_string"],
                        results.json()["current_observation"]["weather"],
                        results.json()["current_observation"]["relative_humidity"]))

# cc = CurrentCondition(27713)
# cc.get_current_condition()

# 10 day forecast for that location


class TenDayForecast:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/forecast10day/q/{}{}".format(self.zipcode, '.json')

    def get_ten_day_forecast(self):
        days_list = []
        results = requests.get(self.url)
        for key in results.json()["forecast"]["txt_forecast"]["forecastday"]:
            day = (key["title"], key["fcttext"])
            days_list.append(day)
        for day, forecast in days_list:
            tenday_data = ("Day: {}\nForecast: {}\n".format(day, forecast))
            print(tenday_data + "\n")

# td = TenDayForecast(27713)
# td.get_ten_day_forecast()

# Sunrise and sunset times


class SunRiseSunSet:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/astronomy/q/{}{}".format(self.zipcode, '.json')

    def get_sunrise(self):
        r = requests.get(self.url)
        sun_times = (r.json()["sun_phase"])
        return "\nSunrise: {}:{}am".format(sun_times["sunrise"]['hour'],
                                           sun_times["sunrise"]['minute'])

    def get_sunset(self):
        r = requests.get(self.url)
        sun_times = (r.json()["sun_phase"])
        return "Sunset: {}:{}pm\n".format(sun_times["sunset"]['hour'],
                                          sun_times["sunset"]['minute'])

# sr = SunRiseSunSet(27713)
# sr.get_sunrise()
# sr.get_sunset()


# Any current weather alerts


class WeatherAlert:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/alerts/q/{}{}".format(self.zipcode, '.json')

    def get_weather_alert(self):
        results = requests.get(self.url)
        if len(results.json()["alerts"]) == 0:
            return "No alerts for your area.\n"
        return ("Alert Type: {}\nDescription: {}\nExpires: {}\n"
                .format(results.json()["alerts"][0]["type"],
                        results.json()["alerts"][0]["description"],
                        results.json()["alerts"][0]["expires"]))
# wa = WeatherAlert(27713)
# wa.get_weather_alert()

# A list of all active hurricanes (anywhere)


class Hurricane:
    def __init__(self):
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/currenthurricane/view.json"

    def get_hurricanes(self):
        results = requests.get(self.url)
        if results.json()["response"]["features"]["currenthurricane"] != 0:
            return ("Name: {}\nCategory: {}\nWindspeed: {}\n".format(
                results.json()["currenthurricane"][0]["stormInfo"]["stormName_Nice"],
                results.json()["currenthurricane"][0]["Current"]["Category"],
                results.json()["currenthurricane"][0]["Current"]["WindSpeed"]["Mph"],
                results.json()["currenthurricane"][0]["Current"]["Movement"]["Text"])
                )

# gh = Hurricane()
# gh.get_hurricanes()


if __name__ == "__main__":
    pass
