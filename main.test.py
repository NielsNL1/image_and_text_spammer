# imports libraries
from PIL import Image
import requests
from io import BytesIO

# defines URL
url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2F7ZX9JMY_k2E%2Fmaxresdefault.jpg" \
      "&f=1&nofb=1&ipt=fb9279e17f046cf240011cbb1ee03ee33adf1c7ff5574e62035d006c270cbf6b&ipo=images "


# gets the URL image and defines image_spam
def image_spam():
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


# creates the infinite loop
while True:
    print('test')
    print(image_spam)
