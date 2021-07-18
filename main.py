from flask import Flask, render_template, request

app = Flask(__name__)


import numpy as np
from bs4 import BeautifulSoup
import requests
import json
from typing import Any, Dict, List, Tuple, Union

verbs_movement = [
    "go",
    "went",
    "gone",
    "come",
    "came",
    "visit",
    "run",
    "ran",
    "sprint",
    "jog",
    "trot",
    "dash",
    "walk",
    "stride",
    "ride",
    "wander",
    "stroll",
    "march",
]


class weather_tomorrow:
    def __init__(self, city):
        self.city = city
        self.problems = False
        self.tomorrow_info = self.get_forecast_tomorrow()

    @staticmethod
    def get_forecast_tomorrow():
        url_for_location = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&units=metric&APPID={self.api_key}"
        r = requests.get(url_for_location)
        if r.status_code != 200:
            self.problems = True
            return {"Problems": "invalid town"}
        lat = r.json().get("coord").get("lat")
        lon = r.json().get("coord").get("lon")
        url_forecast = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&units=metric&appid={self.api_key}"
        r_forecast = requests.get(url_forecast)
        return r_forecast.json().get("daily")[1]

    def __call__(self):
        return [self.problems, self.tomorrow_info]


class the_relevant_activity_depends_on_weather:
    @staticmethod
    def check_the_weather_is_bad(weather):
        wind = weather["wind_speed"] > 20
        precip = weather["pop"] > 0.5
        temp = weather["temp"]["max"] > 28 or weather["temp"]["min"] < -25
        return wind or precip or temp

    @staticmethod
    def get_new_activity():
        url = f"http://www.boredapi.com/api/activity/"
        resp = requests.get(url)
        return resp.json()["activity"]

    @staticmethod
    def check_the_activity(activity) -> bool:
        return [s for s in verbs_movement if s in activity]

    def __call__(self, activity, weather):
        weather_is_bad = self.check_the_weather_is_bad(weather)
        activity = activity.lower()
        if not self.check_the_activity(activity) or not weather_is_bad:
            return [True, activity]
        for i in range(10):
            new_activity = self.get_new_activity()
            if not self.check_the_activity(new_activity.lower()):
                return [False, new_activity]
        return [False, "Stay at home"]


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "GET":
        return "Sorry"
    if request.method == "POST":
        all_requests = request.form
        city = all_requests["City"]
        activity = all_requests["Activity"]
        q = weather_tomorrow(city)
        weather = q()
        if weather[0]:
            return render_template("data.html", problem=True)
        return render_template(
            "data.html",
            problem=False,
            activity=the_relevant_activity_depends_on_weather()(activity, weather[1]),
            city=city,
            form_data=weather[1]["feels_like"],
            description=weather[1]["weather"][0]["description"],
        )


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
