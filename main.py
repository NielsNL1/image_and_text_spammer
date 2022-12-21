# imports libraries
from PIL import Image
import requests
from io import BytesIO


# allows the user to choose with image and text they want spammed
url = input('copy the URL of the image')
text = input('Type the text you want')


# gets the URL image and defines image_spam
def image_spam():
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


# creates the infinite loop
while True:
    print(text)
    print(image_spam)
