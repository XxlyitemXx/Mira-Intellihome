import requests
import logging

def get_weather(api_key, city, country):
    """Fetches weather information from OpenWeatherMap API.

    Args:
        api_key (str): OpenWeatherMap API key.
        city (str): City name.
        country (str): Country code.

    Returns:
        str: Formatted weather information, or "City Not Found" if an error occurs.
    """
    logging.info("Requesting Weather information.")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city},{country}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 1)
        weather_info = f"The weather in {city} is {weather} with a temperature of {temperature}°C"
        logging.info(f"Weather Information: {weather_info}")
        return weather_info
    else:
        logging.warning("City Not Found while fetching weather information.")
        return "City Not Found"