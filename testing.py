# import torch
# from TTS.api import TTS

# # Get device
# device = "cuda" if torch.cuda.is_available() else "cpu"

# # Init TTS
# tts = TTS("tts_models/en/sam/tacotron-DDC").to(device)

# # Run TTS
# # Text to speech list of amplitude values as output
# wav = tts.tts_to_file(text="Hello world! How are you doing on this fine day?", file_path="output.wav")
    
import python_weather

import asyncio
import os

# Get rid of async
async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Harrisonburg, VA')

    # returns the current day's forecast temperature (int)
    temp = weather.feels_like
    cloud = weather.description
    rain = weather.precipitation

    if (rain <= 0.5):
        rain = "Low to no rain"
    print(temp, cloud, rain)

    # Works for curr weather
    # Add stuff for daily and hourly

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

  asyncio.run(getweather())