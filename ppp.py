import tesserocr
import os
image time
from PIL import Image
image=Image.open('test5.png')
image=image.convert("L")
threshold=125
table=[]
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
test=tesserocr.image_to_text(image)
print(test.strip())