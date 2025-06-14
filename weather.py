from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
def getcurrentweather(city="Bangalore"):
    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data=requests.get(request_url).json()
    return weather_data

if __name__=="__main__":
    print("\n*** Get Current Weather Conditions ***")
    city=input("Enter a city : \n") 
    if not bool(city.strip()):
        city="Bangalore"
    weather_data=getcurrentweather(city)
    
    pprint(weather_data)