import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

threshold = 100
def make_line(img):
    print(img.shape)
    h,w,channels = img.shape

    # define detect line
    line = {}
    for i in range(int(h)):
        temp = []
        for j in range(w):
            if np.sum(img[i][j]) > threshold*3:
                # print("i {}, j {}".format(i,j),end="|")
                img[i, j-1:j+1] = [255, 254, 59]
                temp.append(j)
                break
        for j in range(j+1,w):
            if np.sum(img[i][j]) < threshold*3:
                # print("i {}, j {}".format(i, j), end="|")
                img[i, j-1:j+1] = [255, 254, 59]
                temp.append(j)
                break
        for j in range(j+1,w):
            if np.sum(img[i][j]) > threshold*3:
                # print("i {}, j {}".format(i, j), end="|")
                img[i, j-1:j+1] = [255, 254, 59]
                temp.append(j)
                break
        for j in range(j+1,w):
            if np.sum(img[i][j]) < threshold*3:
                # print("i {}, j {}".format(i, j))
                img[i, j-1:j+1] = [255, 254, 59]
                temp.append(j)
                break
        line[i] = temp

    return line

   
img = cv.imread('output.png', 1)
line = make_line(img)

h,w,channel = img.shape

for i in {int(h/2), int(h/2-50), int(h/2+50)}:
    temp = line[i]
    if len(temp) == 4:
        middle = int((temp[0]+temp[3])/2)
        img[i][middle-1:middle+1] = [0, 255, 0]

cv.imwrite("test2.png", img)
cv.imshow('test', img)

