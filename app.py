from flask import Flask
import requests
import json
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "Simple backend to provide data for a project."


@app.route('/news')
def news():
    params = {
        'apiKey': os.environ.get("NEWS_API_KEY"),
    }
    r = requests.get(
        'https://newsapi.org/v2/top-headlines?country=no',
        params=params)
    return json.loads(r.text)


@app.route('/weather')
def weather():
    params = {
        'APPID': os.environ.get('WEATHER_API_KEY'),
    }
    r = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=Stavanger,no',
        params=params)
    return json.loads(r.text)


@app.route('/football')
def football():
    params = {
        'X-Auth-Token': os.environ.get("FOOTBALL_API_KEY"),
    }
    r = requests.get(
        'https://api.football-data.org/v2/matches',
        params=params)
    return json.loads(r.text)


if __name__ == '__main__':
    app.run(debug=True)
