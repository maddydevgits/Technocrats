import numpy as np
import cv2

current_frame =cv2.VideoCapture(0)


previous_frame=current_frame


while(current_frame.isOpened()):


current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
previous_frame_gray= cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)

frame_diff=cv2.absdiff(current_frame_gray,previous_frame_gray)


cv2.imshow('frame diff ',frame_diff)


cv2.waitKey(1)

current_frame.copyto(previous_frame)
ret, current_frame = current_frame.read()


current_frame.release()
cv2.destroyAllWindows()
