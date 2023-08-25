# import cv2
# import numpy as np

# def balance_white(img, temp):
#   """
#   Balanceia o branco de uma imagem a partir dos dados da temperatura da imagem.

#   Args:
#     img: A imagem original.
#     temp: Os dados da temperatura da imagem.

#   Returns:
#     A imagem balanceada.
#   """

#   # Converte a imagem para o espaço de cores HSV.
#   img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#   # Calcula o valor máximo de saturação para cada canal de cor.
#   max_saturation = np.max(img_hsv, axis=(1, 2))

#   # Calcula o fator de ajuste para cada canal de cor.
#   factors = (max_saturation / temp)

#   # Aplica o fator de ajuste a cada canal de cor.
#   res = img_hsv[:, :, 1] * factors


#   # Converte a imagem de volta para o espaço de cores RGB.
#   img_balanced = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

#   return img_balanced


# # Exemplo de uso
# img = cv2.imread("./img/exemplo.jpg")

# # Dados da temperatura da imagem
# temp = [6500, 6500, 6500]

# temp = np.array(4200)

# # Balanceia o branco da imagem
# img_balanced = balance_white(img, temp)

# # Exibe a imagem balanceada
# cv2.imshow("Imagem balanceada", 4200)
# cv2.waitKey(0)

# import cv2
# import numpy as np

# def balance_white(image, temperature):
#   """
#   Balanceia o branco da imagem a partir da temperatura da imagem.

#   Args:
#     image: A imagem a ser balanceada.
#     temperature: A temperatura da imagem.

#   Returns:
#     A imagem balanceada.
#   """

#   # Converte a imagem para RGB.
#   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#   # Calcula os valores de branco e preto.
#   white = np.array([255.0, 255.0, 255.0])
#   black = np.array([0.0, 0.0, 0.0])

#   # Calcula os valores de temperatura para branco e preto.
#   white_temperature = np.sum(white) / 3.0
#   black_temperature = np.sum(black) / 3.0

#   # Calcula o fator de correção.
#   correction = (white_temperature - temperature) / (white_temperature - black_temperature)

#   # Corrige os valores de cada canal.
#   for channel in range(0, 3):
#     image[:, :, channel] = image[:, :, channel] * correction

#   # Converte a imagem de volta para BGR.
#   image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#   return image


# # Lê a imagem.
# image = cv2.imread("./img/exemplo.jpg")

# # Obtém a temperatura da imagem.
# temperature = 10

# # Balanceia o branco da imagem.
# image = balance_white(image, temperature)

# # Exibe a imagem balanceada.
# cv2.imshow("Imagem balanceada", image)
# cv2.waitKey(0)


import numpy as np
import cv2

def balance_white(image, temperature):
  """Balanceia o branco da imagem a partir da temperatura.

  Args:
    image: A imagem a ser balanceada.
    temperature: A temperatura da imagem, em graus Kelvin.

  Returns:
    A imagem balanceada.
  """

  # Converte a imagem para o espaço de cores Lab.
  image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

  # Calcula os valores de luminosidade de cada canal.
  L = image_lab[:, :, 0]

  # Calcula o fator de correção para cada canal.
  factors = np.power(10000 / temperature, 1 / 5)

  # Aplica o fator de correção a cada canal.
  L *= np.array(factors)

  # Atribui os novos valores de luminosidade à imagem.
  image_lab[:, :, 0] = L

  # Converte a imagem de volta para o espaço de cores RGB.
  image = cv2.cvtColor(image_lab, cv2.COLOR_LAB2BGR)

  return image


# Exemplo de uso

image = cv2.imread("./img/exemplo.jpg")
temperature = np.array(5000)

balanced_image = balance_white(image, temperature)

cv2.imshow("Imagem original", image)
cv2.imshow("Imagem balanceada", balanced_image)
cv2.waitKey(0)
