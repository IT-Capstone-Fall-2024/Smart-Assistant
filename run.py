import transcribe
import python_weather
import asyncio
import os
import 


global query, splitList, module

def get_query():
    query = linux_transcribe()

def splitAndID():
    splitList = query.split()
    if (light in splitList) or (lights in splitList):
        module = "light"
    if (temperature in splitList) or (temp in splitList):
        module = "temp"
    if (door in splitList) or (lock in splitList):
        module = "lock"
    if (weather in splitList):
        module = "weather"
        getWeather()
    

async def getWeather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
        weather = await client.get('New York')
        print(weather.temperature)
        return weather.forecast

