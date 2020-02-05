import cv2 as cv

print(cv.__version__)
RED = (0, 0, 255)
scaleFactor = 1.1
minNeighbors = 5
minSize = (30, 30)

def detect():
    rects = face_detector.detectMultiScale(gray, 
        scaleFactor=scaleFactor,
        minNeighbors=minNeighbors, 
        minSize=minSize, 
        flags=cv.CASCADE_SCALE_IMAGE)

    print(f'found {len(rects)} face(s)')

    img = img0.copy()
    for rect in rects:
        cv.rectangle(img, rect, RED, 2)
    cv.imshow('window', img)

def trackbar(x):
    global minSize, minNeighbors, scaleFactor
    i = cv.getTrackbarPos('size','window')
    d = (24, 30, 60, 120)[i]
    minSize = (d, d)
    
    n = cv.getTrackbarPos('neighbors','window') + 1
    minNeighbors = n

    i = cv.getTrackbarPos('scale','window')
    s = (1.05, 1.1, 1.4, 2)[i]
    scaleFactor
    
    text = f'minNeighbors={n}, minSize={d}, scaleFactor={s}'
    cv.displayOverlay('window', text)
    detect()

img0 = cv.imread('family2.jpg')
img = img0.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

path = 'cascades/haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)

detect()

cv.createTrackbar('neighbors', 'window', 0, 10, trackbar)
cv.createTrackbar('size', 'window', 0, 3, trackbar)
cv.createTrackbar('scale', 'window', 0, 3, trackbar)
cv.waitKey(0)
