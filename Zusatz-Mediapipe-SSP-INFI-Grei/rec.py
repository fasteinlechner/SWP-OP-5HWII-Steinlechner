
import cv2
import time
import gestures

# Diese Methode erkennt alle 3 Gesten mithilfe von Mediapipe und der in der Datei gestures.py vorgegebenen Werte

def get_gest(cap,hands, mpDraw, mpHands):
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            landmarks = handLms.landmark
            for id, lm in enumerate(landmarks):
                #print(id, lm)
                h, w , c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx,cy), 4, (255,0,255), cv2.FILLED)
                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
        # Anleitung wie die Gesten ausschauen müssen, um erkannt zu werden, finden Sie im Ordner Symbolbilder_Anleitung

        if gestures.stein(landmarks):
            return 2
        if gestures.papier(landmarks):
            return 0
        if gestures.schere(landmarks):
            return 1
        
    return -1
        
   
    
   
    
    
