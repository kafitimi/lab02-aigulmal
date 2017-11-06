from PIL import Image
import numpy as np
img = Image.open('darwin.jpg')
img.load()
print(img.size)
print(img.mode)
data = img.getdata()
print(data[0])
a = np.array(img, dtype=np.uint8)
