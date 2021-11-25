import cv2
import numpy as np
arr_x = []
arr_y = []

for i in range(12):
    for j in range(10000,10185):

        filepath = "image/{}_{}.png".format(i,j)
        img = cv2.imread(filepath, cv2.IMREAD_COLOR)
        # cv2.imshow('Gray', img)
        print("i",i,"j",j)
        arr_x.append(img)
        arr_y.append(i)



arrx_n = np.array(arr_x)
arry_n = np.array(arr_y)
print(arrx_n.shape)
print(arry_n.shape)
np.save("x_train",arrx_n)
np.save("y_train",arry_n)

cv2.waitKey(0)
cv2.destroyAllWindows()