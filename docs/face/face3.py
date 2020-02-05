import cv2 as cv
import numpy as np
import time

path = 'cascades/haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)

def detect():
    rects = face_detector.detectMultiScale(gray_s, 
        scaleFactor=1.1,
        minNeighbors=5, 
        minSize=(30, 30), 
        flags=cv.CASCADE_SCALE_IMAGE)

    for rect in rects:
        cv.rectangle(gray_s, rect, 255, 2)

cap = cv.VideoCapture(0)
t0 = time.time()

M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
size = (640, 360)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_s = cv.warpAffine(gray, M, size)

    detect()
    
    cv.imshow('window', gray_s)
    t = time.time()
    cv.displayOverlay('window', f'time={t-t0:.3f}')
    t0 = t

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
