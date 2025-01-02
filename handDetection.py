import mediapipe as mp
import cv2 as cv

tangan = mp.solutions.hands
gambar = mp.solutions.drawing_utils

    
class deteksiTangan:
    def __init__(self, max_num_hands = 2, min_detection_confidence = 0.5, min_tracking_confidence = 0.5):
        self.hands = tangan.Hands(max_num_hands = max_num_hands, min_detection_confidence = min_detection_confidence, min_tracking_confidence = min_tracking_confidence)

    
    def cariHandLandMarks(self, image, handNumber = 0, draw = False):
            gambarAsli =  image
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = self.hands.process(image)
        
        
            landMarkList = []

            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[handNumber]
                for id, landMark in enumerate(hand.landmark):
                    imgH, imgW, imgC = gambarAsli.shape
                    xPos, yPos = int(landMark.x*imgW), int(landMark.y*imgH)
                    landMarkList.append([id, xPos, yPos])
            
                jumlah_jari = 0
                
                if landMarkList[4][1] < landMarkList [3][1] < landMarkList[0][1] :
                    jumlah_jari+=1
                if landMarkList[4][1] > landMarkList [3][1] > landMarkList[0][1] :
                    jumlah_jari+=1
                if landMarkList[8][2] < landMarkList [7][2]:
                    jumlah_jari+=1
                if landMarkList[12][2] < landMarkList [11][2]:
                    jumlah_jari+=1
                if landMarkList[16][2] < landMarkList [15][2]:
                    jumlah_jari+=1
                if landMarkList[20][2] < landMarkList [19][2]:
                    jumlah_jari+=1
                
            
                if draw : 
                    gambar.draw_landmarks(gambarAsli, hand, tangan.HAND_CONNECTIONS)
                    
                return jumlah_jari

    
   
            

        

