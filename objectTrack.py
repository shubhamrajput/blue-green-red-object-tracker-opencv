import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()   #Take each frame
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #Convert from BGR to HSV
    #range for blue color in HSV

    #calculations:
    #blue = np.uint8([[[255,0,0 ]]])
    #hsv_blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
    
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])

    #range for green color in HSV

    #calculations:
    #green = np.uint8([[[0,255,0 ]]])
    #hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    lower_green=np.array([50,50,50])             
    upper_green=np.array([70,255,255])

    #calculations:
    #red = np.uint8([[[0,0,255 ]]])
    #hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0, 50, 50])             
    upper_red=np.array([10, 255, 255])

    #Threshold the HSV image to get only blue color
    mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)

    #Threshold the HSV image to get only green color
    mask_green=cv2.inRange(hsv,lower_green,upper_green)

    #Threshold the HSV image to get only red color
    mask_red=cv2.inRange(hsv,lower_red,upper_red)

    #Bitwise-AND mask and original image
    res_blue=cv2.bitwise_and(frame,frame,mask=mask_blue)
    res_green=cv2.bitwise_and(frame,frame,mask=mask_green)
    res_red=cv2.bitwise_and(frame,frame,mask=mask_red)


    #Show the images

    cv2.imshow('Original',frame)
    cv2.imshow('Mask_BLUE',mask_blue)
    cv2.imshow('Result Blue',res_blue)
    #cv2.imshow('Mask_GREEN',mask_green)
    #cv2.imshow('Result GREEN',res_green)
    #cv2.imshow('Mask_RED',mask_red)
    #cv2.imshow('Result RED',res_red)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
