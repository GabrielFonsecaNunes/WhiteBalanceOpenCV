# import cv2 as cv
# import numpy as np
import utils

def run():
    """
    """
    ...

#     cam = cv.VideoCapture(0)

#     while True:
#         _, frame = cam.read()

#         # Calcula o balanço de branco da imagem.
#         # temperature = tests_white_balance.get_white_balance(frame)

#         # adjusted_image = tests_white_balance.adjust_white_balance(frame, temperature)

#         # temperature = utils_teste.get_white_balance(image=frame)
#         # print(temperature)
        
#         # # Convert the image to HSV color space
#         # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#         # # Find the white point
#         # white_point = cv.selectROI(frame)

#         # 
#         cv.imshow("Original", frame)

#         # # Show the white point
#         # cv.imshow("Balance White", adjusted_image)

#         # # Set the white point
#         # utils.setWhiteBalance(frame, white_point)

#         # # Convert the image back to RGB color space
#         # image = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#         k = cv.waitKey(3)

#         # wait for 'q' key to exit
#         if k == ord('q'):
#             utils.plot_histogram(frame=frame)
#             # utils.plot_histogram(frame=adjusted_image)
#             cv.imwrite('balanced_image.jpg', frame)
#             break

#     # When everything done, release the capture
#     cam.release()
#     cv.destroyAllWindows()

if __name__ == '__main__':
    run()