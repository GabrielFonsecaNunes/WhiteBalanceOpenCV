import cv2 as cv
import numpy as np
import utils

def run():
    """
    """
    cam = cv.VideoCapture(0)

    while True:
        _, frame = cam.read()

        # Convert the image to HSV color space
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Find the white point
        white_point = cv.selectROI(frame)

        # Show the white point
        cv.imshow(white_point, "")

        # Set the white point
        utils.setWhiteBalance(frame, white_point)

        # Convert the image back to RGB color space
        image = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

        # wait for 'q' key to exit
        if cv.waitKey(1) == ord('q'):
            utils.plot_histogram(frame=frame)
            cv.imwrite('balanced_image.jpg', image)
            break

    # When everything done, release the capture
    cam.release()
    cv.destroyAllWindows()


run()