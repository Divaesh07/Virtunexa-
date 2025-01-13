import requests
import tkinter as tk
from tkinter import messagebox

def get_weather_data(city, api_key):
    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    
    if data:
        city = data.get('name')
        country = data['sys'].get('country')
        temp = data['main'].get('temp')
        humidity = data['main'].get('humidity')
        wind_speed = data['wind'].get('speed')

        return (f"Weather in {city}, {country}:\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s")
    else:
        return "check the city name or try again later."

def fetch_weather():
    
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather_data = get_weather_data(city, api_key)
    result = display_weather(weather_data)
    result_label.config(text=result)

def main():
    
    global city_entry, result_label, api_key

    #openweathermap API key
    api_key = "7cec851fb045513a7705afc710630797" 

    
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("400x300")

    
    tk.Label(root, text="Enter city name:").pack(pady=10)

    city_entry = tk.Entry(root, width=30)
    city_entry.pack(pady=5)

    fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
    fetch_button.pack(pady=10)

    result_label = tk.Label(root, text="", justify="left")
    result_label.pack(pady=10)

    
    root.mainloop()

if __name__ == "__main__":
    main()
