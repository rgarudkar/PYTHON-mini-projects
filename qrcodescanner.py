# Import all the required libraries for our program.
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#Now, let’s create a decoder function that decodes barcode and QR code from a given image.
def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    
    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect  #Creates a rectangle around the qrcode
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2)) #automatically finds the dimension
        cv2.polylines(image, [pts], True, (0, 255, 0), 3) #used to draw rectangle around qr code 

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)
#Capture the video from the device camera.

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(1)
    if code == ord('q'):
        break