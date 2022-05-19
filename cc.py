#pip works in python3
import cv2  #module import
cam=cv2.VideoCapture(0) #class VideoCApture, cam=object, VideoCApture is inside cv2, 0 always
a,img=cam.read() #VideCApture inside read 2 values - a-info, img -raw capture image
cv2.imwrite("/home/abhirup/ab.png",img) #cv2 imwrite colvert raw to human read
cam.release() #camera func close, so it doesnt process