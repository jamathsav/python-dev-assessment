import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()
        users = response.json()
        for user in users[:num_users]:
            print(f"Name: {user['name']}, Email: {user['email']}, City: {user['address']['city']}")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except KeyError as e:
        print(f"Missing expected key: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example
fetch_and_display_users(3)