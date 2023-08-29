import random
import string


def generate_ramdom_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def random_string():
    string_len=10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(string_len))
    return random_string

class HeadersUtility:
    @staticmethod
    def get_authorization_header(token):
        return {
            "Authorization": f"Bearer {token}"
        }

    @staticmethod
    def test_data():
        data = {
            "email": generate_ramdom_email(),
            "fullName": random_string(),
            "companyName": random_string(),
            "domainName": random_string(),
            "phone": "1234567890"
        }
        return data







