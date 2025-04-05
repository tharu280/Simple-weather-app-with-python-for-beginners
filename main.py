import requests
import json


class WeatherApp:
    def __init__(self, api_key):

        self.api_key = api_key
        self.url = "http://api.weatherapi.com/v1/current.json"

    def weather_get(self, city):

        params = {
            'key': self.api_key,
            'q': city,
            'aqi': 'no'
        }

        try:
            response = requests.get(self.url, params=params)
            data = response.json()

            location = data['location']['name']
            country = data['location']['country']
            temp_c = data['current']['temp_c']
            condition = data['current']['condition']['text']

            print(f"📍 {location}, {country}")
            print(f"🌡️ {temp_c}°C — {condition}")
            return True

        except requests.exceptions.RequestException as e:
            print("⚠️ Network or request error:", e)
            return False

        except KeyError:
            print("❌ Couldn't find weather data for that location. Try another city.")
            return False

        except json.decoder.JSONDecodeError:
            print("🛑 Error decoding response. The API might be down or returning invalid JSON.")
            return False

        except Exception as e:
            print("❗ Something unexpected happened:", e)
            return False

    def run(self):

        while True:
            city = input('Enter your city name: ')
            success = self.weather_get(city)
            if success:
                break
            else:
                print("Please try again.")


api_key = ""
app = WeatherApp(api_key)
app.run()
