import cv2 as cv
from time import sleep

cap = cv.VideoCapture('../data/water.mp4')
totalFrame = cap.get(cv.CAP_PROP_FRAME_COUNT)
print('total frame:',totalFrame)
current = 0
while True:

    # 读视频帧
    ret, frame = cap.read()
    # frame = cv.flip(frame,1)
    # 显示视频
    # cv.imshow('Video', frame)
    if current % 10 == 0:
        cv.imwrite('../output/video_image/'+ str(current) + '.jpg', frame)
        print('%d frame is got' % current)
    current = current + 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if current >= totalFrame:
        break
cap.release()
cv.destroyAllWindows()
