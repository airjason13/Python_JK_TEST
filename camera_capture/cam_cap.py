import cv2
import platform

print platform.machine()

print platform.version()

print platform.uname()

print platform.system()

#print platform.processor()

if platform.machine() == 'x86_64':
    print "Running on X86_64"

cap = cv2.VideoCapture(0);

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()