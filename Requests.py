import requests
import os
os.system('cls')

r = requests.get('https://httpbin.org/delay/4', timeout=3)

print(r)
