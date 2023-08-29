import requests
import pytest
from Configurations import token
from Configurations.config import *
from utilities.headers_utility import *
import json
import random
import string


@pytest.fixture
def response_token():
    return token.response_token

def test_temp_email():
    # Replace 'your_api_key' with your Mailinator API key
    api_key = 'ddcdnjj'
    response = requests.post(f'https://api.mailinator.com/v2/domains/inbox.mailinator.com/inboxes?token={api_key}')
    email = response.json()['inbox']
    print(response)
    print(email)
    yield email

def generate_ramdom_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email


def test_successful_comp(response_token):
    headers = HeadersUtility.get_authorization_header(response_token)
    response = requests.get(url=baseURL + costcenter, headers=headers)
    assert response.status_code == 200

def test_post_request(response_token):
    headers = HeadersUtility.get_authorization_header(response_token)
    data = HeadersUtility.test_data()
    response = requests.post(url=baseURL + register, headers=headers, json=data)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post responce body: ", json_str)
    assert "status" in json_data
    assert json_data["status"] == "CREATED"
    return json_data

