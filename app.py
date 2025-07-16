#hi my name is abhijeet singh this is just a side project i hope you will like this...

import cv2 
import mediapipe as mp

import math
mpface=mp.solutions.face_mesh

face=mpface.FaceMesh()
mppose=mp.solutions.pose

pose=mppose.Pose()

cap=cv2.VideoCapture(0)
left_arm_angle=0
left_shoulder_angle=0

def findangle(p1,p2,p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3
    return (math.degrees(math.atan2((y2-y3),(x2-x3))-math.atan2((y2-y1),(x2-x1))))

def drawcircle(img,point,color=(255,0,0),thick=-1,rad=10):
    
    x,y=point
    
    ih,iw,ic=img.shape
    cx=int(iw*x)
    cy=int(ih*y)
    
    cv2.circle(img,(cx,cy),rad,color,thick)

while True:


    
    ok,frame=cap.read()



    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result1=(face.process(rgb))

    result=pose.process(rgb)
        
    if (result.pose_landmarks):
        left_shoulder=result.pose_landmarks.landmark[11].x,result.pose_landmarks.landmark[11].y
        left_elbow=result.pose_landmarks.landmark[13].x,result.pose_landmarks.landmark[13].y
        left_wrist=result.pose_landmarks.landmark[15].x,result.pose_landmarks.landmark[15].y


        left_hip=result.pose_landmarks.landmark[23].x,result.pose_landmarks.landmark[23].y
            
        left_arm_angle=(findangle(left_shoulder,left_elbow,left_wrist))
        left_shoulder_angle=(findangle(left_hip,left_shoulder,left_elbow))

    
    
    if (result1.multi_face_landmarks):

        for i in result1.multi_face_landmarks:
            for id,pos in enumerate(i.landmark):
                if id==151:
                    if left_shoulder_angle<-12 and left_arm_angle <30:
                        cv2.putText(frame,"THREAT!!! Target Locked",(50,50),cv2.FONT_HERSHEY_DUPLEX,1.5,(0,0,255),2)  
                        ih,iw,ic=frame.shape
##                      print(left_shoulder_angle)
##                      print("arm",left_arm_angle)

                        cx=int(iw*(pos.x))
                        cy=int(ih*(pos.y))
                        cv2.circle(frame,(cx,cy),10,(0,0,255),2)
                        cv2.line(frame,(cx,cy-5000),(cx,cy),(255,0,0),2)
                        cv2.line(frame,(cx-5000,cy),(cx,cy),(255,0,0),2)
                        cv2.line(frame,(cx+5000,cy),(cx,cy),(255,0,0),2)
                        cv2.line(frame,(cx,cy+5000),(cx,cy),(255,0,0),2)
                        cv2.circle(frame,(cx,cy),2,(0,0,255),2)

                    else:
                        cv2.putText(frame,"NO THREAT!!!",(50,50),cv2.FONT_HERSHEY_DUPLEX,1.5,(0,255,0),2)  

##                    print(left_shoulder_angle)
##                    print("arm",left_arm_angle)
                    
                
                 
                    
                



    cv2.imshow("frame",frame)

    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
