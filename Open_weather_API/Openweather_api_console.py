import weather_data_methods as wd

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
           city =  wd.input_selector()
           data = wd.match_case_selector()
           weather_data = wd.fetch_open_weather(city)
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
