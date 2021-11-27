import cv2
#MD NAYEEM MOLLA


cap = cv2.VideoCapture("v1.mp4")
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=20)
while True:
    ret, frame = cap.read()
    height, width,_ = frame.shape

    roi = frame[150: 640, 320: 680]

    mask = object_detector.apply(roi)
    
    contour, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 0), 3)

    
    cv2.imshow("roi", roi)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

    