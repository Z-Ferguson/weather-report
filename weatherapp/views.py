from django.shortcuts import render
from django.http import HttpResponse
# from django.utils import simplejson
from django.http import JsonResponse


def current_condition(request):
    return JsonResponse({
        "current_observation": {
            "dewpoint_f": 44,
            "local_epoch": "1480367075",
            "precip_1hr_in": "0.00",
            "heat_index_c": "NA",
            "dewpoint_c": 6,
            "display_location": {
                "full": "Durham, NC",
                "city": "Durham",
                "state_name": "North Carolina",
                "country_iso3166": "US",
                "zip": "27713",
                "elevation": "105.2",
                "state": "NC",
                "magic": "1",
                "longitude": "-78.91999817",
                "country": "US",
                "wmo": "99999",
                "latitude": "35.91999817"
            },
            "windchill_f": "NA",
            "observation_time_rfc822": "Mon, 28 Nov 2016 16:04:26 -0500",
            "UV": "0.0",
            "visibility_km": "16.1",
            "wind_dir": "SSE",
            "feelslike_f": "55.4",
            "precip_1hr_metric": " 0",
            "temp_f": 55.4,
            "wind_mph": 0.0,
            "wind_string": "Calm",
            "precip_today_string": " in ( mm)",
            "feelslike_c": "13.0",
            "weather": "",
            "dewpoint_string": "44 F (6 C)",
            "visibility_mi": "10.0",
            "ob_url": "http://www.wunderground.com/cgi-bin/findweather/getForecast?query=35.990646,-78.937607",
            "pressure_trend": "+",
            "precip_today_in": "",
            "image": {
                "link": "http://www.wunderground.com",
                "title": "Weather Underground",
                "url": "http://icons.wxug.com/graphics/wu2/logo_130x80.png"
            },
            "observation_epoch": "1480367066",
            "estimated": {},
            "wind_degrees": 162,
            "wind_gust_kph": 0,
            "observation_time": "Last Updated on November 28, 4:04 PM EST",
            "solarradiation": "22",
            "icon": "",
            "local_tz_offset": "-0500",
            "local_tz_short": "EST",
            "icon_url": "http://icons.wxug.com/i/c/k/.gif",
            "pressure_in": "30.14",
            "heat_index_string": "NA",
            "heat_index_f": "NA",
            "local_tz_long": "America/New_York",
            "wind_gust_mph": 0,
            "history_url": "http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNCDURHA138",
            "observation_location": {
                "latitude": "35.990646",
                "full": "Duke Homesites, Durham, North Carolina",
                "city": "Duke Homesites, Durham",
                "longitude": "-78.937607",
                "country_iso3166": "US",
                "state": "North Carolina",
                "elevation": "341 ft",
                "country": "US"
            },
            "temperature_string": "55.4 F (13.0 C)",
            "relative_humidity": "64%",
            "windchill_string": "NA",
            "feelslike_string": "55.4 F (13.0 C)",
            "pressure_mb": "1020",
            "temp_c": 13.0,
            "forecast_url": "http://www.wunderground.com/US/NC/Durham.html",
            "station_id": "KNCDURHA138",
            "nowcast": "",
            "precip_today_metric": "--",
            "precip_1hr_string": "0.00 in ( 0 mm)",
            "wind_kph": 0,
            "local_time_rfc822": "Mon, 28 Nov 2016 16:04:35 -0500",
            "windchill_c": "NA"
        },
        "response": {
            "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
            "version": "0.1",
            "features": {
                "conditions": 1
            }
        }
    })
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
