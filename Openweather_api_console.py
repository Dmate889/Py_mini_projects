import requests

api_key = "2151d7e178017e10631556b4da476ae1"

def input_selector():
    print("Please provide a city name: ")
    city = input()
    return city

def fetch_open_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Could not fetch url: {url}")

def match_case_selector():
    print("Please provide the number for type of weather data you need:"
          "\n1. Current temperature\n"
          "2. How it feels like\n"
          "3. Minimum temperature\n"
          "4. Maximum temperature\n")

    data = input()

    match data:
        case "1":
            return 'temp'
        case "2":
            return 'feels_like'
        case "3":
            return 'temp_min'
        case "4":
            return 'temp_max'


def main():

    is_running = True

    while is_running:
        print("=============================================")
        print("Welcome to the Python OpenWeather Console application")
        print("=============================================")
        print("Press 1. for weather data")
        print("Press 2. for exit")
        user_input = input()

        if user_input == "1":
           city =  input_selector()
           data = match_case_selector()
           weather_data = fetch_open_weather(city)
           if weather_data:
                print(f"{city}: {weather_data['main'][data]} Celsius")
           else:
                print("Could not fetch weather data. Please check city name")
        elif user_input == "2":
            is_running = False
            print("Have a nice day!")
        else:
            print("Wrong input, please try again")


if __name__ == "__main__":
    main()
