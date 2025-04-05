# Simple Python Weather Application for Beginners with error handling

This is a simple weather application built with Python. It allows users to input a city name and fetch real-time weather data from the [WeatherAPI](https://www.weatherapi.com/). The app features basic error handling and uses an Object-Oriented Programming (OOP) approach, making it a great practice project for beginners.

### Features:
- Fetches weather data (location, temperature, and weather condition) based on the city input by the user.
- Includes error handling to manage network issues, invalid city names, and other unexpected situations.
- Provides a user-friendly interface to try again if something goes wrong.
- Implements Object-Oriented Programming (OOP) principles with `class`, `self`, `__init__()`, and `super()`.

---

## Installation

To run the weather application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/simple-python-weather-app.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd simple-python-weather-app
   ```

3. **Install the required dependencies:**

   This project uses the `requests` library to make API requests. You can install it using `pip`:

   ```bash
   pip install requests
   ```

---

## How to Use

1. **Get an API Key:**

   To use this weather app, you need to obtain an API key from [WeatherAPI](https://www.weatherapi.com/). Once you sign up and get your API key, replace the `api_key` variable in the code with your own key.

2. **Run the Program:**

   After installing the dependencies and setting up the API key, run the application:

   ```bash
   python weather_app.py
   ```

3. **Enter the city name:**

   The app will ask you to enter a city name. Type the name of any city to fetch its current weather.

   Example:
   ```
   Enter your city name: London
   📍 London, United Kingdom
   🌡️ 15°C — Partly cloudy
   ```

4. **Error Handling:**

   If the city name is incorrect or there is a network issue, the program will print an error message and allow you to try again.

---

## Code Structure

The application is structured using Object-Oriented Programming principles, with the following key components:

- **`WeatherApp` Class:** The main class containing methods for initializing the app, making the API request, and handling the response.
  - **`__init__(self, api_key)`**: Initializes the application with the provided API key.
  - **`weather_get(self, city)`**: Fetches and displays weather data for the specified city. Handles exceptions such as invalid city names, network issues, and API response errors.
  - **`run(self)`**: Keeps prompting the user for a city name until valid weather data is returned.

---

## Example Output

```bash
Enter your city name: London
📍 London, United Kingdom
🌡️ 15°C — Partly cloudy
```

---

## Error Handling

This application includes the following error handling:

1. **Network Errors**: If the app encounters any issue during the API request (e.g., network failure), it will display an error message and retry the request.
   
2. **Invalid City Name**: If the city is not found in the WeatherAPI database, the app will inform the user and ask for another city name.

3. **Invalid API Response**: If the API returns an invalid or corrupted response, the app will handle it gracefully.

---

## Contribution

Feel free to fork this repository and make improvements. If you find any bugs or want to add new features (such as temperature unit conversion, extended weather information, etc.), create a pull request, and I’ll review it!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you need anything else!
