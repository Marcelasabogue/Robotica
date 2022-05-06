import cv2
import numpy as np

import cv2

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

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # Red color
    low_red = np.array([0, 93, 0])
    high_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
    se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
    mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, se1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)
    # --------Blue color
    #low_blue = np.array([94, 80, 2])
    #high_blue = np.array([126, 255, 255])
    #blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    #blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    # -----Green color
    #low_green = np.array([25, 52, 72])
    #high_green = np.array([102, 255, 255])
    #green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    #green = cv2.bitwise_and(frame, frame, mask=green_mask)
    # Every color except white
    #low = np.array([0, 42, 0])
    #high = np.array([179, 255, 255])
    #mask = cv2.inRange(hsv_frame, low, high)
    #result = cv2.bitwise_and(frame, frame, mask=mask)
    #anotacion
    #img=np.zeros((180,320,3),np.uint8)
    #anotacion = cv2.circle(img,(256,256),63, (255,255,255), -1)
    #cv2.imshow("Anotacion",anotacion)
    #interseccion = anotacion + red_mask > 1
    #union = anotacion + red_mask > 0
    #jaccard = np.sum(interseccion) / np.sum(union)
    #print(jaccard)
    #print(red_mask)
    
    M = cv2.moments(red_mask)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(frame, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("Image", frame)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Red", mask)
    #cv2.imshow("Blue", blue)
    #cv2.imshow("Green", green)
    #cv2.imshow("Result", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
      

