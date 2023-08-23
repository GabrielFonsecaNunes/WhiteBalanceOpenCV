import cv2 as cv
from time import sleep

def increase_temperature(image, factor):
  """
  Aumenta a temperatura de uma imagem.

  Args:
    image: A imagem a ser alterada.
    factor: O fator de aumento da temperatura.

  Returns:
    A imagem alterada.
  """

  # Converte a imagem para a escala de cor HSV.
  hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

  # Aumenta o canal value da imagem.
  hsv_image[:, :, 2] = hsv_image[:, :, 2] * factor

  # Converte a imagem de volta para a escala de cor BGR.
  output_image = cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

  return output_image

if __name__ == "__main__":

    i = 0.01
    cam = cv.VideoCapture(0)

    while True:
        _, frame = cam.read()

        # Aumenta a temperatura da imagem
        output_image = increase_temperature(frame, 1*i)

        output_image_blur = cv.blur(output_image, (3,3), 0)

        # output_image_blurGaussian = cv.GaussianBlur(output_image, (3,3), 0)

        # Mostra a imagem original e a imagem alterada.
        cv.imshow("Imagem original", frame)
        cv.imshow("Imagem alterada", output_image_blur)
        sleep(0.05)
        i += 0.01

        if i >= 4:
          i = 0.0

        print(i)

        # wait for 'q' key to exit
        if cv.waitKey(1) == ord('q'):
            cv.imwrite('balanced_image.jpg', output_image)
            break

    cam.release()
    cv.destroyAllWindows()