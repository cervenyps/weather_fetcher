import requests

CITIES = ["New York", "Vancouver", "London", "Tokyo", "Amsterdam"]

def fetch_temperature(city: str) -> float:
    """Fetch the temperature for a given city in Celsius using wttr.in."""
    url = f"http://wttr.in/{city}?format=%t"
    response = requests.get(url)
    temperature = response.text.strip()
    return float(temperature.replace("+", "").replace("°C", "").strip())

def get_temperatures() -> dict:
    """Fetch the temperature for all specified cities."""
    temperatures = {}
    for city in CITIES:
        try:
            temp = fetch_temperature(city)
            temperatures[city] = temp
        except Exception as e:
            temperatures[city] = str(e)
    return temperatures
