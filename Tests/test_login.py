import json
import jsonpath
import os
import requests
from Configurations.config import *


config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Configurations", "token.py"))


def test_successful_login():
    response = requests.post(url=baseURL + login, json={"email": email, "password": password})
    responseJson = json.loads(response.text)
    token = jsonpath.jsonpath(responseJson, 'data.token')[0]

    with open(config_file_path, "w") as file:
        file.write(f'response_token = "{token}"')
