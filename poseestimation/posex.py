import cv2 as cv 
import posmodule as pm  
import time 


cap = cv.VideoCapture(0)
pTime = 0 
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        print(lmList[14])
        cv.circle(img, (lmList[14][1],lmList[14][2]), 10, (0,0,255), cv.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime 

    cv.putText(img, str(int(fps)), (10,50), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
    cv.imshow("Image", img)
    cv.waitKey(1)


