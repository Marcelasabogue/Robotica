import cv2
import numpy as np


vcap = cv2.VideoCapture('video.avi') # 0=camera
if vcap.isOpened(): 
    # get vcap property 
    width  = vcap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)   # float `width`
    height = vcap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)  # float `height`
    # or
    width  = vcap.get(3)  # float `width`
    height = vcap.get(4)  # float `height`

    # it gives me 0.0 :/
    fps = vcap.get(cv2.cv.CV_CAP_PROP_FPS)
    print(width)
    print(height)
a=4
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
  # Color
    if a==1:
     low_red = np.array([0, 100, 74])
     high_red = np.array([0, 255, 255])
     red_mask = cv2.inRange(hsv_frame, low_red, high_red)
     color = cv2.bitwise_and(frame, frame, mask=red_mask)
     se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
     se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
     mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, se1)
     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)
    elif a==2:
    # --------Color azul
     low_blue = np.array([110, 50, 50])
     high_blue = np.array([130, 255, 255])
     blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
     color = cv2.bitwise_and(frame, frame, mask=blue_mask)
     se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
     se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
     mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, se1)
     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)
    else:
    # -----Color amarillo
     low_green = np.array([20, 80, 80])
     high_green = np.array([30, 255, 255])
     green_mask = cv2.inRange(hsv_frame, low_green, high_green)
     color = cv2.bitwise_and(frame, frame, mask=green_mask)
     se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
     se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
     mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, se1)
     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)
        
    M = cv2.moments(mask)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("Image", frame)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", color)
    cv2.imshow("mascara", mask)
    #cv2.imshow("Blue", blue)
    #cv2.imshow("Green", green)
    #cv2.imshow("Result", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
      

