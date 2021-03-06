import requests
import json


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
            tenday_data = ("Time: {}\nForecast: {}\n".format(day, forecast))
            print(tenday_data + "\n")


class SunRiseSunSet:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/astronomy/q/{}{}".format(self.zipcode, '.json')

    def get_sunrise(self):
        r = requests.get(self.url)
        sun_times = (r.json()["sun_phase"])
        return "\nSunrise: {}:{}am,\n Sunset: {}:{}pm\n".format(sun_times["sunrise"]['hour'],
                                                                sun_times["sunrise"]['minute'],
                                                                sun_times["sunset"]['hour'],
                                                                sun_times["sunset"]['minute'])


class WeatherAlert:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/alerts/q/{}{}".format(self.zipcode, '.json')

    def get_weather_alert(self):
        results = requests.get(self.url)
        if len(results.json()["alerts"]) == 0:
            return "No alerts, go outside you nerd\n"
        return ("Alert Type: {}\nDescription: {}\nExpires: {}\n"
                .format(results.json()["alerts"][0]["type"],
                        results.json()["alerts"][0]["description"],
                        results.json()["alerts"][0]["expires"]))


class Hurricane:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.wunderground.com/api/103c92d6094529b8/currenthurricane/q/{}{}".format(self.zipcode, '.json')

    def get_hurricane(self):
            results = requests.get(self.url)
            if len(results.json()["currenthurricane"]) == 0:
                return "There are no Hurricanes currently.\n"
            return ("Name: {}\nCategory: {}\nWindspeed: {}\n".format(
                results.json()["currenthurricane"][0]["stormInfo"]
                ["stormName_Nice"],
                results.json()["currenthurricane"][0]["Current"]["Category"],
                results.json()["currenthurricane"][0]["Current"]["WindSpeed"]
                ["Mph"],
                results.json()["currenthurricane"][0]["Current"]["Movement"]
                ["Text"]))


if __name__ == "__main__":
    pass
