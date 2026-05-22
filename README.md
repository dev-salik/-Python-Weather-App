# 🌤️ Python Weather App

A simple command-line weather app built with Python that shows real-time weather data for any city.

## Features
- Current temperature & feels like
- Weather condition (sunny, cloudy, etc.)
- Humidity & wind speed
- Supports any city worldwide

## Requirements
```
  pip install requests

```

## Setup

1. Clone the repo
   git clone https://github.com/dev-salik/-Python-Weather-App.git
   cd -Pyhton-Weather-App


2. Add your API key
   - Get a free key from https://openweathermap.org/api
   - Open `weather.py` and replace `YOUR_API_KEY` with your key

3. Run the app
   python weather.py

## Usage
Enter any city name when prompted.
Type 'q' to quit.

## Sample Output
```
===================================
  Mumbai, IN
===================================
  Temperature  : 31°C
  Feels like   : 35°C
  Condition    : Haze
  Humidity     : 72%
  Wind speed   : 3.5 m/s
===================================
```

## Built With
- Python
- OpenWeatherMap API
