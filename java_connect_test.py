from PIL import Image
import requests
from io import BytesIO

# https://medimedi.s3.ap-northeast-2.amazonaws.com/83542989.jfif
urlFromJava = input()
response = requests.get(urlFromJava)
img = Image.open(BytesIO(response.content))
img.show()
print("success")
