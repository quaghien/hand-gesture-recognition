import cv2
from cvzone.HandTrackingModule import HandDetector

detection = HandDetector(detectionCon=0.95, maxHands= 2)
#staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5
video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    hands,img = detection.findHands(frame)
    height, width, _ = frame.shape

    cv2.rectangle(frame, (0, 0), (200, 50),(50,50,255),-2)
    cv2.rectangle(frame, (width - 200, 0), (width, 50),(50,50,255),-2)


    if hands:
        lmlist = hands[0]
        figerUp= detection.fingersUp(lmlist)
        print(figerUp)
        if figerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Frame Count = 0',(20,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'STOP', (width-180, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[0,1,0,0,0] or figerUp==[1,0,0,0,0] or figerUp==[0,0,1,0,0] or figerUp==[0,0,0,1,0] or figerUp==[0,0,0,0,1]:
            cv2.putText(frame,'Frame Count = 1',(20,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Cheating Answer A', (width-180, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[0,1,1,0,0] or figerUp==[1,1,0,0,0] or figerUp==[0,0,1,1,0] or figerUp==[0,0,0,1,1] or figerUp==[1,0,0,0,1]:
            cv2.putText(frame,'Frame Count = 2',(20,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Cheating Answer B', (width-180, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[0,1,1,1,0] or figerUp==[1,1,1,0,0] or figerUp==[0,0,1,1,1] or figerUp==[1,1,0,0,1]:
            cv2.putText(frame,'Frame Count = 3',(20,20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Cheating Answer C',(width-180, 30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
        if figerUp==[0,1,1,1,1] or figerUp==[1,1,1,1,0] or figerUp==[1,1,1,0,1]or figerUp==[1,1,1,1,0]:
            cv2.putText(frame,'Frame Count = 4',(20,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'Cheating Answer D', (width-180, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
        if figerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Frame Count = 5',(20,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, 'CONTINUE', (width-180, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1,cv2.LINE_AA)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    
    if k==ord('x'):
        
        break
 # Use the 'x' button on the keyboard to exit



video.release()
cv2.destroyAllWindows()