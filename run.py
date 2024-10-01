import transcribe
import modules
import python_weather
import asyncio
import os
import paho.mqtt.client as mqtt



global query, splitList, module



def get_query():
    global query 
    query = transcribe.linux_transcribe()

def splitAndID():
    global query, module
    splitList = query.split()
    if ("light" in splitList) or ("lights" in splitList):
        module = "light"
        print("light")
        modules.lights(splitList)
    if ("temperature" in splitList) or ("temp" in splitList):
        module = "temp"
    if ("door" in splitList) or ("lock" in splitList):
        module = "lock"
        modules.lock(splitList)
    if ("weather" in splitList):
        module = "weather"
        getWeather()
    

async def getWeather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
        weather = await client.get('New York')
        print(weather.temperature)
        return weather.forecast

get_query()
splitAndID()
print(query + module)