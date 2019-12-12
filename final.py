import requests
from PIL import Image, ImageDraw, ImageFont

im = Image.open('tacos-unsplash.jpg')

width = im.width
height = im.height

print(width, height)





taco_data = 'https://taco-1150.herokuapp.com/random/?full_taco=true'  # requesting data from url
response = requests.get(taco_data)

if not response:
    print('page you requested cannot be found')  # checking if data is available
    quit()

response_json = response.json()  # this will bring back a dictionary of variables, of keys and ingredients

print('printing the name of the seasoning:')  # returning name of seasoning
print(response_json['seasoning']['name'])
print('printing the recipe of the seasoning:')
print(response_json['seasoning']['recipe'])  # return recipe to seasoning


# use this if you want to view all of the data / to see what the keys are
"""
for first_key in response_json.keys(): 
    item = response_json[first_key]
    for second_key in item.keys()
    print(f'--------------------------------')
    print(f'[{first_key}][{second_key}]')
    print(f'--------------------------------')
    print(item[second_key])
    print()
"""