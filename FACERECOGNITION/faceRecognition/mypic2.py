import cv2
from PIL import Image

 
img = cv2.imread('1234.jpg', cv2.IMREAD_COLOR)
 
img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

img90.open('1234.jpg', mode = 'r')
