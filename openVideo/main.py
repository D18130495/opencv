import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.open(0)

while cap.read():
    flag, frame = cap.read()
    cv2.imshow("My_window", frame)

    key_pressed = cv2.waitKey(60)

    if key_pressed == 27:
        break

cap.release()
cv2.destroyAllWindows()
