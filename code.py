import numpy as np
import cv2
import time

cap = cv2.VideoCapture(-1)

time.sleep(1)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)   #imgshow
    if cv2.waitKey(100) & 0xff == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

























