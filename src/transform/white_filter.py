import cv2 as cv
import numpy as np
from .transform import Transform
from train_model_regressor import TrainModelRegressor
import pandas as pd
import matplotlib.pyplot as plt

DIAMETER_VIZINHANCA = 3
SIZE_VIZINHANCA = DIAMETER_VIZINHANCA // 2

limite_minimo = np.array([0, 0, 100])
limite_maximo = np.array([255, 255, 255])

def aplica_mascara(frameBGR, frameHSV):
    mask = cv.inRange(frameHSV, limite_minimo, limite_maximo)
    res = cv.bitwise_and(frameBGR, frameBGR, mask=mask)
    return res

def encontra_pixel_branco(frameBGR, frameHSV):
    white_pixels = np.where((frameHSV[:, :, 2] >= 0.97 * 255) & (frameHSV[:, :, 2] <= 255))
    if white_pixels[0].size == 0:
        return [0, 0, 255, 255]  # Default if no white pixels found
    
    x, y = white_pixels[0][0], white_pixels[1][0]
    mais_branco = [x, y, frameHSV[x, y, 1], frameHSV[x, y, 2]]
    return mais_branco

def media_vizinhanca(bilateral_blur, ponto_branco):
    x_centro, y_centro = ponto_branco[0], ponto_branco[1]
    bounded_x = np.clip(x_centro + np.arange(-SIZE_VIZINHANCA, SIZE_VIZINHANCA + 1), 0, bilateral_blur.shape[1] - 1)
    bounded_y = np.clip(y_centro + np.arange(-SIZE_VIZINHANCA, SIZE_VIZINHANCA + 1), 0, bilateral_blur.shape[0] - 1)

    vizinhos = bilateral_blur[bounded_y[:, np.newaxis], bounded_x]
    media_vizinhanca_mais_branco = np.mean(vizinhos, axis=(0, 1))
    media_abs = media_vizinhanca_mais_branco / max(media_vizinhanca_mais_branco)
    
    print('valor bgr médio da vizinhança do pixel mais branco (BGR):', media_vizinhanca_mais_branco)
    print(media_abs)

    return media_vizinhanca_mais_branco

def plot_histogram(frame):
    """
    Args:
        frame:
    """
    plt.figure(figsize= (10, 6))
    plt.title("Histograma RGB")
    color = ('b','g','r')

    for i,col in enumerate(color):
        histr = cv.calcHist([frame],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.plot(data = frame)
    plt.show()

def pipeline_filter_white(frame):
    bilateral_blur = cv.bilateralFilter(frame, 9, 75, 75)
    hsv = cv.cvtColor(bilateral_blur, cv.COLOR_BGR2HSV)
    pixel_branco = encontra_pixel_branco(bilateral_blur, hsv)
    mean = media_vizinhanca(bilateral_blur, pixel_branco)
    res = aplica_mascara(bilateral_blur, hsv)
    return res, mean

def measere_temp(frame):
    """
    """
    h, v, _ = frame.shape
    frame_filter, mean = pipeline_filter_white(frame)
    transform = Transform(frame=frame_filter)
    # img_temp_mean = transform.BGR2TEMP().reshape((h, v, 1))
    img_temp_mean = transform.BGR2TEMP()
    return img_temp_mean.min()