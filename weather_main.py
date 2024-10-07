
# Import class
from weather_forecast import WeatherForcast

# Write main script
def main():
    weather_app = WeatherForcast()
    while True:
        try:
            city = input("Enter a city to get its weather forecast, or 'exit' to quit: ")
            if city.lower() == "exit":
                break
            weather_app.display_weather(city)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()