import requests
from PIL import Image

taco_data = 'https://taco-1150.herokuapp.com/random/?full_taco=true'  # requesting data from url
response = requests.get(taco_data)

if not response:
    print('page you requested cannot be found')  # checking if data is usable
    quit()

response_json = response.json()  # this will bring back a dictionary of variables, of keys and ingredients

print('printing the name of the seasoning:')
print(response_json['seasoning']['name'])
print('printing the recipe of the seasoning:')
print(response_json['seasoning']['recipe'])

"""
for key in response_json.keys(): # for use if needed to run all data
    print(f'key = {key}')
    print(response_json[key])
    print()
"""