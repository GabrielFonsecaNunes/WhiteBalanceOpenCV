import cv2 as cv
import numpy as np
import pickle as pkl
from train_model_regressor import TrainModelRegressor

class Transform:
    def __init__(self, frame):
        """
        Initialize the Transform object.

        Args:
            frame (numpy.ndarray): The input image frame.
        """
        self.frame = frame
        self.model_path = './src/model/models/'
        self.BGR2TEMP_model = self.load_model('model_regressor_bgr2temp')
        self.TEMP2BGR_model = self.load_model('model_regressor_temp2bgr')

    def load_model(self, model_name):
        """
        Load a model from a pickle file.

        Args:
            model_name (str): Name of the model to be loaded.

        Returns:
            object: Loaded model object.
        """
        model_path = f"{self.model_path}/{model_name}"
        with open(model_path, "rb") as f:
            model = pkl.load(f)
        return model

    def BGR2TEMP(self):
        """
        Convert the BGR image to a temperature image.

        Returns:
            numpy.ndarray: Temperature image.
        """
        BGR = self.frame.reshape(-1, 3)
        temp_frame = self.BGR2TEMP_model.fit_transform(BGR).reshape(-1, 1)
        return temp_frame

    def TEMP2BGR(self, temp_frame):
        """
        Convert a temperature image back to a BGR image.

        Args:
            temp_frame (numpy.ndarray): Temperature image.

        Returns:
            numpy.ndarray: BGR image.
        """
        rgb_frame = self.TEMP2BGR_model.fit_transform(temp_frame)
        rgb_frame = rgb_frame.reshape(self.frame.shape)
        rgb_frame = np.clip(rgb_frame, 0, 255).astype(np.uint8)
        return rgb_frame

    def modify_temperature(self, temp):
        """
        Modify the temperature of the image.

        Args:
            temp (int): Temperature adjustment value.

        Returns:
            numpy.ndarray: Modified temperature image.
        """
        temp_frame = self.BGR2TEMP()
        temp_frame += temp
        return temp_frame

    def black_mask(self, img_rgb):
        """
        Apply a black mask to the input RGB image.

        Args:
            img_rgb (numpy.ndarray): RGB image.

        Returns:
            numpy.ndarray: RGB image with black mask applied.
        """
        black_pixels = np.logical_and.reduce(img_rgb[:, :, :3] <= 160, axis=-1)
        img_rgb[black_pixels] = self.frame[black_pixels]
        return img_rgb

if __name__ == '__main__':
    img_path = "./resources/img/avatar1.jpeg"
    img = cv.imread(img_path)
    img = cv.GaussianBlur(img, (3, 3), 1)

    transform = Transform(frame=img)

    img_temp = transform.BGR2TEMP()
    img_rgb = transform.TEMP2BGR(temp_frame=img_temp)
    
    img_temp_lower = transform.modify_temperature(-2500)
    img_temp_higher = transform.modify_temperature(2500)

    img_rgb_lower = transform.TEMP2BGR(temp_frame=img_temp_lower)
    img_rgb_higher = transform.TEMP2BGR(temp_frame=img_temp_higher)

    img_rgb_lower_mask = transform.black_mask(img_rgb_lower)
    img_rgb_higher_mask = transform.black_mask(img_rgb_higher)

    cv.imshow("IMG Original", img)
    cv.imshow("Transform IMG Same Temp", img_rgb)
    cv.imshow(f"Transform IMG 2500 Lower", img_rgb_lower)
    cv.imshow(f"Transform IMG 2500 Higher", img_rgb_higher)
    cv.waitKey(0)
