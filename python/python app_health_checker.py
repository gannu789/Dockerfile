import requests
import time

# Application URL
APP_URL = "http://example.com"

# Function to check application status
def check_application_status():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            print(f"Application is UP. Status code: {response.status_code}")
        else:
            print(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Error: {e}")

# Main loop to monitor application
def main():
    while True:
        check_application_status()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()