import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def set_white_balanced(setpoint: float = 4200):
    """
    Define o valor do balanço de branco ideal
    Args:
        setpoint (flaot): Temperatura ideal de 2400 até 9900 K
    """
    ...

def has_white_pixels(frame):
    """
    Args:
        frame (image):
        threshold ():
    Returns:
        True se houver pixels brancos no frame, False caso contrário.
    """

    """
    Ainda é necessário testar mais, pra ver se o intervalo de branco está correto
    """
    resizedFrame = cv.resize(frame, (1000, 700))

    # Convert BGR to HSV
    hsv = cv.cvtColor(resizedFrame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # lower_blue = np.array([110,50,10])
    # upper_blue = np.array([130,255,255])

    #2.4k equivale a 157,60,50 HSV
    #9.9k equivale a 21,194,255 HSV 
    lower_white = np.array([0,5,120])
    upper_white = np.array([255,230,200])

    #Threshold the HSV image to get only white colors
    #mask = cv.inRange(hsv, lower_blue, upper_blue)
    mask = cv.inRange(hsv, lower_white, upper_white)

    #Bitwise-AND mask and original image
    res = cv.bitwise_and(resizedFrame,resizedFrame, mask= mask)

    #escreve o HSV do pixel [1, 1] na tela
    teste_hsv = 'HSV pixel [999][349]= ' + str(hsv[349][499])
    cv.putText(resizedFrame, teste_hsv,(100,40),cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 5, cv.FILLED, False)

    #pixel [1][1] branco no 2.4k = (107-108, 210-220, 130-140)
    #pixel [1][1] branco no 5.4k = (80-90, 40-55, 129-132)
    #pixel [1][1] branco no 9.9k = (30-36, 38-45, 125-132)

    newFrame = cv.hconcat([resizedFrame, res])

    #out.write(newFrame)

    cv.imshow('resizedFrame',newFrame)
    cv.imshow('res',res)


def find_white_pixels():
    """
    Verifique se existem pixels brancos no frame e 
    retorna a região com pixels brancos.
    Args:
        frame (image):
        threshold ():
    Returns:
        ret, region_white tuple(bool, frame):
    """


def xyz_to_rgb():
    """
    Args:
    Returns:
    """


def get_percentilewhite():
    """
    Args:
    Returns:
    """
    ...


def get_diff_setpoint():
    """
    Args:
    Returns:
    """
    ...

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


def background_subtraction():
    """
    Args:
    Returns:
    """
    ...

def object_detection():
    """
    Args:
    Returns:
    """
    ...

def location_highlights():
    """
    Args:
    Returns:
    """
    ...

def core_processing():
    """
    Args:
    Returns:
    """
    ...


def plot_balanced_frame():
    """
    Args:
    Returns:
    """
    ...
