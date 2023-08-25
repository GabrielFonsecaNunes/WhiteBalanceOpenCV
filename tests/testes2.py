import cv2
import numpy as np

def change_temperature_precise(img, temperature):
  """
  Altera a temperatura da cor de uma imagem com alta precisão.

  Args:
    img: A imagem a ser alterada.
    temperature: A temperatura da cor desejada.

  Returns:
    A imagem com a temperatura alterada.
  """

  # Converte a imagem para o espaço de cores HSV.
  img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  # Calcula os canais de matiz, saturação e valor da imagem.
  h, s, v = cv2.split(img_hsv)

  # Ajusta o canal de valor da imagem.
  v_adjusted = np.array(v * temperature).astype('uint8')

  # Concatena os canais de matiz, saturação e valor da imagem ajustada.
  img_hsv_adjusted = cv2.merge((h, s, v_adjusted))

  # Converte a imagem de volta para o espaço de cores RGB.
  img_rgb = cv2.cvtColor(img_hsv_adjusted, cv2.COLOR_HSV2BGR)

  return img_rgb


def main():
  # Lê a imagem.
  img = cv2.imread("./img/image.jpg")

  # Altera a temperatura da imagem para 3.000 K.
  img_warm = change_temperature_precise(img, 0.1)

  # Altera a temperatura da imagem para 5.500 K.
  img_cold = change_temperature_precise(img, 0.2)

  # Exibe as imagens.
  cv2.imshow("Imagem original", img)
  cv2.imshow("Imagem mais quente", img_warm)
  cv2.imshow("Imagem mais fria", img_cold)
  cv2.waitKey(0)


if __name__ == "__main__":
  main()


# if __name__ == '__main__':

#     img = cv2.imread("./img/image.jpg")

#     img_balanced = auto_white_balance(img)

#     cv2.imshow("Imagem original", img)
#     cv2.imshow("Imagem equilibrada", img_balanced)
#     cv2.waitKey(0)
