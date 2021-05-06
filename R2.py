#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

path = cv2.data.haarcascades + "haarcascade_frontalcatface.xml"

# Inicializa o classificador cascade
face_classifier = cv2.CascadeClassifier(path) 

# configura a captura de imagem da webcam
video_cap = cv2.VideoCapture(0)

# se a webcam abrir pego um frame
if video_cap.isOpened():
    rval, frame = video_cap.read()
    
else:
    rval = False

while rval:
    # Converte o frame para escala de cinza 
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Realiza a detecção de face na imagem em cinza
    faces_return = face_classifier.detectMultiScale(img_gray, scaleFactor = 1.2, minNeighbors = 5)
    # Faz a varredura na lista de faces detectadas em faces_return
    for (x,y,w,h) in faces_return:
        # Desenha um retangulo em cada face detectada
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)

        # Faz o mesmo crop da face com a imagem colorida
        roi_color = frame[y:y+h, x:x+w]

        # Exibe saida da imagem
        cv2.imshow("result", roi_color)


    # Exibe saida da imagem
    cv2.imshow("normal", frame)
    

    # Atualiza com um novo frame
    rval, frame = video_cap.read()

    # ESC para sair do programa
    key = cv2.waitKey(10)
    if key == 27:
        break

video_cap.release()
cv2.destroyAllWindows()
 