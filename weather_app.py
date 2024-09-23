
import requests

def get_weather(city):
    api_key = "your_api_key"  # Replace with your OpenWeather API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    if data['cod'] == 200:
        main = data['main']
        return f"Temperature: {main['temp']}°C\nHumidity: {main['humidity']}%"
    else:
        return "City not found"

# Example
city = "London"
print(get_weather(city))
