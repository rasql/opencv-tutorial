# background subtraction (BS)
import cv2 as cv

cap = cv.VideoCapture(0)

# print width and height
print('width:', cap.get(3))
print('height:', cap.get(4))

# set to 640x360
ret = cap.set(3, 640)
ret = cap.set(4, 360)

print('width:', cap.get(3))
print('height:', cap.get(4))


backSub = cv.createBackgroundSubtractorMOG2()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()


    fgMask = backSub.apply(frame)
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(cap.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    #show the current frame and the fg masks
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()