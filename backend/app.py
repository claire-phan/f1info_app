from flask import Flask, jsonify
import requests

app = Flask(__name__) #am i supposed to name it here?

#Create URL for API request.
def create_url(category: str = None) -> str:
    BASE_URL = "http://ergast.com/api/f1/current"

    if category is not None:
        new_url = BASE_URL + "/" + category + ".json"
        return new_url
    
    return BASE_URL + ".json"

def get_data(url: str) -> dict:
    response = requests.get(url)
    try:
        if response.status_code == 200:
            data_dict = response.json() #turns data from json into a dictionary
            print("API Request was successful!")
            print(data_dict)
            return data_dict
        else:
            print(f"API Request failed with status code: {response.status_code}")

    finally:
        response.close()

    return None

def parse_data(data: dict):
    pass

get_data("http://ergast.com/api/f1/current/results.json")

class Race:
    def __init__(self, race: dict, results):
        self._round = race[round]
        self._name = race[raceName]
        self._circuit = race[circuit][circuitName]
        self._city = race[location][locality]
        self._country = race[location][country]
        self._date = race[date]
        self._time = race[time]
        
    def race_round(self) -> int:
        return self._round

    

