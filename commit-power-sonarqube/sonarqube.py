# sonarqube.py

import requests
from requests.auth import HTTPBasicAuth

def get_sonarqube_data(url, username, password):
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        content_type = response.headers.get('Content-Type')
        if 'application/json' in content_type:
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                print(f"Error decoding JSON from {url}")
                print("Response text:", response.text)
                return None
        elif 'text/html' in content_type:
            print(f"Error: Response is HTML - Content-Type: {content_type}")
            return response.text
        else:
            print(f"Unexpected Content-Type: {content_type}")
            print("Response text:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
        return None
