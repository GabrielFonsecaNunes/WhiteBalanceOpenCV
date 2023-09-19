import cv2 as cv
import pickle as pkl
import numpy as np
import numba
from train_model_regressor import TrainModelRegressor


class Transform:

    def __init__(self, frame):
        self.frame = frame
        self.model_path = './model/models/'

    def get_transformer_BGR2TEMP(self, model_path):
        """
        Load the model BGR2TEMP
        """
        model_name = "model_regressor_rgb2temp"

        # Abrir o arquivo pickle
        with open(f"{model_path}/{model_name}", "rb") as f:
            # Carregar o modelo do arquivo
            model = pkl.load(f)

        # Retornar o modelo
        return model

    def get_transformer_TEMP2BGR(self, model_path):
        """
        Load the model TEMP2BGR
        """
        model_name = "model_regressor_temp2rgb"

        # Abrir o arquivo pickle
        with open(f"{model_path}/{model_name}", "rb") as f:
            # Carregar o modelo do arquivo
            model = pkl.load(f)

        # Retornar o modelo
        return model        

    def BGR2TEMP(self):
        """
        Args:
        Returns:
        """

        # 
        height, width, channels = self.frame.shape

        # Transform channels 
        BGR = self.frame[:, :, :].reshape(-1, 3)

        # Load Transformer BGR2TEMP
        BGR2TEMP = self.get_transformer_BGR2TEMP(model_path="./model/models/")

        # Frame BGR -> Frame Temperature
        temp_frame = BGR2TEMP.fit_transform(BGR)
        temp_frame = temp_frame.reshape(-1, 1)

        return temp_frame

    def TEMP2BGR(self, temp_frame):
        """
        Args:
            temp_frame:
        Returns:
        """
        # Shape Frame
        height, width, channels = self.frame.shape

        # 
        TEMP2BGR = self.get_transformer_TEMP2BGR(model_path="./model/models/")
        rgb_frame = TEMP2BGR.fit_transform(temp_frame)
        rgb_frame = np.resize(rgb_frame, (height, width, 3))
        rgb_frame = rgb_frame.astype(np.uint8)
        return rgb_frame
    
    def increase_temperature(self, temp):
        """
        """
        img_temp = self.BGR2TEMP()

        img_temp += (temp)

        return img_temp
    
    def descrease_temperature(self, temp):
        """
        """
        img_temp = self.BGR2TEMP()

        img_temp -= (temp)

        return img_temp
        
    
    def black_mask(self, img_rgb):
        """
        Args:
            img_rgb (): 
        Returns:
        """
        # Percorre os pixels da imagem original
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                # Verifica se o pixel é preto
                B, G, R = img[i, j]

                if R <= 150 or G <= 150 and B <= 150:
                    # Aplica o pixel na imagem de destino
                    img_rgb[i, j] = self.frame[i, j]

        return img_rgb

if __name__ == '__main__':
    # 
    img_path = "./resources/img/avatar1.jpeg"
    img = cv.imread(img_path)
    img = cv.GaussianBlur(img, (3,3), 1)

    # Create Transform 
    transform = Transform(frame= img)

    img_temp = transform.BGR2TEMP()
    
    img_rgb = transform.TEMP2BGR(temp_frame=img_temp)
    
    
    # img_rgb = transform.black_mask(img_rgb)

    cv.imshow("IMG Original", img)
    
    temp = 100

    # for i in range(20):
    #     img_temp_lower = transform.descrease_temperature(temp=temp)
    #     img_temp_higher = transform.increase_temperature(temp=temp)

    #     img_rgb_lower = transform.TEMP2BGR(temp_frame=img_temp_lower)
    #     img_rgb_higher = transform.TEMP2BGR(temp_frame=img_temp_higher)

    #     cv.imshow(f"Transform IMG {temp} Lower", img_rgb_lower)
    #     cv.imshow(f"Transform IMG {temp} Higher", img_rgb_higher)
    #     temp += 100
    #     cv.waitKey(0)

    img_temp_lower = transform.descrease_temperature(temp=2500)
    img_temp_higher = transform.increase_temperature(temp=2500)

    img_rgb_lower = transform.TEMP2BGR(temp_frame=img_temp_lower)
    img_rgb_higher = transform.TEMP2BGR(temp_frame=img_temp_higher)

    img_rgb_lower_mask = transform.black_mask(img_rgb_lower)
    img_rgb_higher_mask = transform.black_mask(img_rgb_higher)

    cv.imshow("Transform IMG Same Temp", img_rgb)
    cv.imshow(f"Transform IMG 2000 Lower", img_rgb_lower)
    cv.imshow(f"Transform IMG 2000 Higher", img_rgb_higher)
    cv.waitKey(0)
