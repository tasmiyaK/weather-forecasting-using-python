import requests
import json
import argparse

def get_weather(city, units='metric'):
    api_key = '679a36fb4afd0a66a02687c05e51e2a8'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': units}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def parse_weather(data):
    weather = data['weather'][0]
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    #dew_point = data['main']['dew_point']
    clouds = data['clouds']['all']
    visibility = data['visibility']
    wind_speed = data['wind']['speed']
    wind_gust = data['wind'].get('gust')
    wind_deg = data['wind']['deg']
    uvi = data.get('uvi')
    rain_1h = data.get('rain', {}).get('1h', 0)
    snow_1h = data.get('snow', {}).get('1h', 0)
    weather_desc = weather['description']
    weather_icon = weather['icon']
    return temperature, feels_like, pressure, humidity, clouds, visibility, wind_speed, wind_gust, wind_deg, uvi, rain_1h, snow_1h, weather_desc, weather_icon

def main():
    parser = argparse.ArgumentParser(description='Get current weather forecast')
    parser.add_argument('city', type=str, help='City name')
    parser.add_argument('--units', type=str, default='metric', choices=['metric', 'imperial'], help='Units of measurement: metric or imperial')
    args = parser.parse_args()

    city = args.city
    units = args.units

    weather_data = get_weather(city, units)
    if weather_data['cod'] == 200:
        temperature, feels_like, pressure, humidity, clouds, visibility, wind_speed, wind_gust, wind_deg, uvi, rain_1h, snow_1h, weather_desc, weather_icon = parse_weather(weather_data)

        print(f'Weather forecast for {city}:')
        print(f'Temperature: {temperature}°{units.upper()}')
        print(f'Feels Like: {feels_like}°{units.upper()}')
        print(f'Pressure: {pressure} hPa')
        print(f'Humidity: {humidity}%')
        #print(f'Dew Point: {dew_point}°{units.upper()}')
        print(f'Cloudiness: {clouds}%')
        print(f'Visibility: {visibility} meters')
        print(f'Wind Speed: {wind_speed} {units}/sec')
        if wind_gust:
            print(f'Wind Gust: {wind_gust} {units}/sec')
        print(f'Wind Direction: {wind_deg}°')
        if uvi:
            print(f'UV Index: {uvi}')
        print(f'Rain (last 1 hour): {rain_1h} mm')
        print(f'Snow (last 1 hour): {snow_1h} mm')
        print(f'Weather Description: {weather_desc}')
        print(f'Weather Icon: http://openweathermap.org/img/wn/{weather_icon}.png')
    else:
        print('Failed to fetch weather data.')

if __name__ == '__main__':
    main()
