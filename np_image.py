import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image 
import requests  
from io import BytesIO

def load_image_from_url(url):
    response=requests.get(url)
    return Image.open(BytesIO(response.content)) 
shiva_url="https://5.imimg.com/data5/SELLER/Default/2023/3/MK/KV/VK/121932234/2-adiyogi-13-16-inch-5-jpg.jpg"
shiva=load_image_from_url(shiva_url)

#display original image
plt.figure(figsize=(8,4))
plt.imshow(shiva)
plt.title("Shiva")
plt.axis('off')
plt.show()

#image to array
shiva_np=np.array(shiva)
print('Elephant Image shape',shiva_np.shape)
 
#grayscale image
shiva_gray=shiva.convert("L")
plt.figure(figsize=(6,6))
plt.imshow(shiva_gray,cmap='gray')
plt.title("Shiva(grayscale)")
plt.axis('off')
plt.show()

#pink scale image
shiva_red=shiva.convert("L")
plt.figure(figsize=(6,6))
plt.imshow(shiva_red,cmap='pink')
plt.title("Shiva(pink)")
plt.axis('off')
plt.show()

