import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./data/input.png',1)

def change(img):
    # ret,thresh = cv.threshold(img,180,255,cv.THRESH_BINARY)
    ret,thresh = cv.threshold(img,200,200,200)
    return thresh


def make_line(img, threshold):
    print(img.shape)
    h, w, channels = img.shape

    # define detect line
    middle_line = {}
    line = {}
    for i in range(int(h)):
        temp = []
        for j in range(w):
            if np.sum(img[i][j]) > threshold:
                # print("i {}, j {}".format(i,j),end="|")
                temp.append(j)
                break
        for j in range(j+1, w):
            if np.sum(img[i][j]) < threshold:
                # print("i {}, j {}".format(i, j), end="|")
                # img[i, j-1:j+1] = [255, 254, 59]
                temp.append(j)
                break
        for j in range(j+1, w):
            if np.sum(img[i][j]) > threshold:
                # print("i {}, j {}".format(i, j), end="|")
                # img[i, j-1:j+1] = [255, 254, 59]
                temp.append(j)
                break
        for j in range(j+1, w):
            if np.sum(img[i][j]) < threshold:
                # print("i {}, j {}".format(i, j))
                # img[i, j-1:j+1] = [255, 254, 59]
                temp.append(j)
                break
        if len(temp) == 4:
            line[i] = temp
            middle = int((temp[0]+temp[3])/2)
            middle_line[i] = middle
        else:
            line[i] = 0
            middle_line[i] = 0
    return middle_line, line

binary_img = change(img)
h,w,channels = binary_img.shape
# binary_img = binary_img[int(h/2):h,:]

middle_line, line = make_line(binary_img,300)

i = 40
while(i<h-40):
    if line[i] is not 0:
        for j in line[i]:
            img[i-2:i+2, j-2:j+2] = [255, 254, 59]
    if middle_line[i] is not 0:
        j = middle_line[i]
        img[i-2:i+2,j-2:j+2] = [0,255,0]
    i += 10

k = 0
estimate_line = []
i = int(h/2)
while(k<3):
    print(i)
    if middle_line[i]!=0:
        j = middle_line[i]
        img[i-2:i+2, j-2:j+2] = [0, 0, 255]
        estimate_line.append({
            "i":i,
            "j":j
        })
        k+=1
        if i+40<h:
            i+=40
    else:
        i+=1

print(estimate_line)

titles = ['Original Image', 'BINARY']
images = [img,binary_img]

cv.imwrite("./data/output2.png", img)


for i in range(len(images)):
    plt.subplot(2, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

