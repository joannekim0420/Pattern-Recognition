import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

img=cv2.imread('hand.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height = img.shape[0]
width = img.shape[1]
print(height, width)
plt.figure(figsize=(10, 5))
plt.subplot(1,3,1)
plt.imshow(img)
plt.axis('off')
plt.title('original')

center = (width/2, height/2)
cv_M = cv2.getRotationMatrix2D(center, 90, 1.0)
cv_result = cv2.warpAffine(img, cv_M, (width, height))
print(cv_M, end='\n\n')

plt.subplot(1,3,2)
plt.imshow(cv_result)
plt.axis('off')
plt.title('cv_result')

#my_M

y = (width-height)/2
#print(y)
x = -(width-y)
#print(x)
M1 = np.array([[math.cos(math.radians(-90)), -math.sin(math.radians(-90))],
               [math.sin(math.radians(-90)), math.cos(math.radians(-90))]]) #회전행렬
M2 = np.array([[1, 0, x],
              [0, 1, y]]) #이동행렬
my_M = np.matmul(M1, M2)

print('>>My matrix')
print(my_M)

##correct code

fwd_tran_M = np.array([[1,0,-center[0]],
                      [0,1,-center[1]],
                      [0,0,1]])

rot_M = np.array([[0,1,0],
                      [-1,0,0],
                      [0,0,1]])

bwd_tran_M = np.array([[1,0,center[0]],
                      [0,1,center[1]],
                      [0,0,1]])

tmp = np.matmul(rot_M, fwd_tran_M)
my_M = np.matmul(bwd_tran_M)
my_M = my_M[:2, ] #=my_M[0:2, 0:3]

my_result=cv2.warpAffine(img, my_M, (width, height))

plt.subplot(1,3,3)
plt.imshow(my_result)
plt.axis('off')
plt.title('my_result')

plt.tight_layout()
plt.show()