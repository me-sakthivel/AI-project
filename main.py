import cv2
import winsound
# To open the web cam
cap = cv2.VideoCapture(0)

# importing xml file
phone = cv2.CascadeClassifier('Phone.xml')


while(True):
    # capture frame by frame
    ret, frame = cap.read()

    # To make the frame grey
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = phone.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         #for alart 
         winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
         

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# To destory
cap.release()
cv2.destroyAllWindows()
