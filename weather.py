from api_endpoints import (CurrentCondition, TenDayForecast, SunRiseSunSet,
                           WeatherAlert, Hurricane)

from menu import Menu


def quit():
    exit()


def current_condition():
    zip_code = input("Please Enter your zip code: ")
    current_f = CurrentCondition(zip_code)
    print(current_f.get_current_condition())


def ten_day_forecast():
    zip_code = input("Please Enter your zip code: ")
    ten_day_f = TenDayForecast(zip_code)
    ten_day_f.get_ten_day_forecast()


def sunrise_sunset():
    zip_code = input("Please Enter your zip code: ")
    sun = SunRiseSunSet(zip_code)
    sun_rise = sun.get_sunrise()
    print(sun_rise)


def alert():
    zip_code = input("Please Enter your zip code: ")
    alert = WeatherAlert(zip_code)
    print(alert.get_weather_alert())


def hurricane_info():
    zipcode = input("Please Enter your zip code: ")
    hurricane_info = Hurricane(zipcode)
    print(hurricane_info.get_hurricane())


def main():
    m = Menu("\t--Weather Forecast App--\n")
    m.register("Get current forecast", current_condition)
    m.register("Get ten day forecast", ten_day_forecast)
    m.register("Get today's sunrise/sunset", sunrise_sunset)
    m.register("Get weather alerts", alert)
    m.register("Get hurricanes", hurricane_info)
    m.register("Quit", quit)
    m.display()

main()
