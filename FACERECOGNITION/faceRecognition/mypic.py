from PIL import Image

img = Image.open('1111.jpg')  

img_resize = img.resize((64, 64))
img_resize.save('11111.jpg')