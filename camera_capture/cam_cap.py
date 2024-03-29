import cv2
import dlib
import imutils
import platform

print platform.machine()

print platform.version()

print platform.uname()

print platform.system()

#print platform.processor()

if platform.machine() == 'x86_64':
    print "Running on X86_64"

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()


while(True):
    ret, frame = cap.read()

    face_rects, scores, idx = detector.run(frame, 0)

    for i, d in enumerate(face_rects):
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()
        text = "%2.2f(%d)" % (scores[i], idx[i])

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)

        cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,
                    0.7, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()