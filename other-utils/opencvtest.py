import numpy as np
import cv2 as cv

cam = cv.VideoCapture(0)
cv.namedWindow("Detect",cv.WINDOW_AUTOSIZE)
while cv.waitKey(1) != 27:
    ret, frame = cam.read()
    # frame = cv.flip(frame, 1)
    cv.imshow("Detect",frame)


cam.release()
cv.destroyAllWindows()