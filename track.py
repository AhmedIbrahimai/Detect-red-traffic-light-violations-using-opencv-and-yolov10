import time
import numpy as np
import cv2


cap=cv2.VideoCapture('tr.mp4')

def nothing(x):
    pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)


while True:
     ret,frame=cap.read()
     if not ret:
        # If the video reaches the end, rewind it to the start
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

     frame=cv2.resize(frame,(1020,600))
     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
     l_h = cv2.getTrackbarPos("L - H", "Trackbars")
     l_s = cv2.getTrackbarPos("L - S", "Trackbars")
     l_v = cv2.getTrackbarPos("L - V", "Trackbars")
     u_h = cv2.getTrackbarPos("U - H", "Trackbars")
     u_s = cv2.getTrackbarPos("U - S", "Trackbars")
     u_v = cv2.getTrackbarPos("U - V", "Trackbars")

     lower_color = np.array([l_h, l_s, l_v])
     upper_color = np.array([u_h, u_s, u_v])

     mask = cv2.inRange(hsv, lower_color, upper_color)

     result = cv2.bitwise_and(frame, frame, mask=mask)    

    # show thresholded image
     cv2.imshow("mask", mask)
     cv2.imshow("result", result)  

     key = cv2.waitKey(0) & 0xFF
     if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
