import requests

# Higher-order function to fetch weather data from WeatherAPI
def fetch_weather(api_key):
    def get_weather(city):
        endpoint = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
        response = requests.get(endpoint)
        data = response.json()
        return data

    return get_weather

# Side-effect-free function to display weather information with error handling
def display_weather(data):
    try:
        current_temperature = data['current']['temp_c']
        weather_description = data['current']['condition']['text']
        print(f'Current Temperature: {current_temperature} °C\nWeather Description: {weather_description}')
    except KeyError as e:
        print(f'Error: {e}. Unable to retrieve weather information.')

# Function as a parameter to handle user input
def get_user_input():
    return input('Enter city name: ')

# Closures and anonymous functions for composition
def main(api_key):
    get_weather_info = fetch_weather(api_key)

    def get_and_display_weather():
        city = get_user_input()
        weather_data = get_weather_info(city)
        display_weather(weather_data)

    return get_and_display_weather

# API Key for WeatherAPI (Replace with your WeatherAPI key)
api_key = '9ba0084a8bd54480b92172347242301'

# Get and display weather information
get_weather_and_display = main(api_key)
get_weather_and_display()
