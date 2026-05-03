import requests

API_KEY = "Enter Your API_KEY"
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
        
        print("\n" + "="*35)
        print(f"  {city_name}, {country}")
        print("="*35)
        print(f"  Temperature  : {temp}°C")
        print(f"  Feels like   : {feels_like}°C")
        print(f"  Condition    : {condition.capitalize()}")
        print(f"  Humidity     : {humidity}%")
        print(f"  Wind speed   : {wind_speed} m/s")
        print("="*35 + "\n")
    
    elif response.status_code == 404:
        print(f"\n[Error] '{city}' City Not found.\nPlease Enter Valid City Name\n-----------------------------")


def main():
    print("\n=== Python Weather App ===")
    print(" ")
    while True:
        city = input("Enter Your City Name:\n> ").strip()

        if city.lower() == 'q':
            print("Bye!")
            break
        if city:
            get_weather(city)
            print("If want quit press 'q'. ")

if __name__ == "__main__":
    main()
