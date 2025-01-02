import cv2 as cv
from handDetection import  deteksiTangan
import serial

deteksiTangan = deteksiTangan(min_detection_confidence=0.5, min_tracking_confidence=0.5)

arduino = serial.Serial('COM5', 9600)

def koneksi(signal):
    arduino.write(signal.encode())

webcam = cv.VideoCapture(0)

while True:
    status, frame = webcam.read()
    frame = cv.flip(frame, 1)
    
    
    handLandMarks = deteksiTangan.cariHandLandMarks(image = frame, draw = True)
    
    print(f"Jari yang terdeteksi : {handLandMarks}")
    
    koneksi(str(handLandMarks))
    
    cv.imshow("Deteksi Tangan", frame)
    
    if cv.waitKey(1) == ord('a'):
        break
    
webcam.release()
cv.destroyAllWindows()