import requests
from PIL import Image, ImageDraw, ImageFont

im = Image.open('tacos-unsplash.jpg')  # this open my image
width = im.width  # requesting the height and width of my original photo, and storing data
height = im.height

print(width, height)  # preserving the aspect ratio

half_height = int(height / 2)  # i am reducing the size of my image
half_width = int(width / 2)  # i am saving the changes to my resized images

half_size = im.resize((half_width, half_height))
half_size.show()
half_size.save('half_size_taco.jpg')



im_draw = ImageDraw.Draw(im)

# font = ImageFont.truetype('DejaVuSans.ttf', 100)
# im_draw.text([640, 790, ], 'Random Taco Cookbook', fill='black', font=font)
# smaller_im.show()


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
