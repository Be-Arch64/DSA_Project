import requests
from api_key import api_key #Remove this line
api_key = api_key() # Replace the function with your openweather api key


def get_data(place, days=None, selection=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Mysore", days=3))
