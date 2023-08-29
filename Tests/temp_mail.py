import requests
import pytest
import os
# Define Guerrilla Mail API endpoints
BASE_URL = "https://api.guerrillamail.com/ajax.php"
CREATE_EMAIL_ENDPOINT = f"{BASE_URL}?f=get_email_address"
FETCH_EMAILS_ENDPOINT = f"{BASE_URL}?f=check_email&seq=0"

EMAIL_STORAGE_DIRECTORY = "..\TestData"

@pytest.fixture(scope="module")
def temporary_email():
    # Create a temporary email address
    response = requests.get(CREATE_EMAIL_ENDPOINT)
    data = response.json()
    print(response)
    print(data)

    # Define the path to the email address file in the specified directory
    email_addr_file_path = os.path.join(EMAIL_STORAGE_DIRECTORY, "temporary_email.txt")

    # Write the email address to the file
    with open(email_addr_file_path, "w") as email_file:
        email_file.write(email_addr)

    print(f"Email address created: {email_addr}")
    return data["email_addr"]



def test_fetch_temporary_email(temporary_email):
    # Ensure the email address is not empty
    assert temporary_email

def test_fetch_temporary_email_messages(temporary_email):
    # Fetch email messages for the temporary email address
    response = requests.get(f"{FETCH_EMAILS_ENDPOINT}&email={temporary_email}")
    data = response.json()

    # Check if the response contains email messages
    assert "list" in data

    # You can perform additional checks on the email messages data as needed
