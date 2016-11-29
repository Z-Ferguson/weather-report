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
    sun_set = sun.get_sunset()
    print(sun_rise + "\n" + sun_set)


def alert():
    zip_code = input("Please Enter your zip code: ")
    alert = WeatherAlert(zip_code)
    print(alert.get_weather_alert())


def hurricane_info():
    zip_code = input("Please Enter your zip code: ")
    hurricane_info = Hurricane(zip_code)
    print(hurricane_info.get_hurricanes())


def main():
    m = Menu("\t--Welcome to Weather Forecast--\n")
    m.register("Get current forecast", current_condition)
    m.register("Get ten day forecast", ten_day_forecast)
    m.register("Get today's sunrise/sunset", sunrise_sunset)
    m.register("Get weather alerts", alert)
    m.register("Get hurricane information", hurricane_info)
    m.register("Quit", quit)
    m.display()

main()
