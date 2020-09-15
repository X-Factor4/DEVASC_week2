#!/usr/local/bin/python3

import json
import requests
from requests.models import Response

url = 'https://api.chucknorris.io/jokes/random'


def get_chuck_joke(api):
    response = requests.get(url) # TASK 1 - use requests to get a joke.
    return json.loads(response.text) # TASK 2 - return the response in JSON format

if __name__ == '__main__':
    joke = get_chuck_joke(url)  # TASK 3 - correct the json statement
    print(joke['value'])  # TASK 4 - print just a joke without any superfluous symbols
