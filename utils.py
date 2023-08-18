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
    ...


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
