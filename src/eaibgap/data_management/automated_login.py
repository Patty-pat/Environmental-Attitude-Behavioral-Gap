import requests
import time

# ---- Constants ----
LOGIN_URL = "https://tanahair.indonesia.go.id/portal-web/login"  # Update with the actual login URL
DATA_URL = "https://tanahair.indonesia.go.id/portal-web/data-endpoint"  # Update with the actual data URL
USERNAME = "your_username"
PASSWORD = "your_password"

# ---- Functions ----
def login_and_get_session(login_url, username, password):
    """
    Logs into the portal and returns an authenticated session.
    """
    session = requests.Session()
    login_payload = {
        'username': username,
        'password': password
    }
    response = session.post(login_url, data=login_payload)
    if response.status_code == 200 and "success" in response.text.lower():  # Adjust based on portal's response
        print("Login successful!")
        return session
    else:
        print(f"Login failed: {response.status_code} - {response.text}")
        return None

def fetch_data(session, data_url, params=None):
    """
    Fetches data from the portal using an authenticated session.
    """
    if not params:
        params = {}

    response = session.get(data_url, params=params)
    if response.status_code == 200:
        print("Data fetched successfully!")
        return response.json()  # Adjust if the portal sends XML or other formats
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return None

def repetitive_task():
    """
    Logs in and performs repetitive data fetching tasks.
    """
    # Login and create session
    session = login_and_get_session(LOGIN_URL, USERNAME, PASSWORD)
    if not session:
        return  # Exit if login fails

    # Example repetitive task: Fetch data every 10 minutes
    while True:
        print("Fetching data...")
        data = fetch_data(session, DATA_URL, params={"layer": "example_layer"})
        if data:
            print("Received data:", data)  # Process or save data as needed
        
        # Wait before the next request
        time.sleep(600)  # Wait for 10 minutes

# ---- Main Execution ----
if __name__ == "__main__":
    repetitive_task()
