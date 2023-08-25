import cv2 as cv
import numpy as np

def get_white_balance(image):
  """
  Calcula o balanço de branco da imagem.

  Args:
    image: A imagem a ser calculada.

  Returns:
    O balanço de branco da imagem.
  """

  # Converte a imagem para o espaço de cores HSV.
  hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

  # Calcula o histograma da imagem HSV.
  # histogram = cv.calcHist([hsv_image],[1],None,[256],[0,256])
  histogram = hsv_image[:, :, 2].flatten()

  # Encontra o pico do histograma no canal V.
  max_index = np.argmax(histogram)

  # Calcula a temperatura da cor branca na imagem.
  temperature = (max_index - 60) / 2

  temperature = np.sum(histogram * 256) / np.sum(histogram)

  # Retorna o balanço de branco da imagem.
  return temperature

def adjust_white_balance(image, temperature):
  """
  Ajusta o balanço de branco da imagem.

  Args:
    image: A imagem a ser ajustada.
    temperature: A temperatura da cor branca.

  Returns:
    A imagem com o balanço de branco ajustado.
  """

  # Converte a imagem para o espaço de cores HSV.
  hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

  # Ajusta o valor do canal V da imagem.
  hsv_image[:, :, 2] = temperature

  # Converte a imagem de volta para o espaço de cores BGR.
  image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

  return image

if __name__ == "__main__":
    # Carrega a imagem.
    image = cv.imread("./img/Equipe.jpg")

    # Calcula o balanço de branco da imagem.
    temperature = get_white_balance(image)

    # Ajusta o balanço de branco da imagem.
    adjusted_image = adjust_white_balance(image, 2000)

    # Exibe a imagem original e a imagem ajustada.
    cv.imshow("Original", image)
    cv.imshow("Ajusted", adjusted_image)
    cv.waitKey(0)
