#use a white glove for this (I'll improve this)
#use the console for this...
#install cv2 (pip install opencv-python)
#install sklearn : pip install scikit-learn 

import cv2
import numpy as np
from sklearn.metrics import pairwise

cap = cv2.VideoCapture(0)

kernelOpen =np.ones((5,5))
kernelClose = np.ones((20,20))
lb = np.array([20,100,100])
ub = np.array([120,255,255])
while True:
  ret, frame = cap.read()
  flipped = cv2.flip(frame, 1)
  flipped = cv2.resize(flipped,(500,400))

  imSeg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  imSegFlipped = cv2.flip(imSeg, 1)
  imSegFlipped = cv2.resize(imSegFlipped,(500,400))
#so we create a mask var
#and also a maskOpen and close var
  
  mask = cv2.inRange(imSegFlipped, lb , ub)
  mask = cv2.resize(mask,(500, 400))

  maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
  maskOpen = cv2.resize(maskOpen,(500,400))
  maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)
  maskClose = cv2.resize(maskClose,(500,400))

  final = maskClose
  conts, h =cv2.findContours(maskClose,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#contour area process (marge)
#ok this part is quite sick coz you need to create a lot of var...its quite annoying tbh
  if(len(conts)!=0):
    b = max(conts, key=cv2.contourArea)
    west = tuple(b[b[:, :, 0].argmin()][0])
    east = tuple(b[b[:, :, 0].argmax()][0])
    north = tuple(b[b[:, :, 1].argmin()][0])
    south = tuple(b[b[:, :, 1].argmax()][0])
    centre_x = (west[0]+east[0])/2
    centre_y = (north[0]+south[0])/2

    cv2.drawContours(flipped, b, -1, (0,255,0), 3)
    cv2.circle(flipped, west, 6, (0,0,255), -1)
    cv2.circle(flipped, east, 6, (0,0,255), -1)
    cv2.circle(flipped, north, 6, (0,0,255), -1)
    cv2.circle(flipped, south, 6, (0,0,255), -1)
    cv2.circle(flipped, (int(centre_x),int(centre_y)), 6, (255,0,0), -1)

  cv2.imshow('video', flipped)
  if cv2.waitKey(1) & 0xFF == ord(' '):
    break


cap.release()
cv2.destroyAllWindows()
