import requests

API_KEY = "Enter YOUR_API"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",   
        "lang": "en"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        city_name   = data["name"]
        country     = data["sys"]["country"]
        temp        = data["main"]["temp"]
        feels_like  = data["main"]["feels_like"]
        humidity    = data["main"]["humidity"]
        condition   = data["weather"][0]["description"]
        wind_speed  = data["wind"]["speed"]
        
        print("=================================")
        print(f"       {city_name}, {country}        ")
        print("=================================")
        print(f"  Temperature  : {temp}°C")
        print(f"  Feels like   : {feels_like}°C")
        print(f"  Condition    : {condition.capitalize()}")
        print(f"  Humidity     : {humidity}%")
        print(f"  Wind speed   : {wind_speed} m/s")
        print("================================")
    
    elif response.status_code == 404:
        print(f"\n[Error] '{city}' City Not found.\nPlease Enter Valid City Name\n-----------------------------")


def main():
    print("=================================")
    print("         Python Weather App")
    print("=================================")
    print(" ")
    print("If want quit press 'q'.\n")
    while True:
        city = input("Enter Your City Name:\n> ").strip()

        if city.lower() == 'q':
            print("Bye!")
            break
        if city:
            get_weather(city)
            break

if __name__ == "__main__":
    main()
