# -*- coding: utf-8 -*-
import cv2
import time

def neighbours(x, y, image):
    '''Return 8-neighbours of point p1 of picture, in order'''
    i = image
    x1, y1, x_1, y_1 = x+1, y-1, x-1, y+1
    #print ((x,y))
    return [i[y1][x],  i[y1][x1],   i[y][x1],  i[y_1][x1],  # P2,P3,P4,P5
            i[y_1][x], i[y_1][x_1], i[y][x_1], i[y1][x_1]]  # P6,P7,P8,P9

def transitions(neighbours):
    n = neighbours + neighbours[0:1]    # P2, ... P9, P2
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))

def zhangSuen(image):
    changing1 = changing2 = [(-1, -1)]
    
    counter = 0
    
    while changing1 or changing2:
        counter = counter + 1
        
        if counter > 20:
            break
        # Step 1
        changing1 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, image)
                if (image[y][x] == 1 and    # (Condition 0)
                    P4 * P6 * P8 == 0 and   # Condition 4
                    P2 * P4 * P6 == 0 and   # Condition 3
                    transitions(n) == 1 and # Condition 2
                    2 <= sum(n) <= 6):      # Condition 1
                    changing1.append((x,y))
                    #print(x,y)
        for x, y in changing1: image[y][x] = 0
        # Step 2
        print('step2')
        changing2 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, image)
                if (image[y][x] == 1 and    # (Condition 0)
                    P2 * P6 * P8 == 0 and   # Condition 4
                    P2 * P4 * P8 == 0 and   # Condition 3
                    transitions(n) == 1 and # Condition 2
                    2 <= sum(n) <= 6):      # Condition 1
                    changing2.append((x,y))
                    
                   # print(x,y)
                    
        for x, y in changing2: image[y][x] = 0
        #print changing1
        #print changing2
    return image




img = cv2.imread('2.jpg', 0)

print(img)

ret, thresh = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY_INV)
print(ret,'------>')

print(thresh, '------------>')

print(thresh)

image = zhangSuen(thresh)

print(image)

#ret1, res = cv2.threshold(image, 255, 1, cv2.THRESH_BINARY_INV)

res = image.copy()
for y in range(1, len(image) - 1):
	for x in range(1, len(image[0]) - 1):
		if image[y][x] == 1:
			res[y][x] = 0
		else:
			res[y][x] =1


cv2.imshow('dst', image*255)

cv2.imwrite('4-10a.jpg', res*255)

cv2.imwrite('4-10b.jpg', image*255)
