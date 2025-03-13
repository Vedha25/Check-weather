import requests
import json
import os

city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(f'The current weather in {city} is {w} degrees')
os.system(f"say 'The current weather in {city} is {w} degrees'")
