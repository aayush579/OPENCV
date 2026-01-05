
import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter('my_video.avi',codec,20,(frame_width,frame_height))

while True:
    success, frame = cap.read()

    if not success:
        break

    recorder.write(frame)
    cv2.imshow('Recording',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

