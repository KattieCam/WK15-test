import requests
from PIL import Image

taco_data = 'https://taco-1150.herokuapp.com/random/?full_taco=true'  # requesting data from url
response = requests.get(taco_data)

if not response:
    print('page you requested cannot be found')  # checking if data is useable
    quit()

response_json = response.json()
for key in response_json.keys():
    print(f'key = {key}')
    print(response_json[key])
    print()
