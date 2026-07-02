from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage, ToolMessage
from langchain_mistralai import ChatMistralAI
from tavily import TavilyClient
from langchain.tools import tool
import os
from rich import print
import requests
import json



API_KEY = os.getenv("OPENWEATHER_API_KEY") 


@tool
def weather(city: str):
    "Return the weather of the given city" #Docstring
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    res = requests.get(base_url)
    data = res.json()
    # print(json.dumps(data, indent=4))



    if res.status_code != 200:
        return f"{data.get('message', "Something went wrong")}"
    
    city = city,
    temperature = data["main"]["temp"]
    desp = data["weather"][0]["description"]
    temp_max = data["main"]["temp_max"]
    temp_min = data["main"]["temp_min"]
    wind_speed = data["wind"]["speed"]

    return {
        "city": city,
        "temperature": temperature,
        "temp_max": temp_max,
        "temp_min": temp_min,
        "desp": desp,
        "wind_speed": wind_speed
    }
print()
print("**********************WEATHER************************")
print()
print(weather.invoke("delhi"))
print()
print()




model = ChatMistralAI(model = "mistral-medium-2508").bind_tools([weather])
