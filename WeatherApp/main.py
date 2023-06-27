import requests
import json
import os
import win32com.client as wincom

city = input("Enter the name of thr city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=7a7f18c90be246dfbd2200219232506&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w = wdic['current']['temp_c']

speak = wincom.Dispatch("SAPI.SpVoice")
text = "say 'the current weather in {city} is {w} degrees"
speak.Speak(text)