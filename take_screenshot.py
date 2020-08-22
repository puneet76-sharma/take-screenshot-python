# pip install opencv-python
# pip install pyautogui


import numpy as np
import cv2
import pyautogui as py


input("enter any key for screenshot")
image= py.screenshot() 

image= cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# writing it to the disk using opencv

cv2.imwrite("image.png", image)

input()