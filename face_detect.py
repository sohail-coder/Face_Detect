from cv2 import cv2 as cv

capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier(r'.\cascade.xml')
# print('all ok')

while True:
    isTrue, Frame = capture.read()
    gray = cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
    flipped = cv.flip(Frame, 1)
    face_rect = haar_cascade.detectMultiScale(flipped, 1.1, 3)
    for (x, y, w, h) in face_rect:
        cv.rectangle(flipped, (x, y), (x+w, y+h), (0, 255, 0), 1)
    cv.imshow("Live Feed", flipped)
    if(cv.waitKey(20) & 0xff == ord('d')):
        break
    # break

capture.release()
cv.destroyAllWindows()
