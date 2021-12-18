import cv2 as cv 
import mediapipe as mp 
import time 


cap = cv.VideoCapture(0)

mpDraw = mp.solutions.drawing_utils 
mpPose = mp.solutions.pose 
pose = mpPose.Pose()

pTime = 0

while True: 
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape 
            cx, cy = int(lm.x*w), int(lm.y*h) 
            cv.circle(img, (cx,cy), 5, (255,0,255), cv.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime 

    cv.putText(img, str(int(fps)), (10,60), cv.FONT_HERSHEY_COMPLEX, 2, (255,0,255), 1)
    cv.imshow("Image", img)
    cv.waitKey(1)


