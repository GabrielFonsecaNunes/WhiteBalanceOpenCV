import cv2 as cv
import numpy as np
from matplotlib.patches import Rectangle

cap = cv.VideoCapture(0)

contador = 0

max_v = 0
min_s = 255

diametro_vizinhanca = 3
size_vizinhanca = int (diametro_vizinhanca / 2)
n_vizinhos = diametro_vizinhanca * diametro_vizinhanca
soma_r = 0
soma_g = 0
soma_b = 0

mais_branco = [0, 0, min_s, max_v]
media_vizinhanca_mais_branco = [0,0,0]

while(1):

    # Take each frame
    _, frame = cap.read()

    #resizedFrame = cv.resize(frame, (1000, 700))
    bilateral_blur = cv.bilateralFilter(frame,9,75,75)

    # Convert BGR to HSV
    hsv = cv.cvtColor(bilateral_blur, cv.COLOR_BGR2HSV)
     
    #encontra o pixel com menor saturação e maior value
    if contador == 100:
        height = bilateral_blur.shape[1]
        width = bilateral_blur.shape[0]

        for y in range(height):
            for x in range(width):
                #print('x: ',x,' y: ',y)
                if ((hsv[x][y][2] >= mais_branco[3]) & (hsv[x][y][2] <= 255)) :
                    if((bilateral_blur[x][y][0] != 255) & (bilateral_blur[x][y][1] != 255) & (bilateral_blur[x][y][0] != 255)):
                        mais_branco[0] = x
                        mais_branco[1] = y
                        mais_branco[2] = hsv[x][y][1]
                        mais_branco[3] = hsv[x][y][2]

        #print('9.900K')
        print('Valores do pixel mais branco (x,y,saturation, value):', mais_branco, 'h',hsv[mais_branco[0]][mais_branco[1]][0])
        print('(BGR): ', bilateral_blur[mais_branco[0]][mais_branco[1]])
        
        x_centro = mais_branco[0]
        y_centro = mais_branco[1]

        for i in range((-size_vizinhanca),(size_vizinhanca+1)):
            for j in range ((-size_vizinhanca),(size_vizinhanca+1)):
                if((x_centro + j) > bilateral_blur.shape[1]):
                    bounded_x = bilateral_blur.shape[1]
                else:
                    bounded_x = x_centro + j
                
                if((y_centro+i) > bilateral_blur.shape[0]):
                    bounded_y = bilateral_blur.shape[0]
                else:
                    bounded_y = y_centro+i
                print('x:', bounded_x, 'y:',bounded_y,'; b:',bilateral_blur[bounded_x][bounded_y][0],', g:',bilateral_blur[bounded_x][bounded_y][1], 'r: ',bilateral_blur[bounded_x][bounded_y][2])
                #
                soma_r += bilateral_blur[bounded_x][bounded_y][2]
                soma_g += bilateral_blur[bounded_x][bounded_y][1]
                soma_b += bilateral_blur[bounded_x][bounded_y][0]

        # print(n_vizinhos)
        # print(soma_b)
        # print(soma_g)
        # print(soma_r)
        media_vizinhanca_mais_branco [0] = int(soma_b / n_vizinhos)
        media_vizinhanca_mais_branco [1] = int(soma_g / n_vizinhos)
        media_vizinhanca_mais_branco [2] = int(soma_r / n_vizinhos)
        print('valor bgr médio da vizinhança do pixel mais branco (BGR):',media_vizinhanca_mais_branco)

        maior_indice = max(media_vizinhanca_mais_branco)
        media_abs = []

        for i in range (3):
            media_abs.append(round((media_vizinhanca_mais_branco[i]/maior_indice),3))
        print(media_abs)
        
        coluna_max = mais_branco[0]
        linha_max = mais_branco[1]
    
        cv.putText(bilateral_blur, 'O',(mais_branco[1],mais_branco[0]),cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2, cv.FILLED, False)
        #cv.putText(bilateral_blur, 'O',(360,316),cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2, cv.FILLED, False)
        cv.imwrite('testePixelMaisBranco.png',bilateral_blur)

        #frame.add_patch(Rectangle((mais_branco[0], mais_branco[1]), 120, 120, linewidth=3, edgecolor='r', facecolor='none'))

    #2.4k equivale a 157,60,50 HSV
    #9.9k equivale a 21,194,255 HSV 
    limite_minimo = np.array([0,0,255])
    limite_maximo = np.array([255,255,255]) 

    #Threshold the HSV image to get only white colors
    #mask = cv.inRange(hsv, lower_blue, upper_blue)
    mask = cv.inRange(hsv, limite_minimo, limite_maximo)

    #Bitwise-AND mask and original image
    res = cv.bitwise_and(bilateral_blur,bilateral_blur, mask= mask)

    #escreve o HSV do pixel na tela
    #teste_bgr = 'BGR pixel [316][360]= ' + str(bilateral_blur[316][360])
    # teste_hsv = 'HSV pixel [316][360]= ' + str(hsv[316][360])

    #cv.putText(bilateral_blur, 'O',(360,316),cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2, cv.FILLED, False)
    #cv.putText(bilateral_blur, teste_hsv,(50,80),cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 5, cv.FILLED, False)

    #pixel [1][1] branco no 2.4k = (107-108, 210-220, 130-140)
    #pixel [1][1] branco no 5.4k = (80-90, 40-55, 129-132)
    #pixel [1][1] branco no 9.9k = (30-36, 38-45, 125-132)

    newFrame = cv.hconcat([bilateral_blur, res])

    contador +=1

    cv.imshow('frame e res',newFrame)

    k = cv.waitKey(5) & 0xFF
 
    if k == 27:
        break

cv.destroyAllWindows()