import pandas as pd
import pickle as pkl
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from hyperopt import fmin, tpe, hp

class TrainModelRegressor:

    def __init__(self, regressor):
        # Model Regressor
        self.model = regressor

    def fit(self, X, Y):
        """
        Args:
            X (np.array | pd.DataFrame): features to train X
            Y (np.array | pd.Series): Target Model Y
        """
        self.model.fit(X, Y)

    def fit_transform(self, X):
        """
        Args:
            X (np.array | pd.DataFrame): features to train X
        Return 
            Y (np.array): fit_transform
        """
        return self.model.predict(X)

    # def save_model(self, path: str, model_name: str):
    #     """
    #     Args:
    #         path (str): Path to folter
    #         model_name (str): Model's name 
    #     """
    #     with open(f"{path}/{model_name}", "wb") as model:
    #         pkl.dump(model_regressor_rgb_temp, model)


    def evaluate(self):
        """
        """
        ...    

if __name__ == "__main__":
    # Load Conversion DataFrame RGB TEMPERATURE KELVIN
    df = pd.read_csv("./resources/data/conversion_rgb_temp_full.csv", sep=";")
    X_train = df.loc[:, ["b", "g", "r"]].values
    Y_train = df.loc[:, ["Temperature [K]"]].values

    # Definindo o espaço de busca dos hiperparâmetros
    space = {
        'n_estimators': hp.choice('n_estimators', range(10, 200)),
        'max_depth': hp.choice('max_depth', range(1, 20)),
        'min_samples_split': hp.choice('min_samples_split', range(2, 20)),
        'min_samples_leaf': hp.choice('min_samples_leaf', range(1, 20)),
        'min_impurity_decrease': hp.uniform('min_impurity_decrease', 0, 0.5)
    }

    # Definindo a função objetivo para a otimização
    def objective(params):
        model = RandomForestRegressor(**params)
        mse_scores = -cross_val_score(model, X_train, Y_train, cv=5, scoring='neg_mean_squared_error')
        return np.mean(mse_scores)

    # Executando a otimização
    # best = fmin(fn=objective,
    #             space=space,
    #             algo=tpe.suggest,
    #             max_evals=100)

    # # Imprimindo os melhores hiperparâmetros encontrados
    # print("Melhores hiperparâmetros:")
    # print(best)

    # Model Regressor X: R G B predict -> Y: Temperature Kelvin
    model_regressor = RandomForestRegressor(
                                            n_estimators= 18, 
                                            max_depth= 10, 
                                            min_samples_split = 7, 
                                            min_impurity_decrease= 0.04905946910151222,
                                            n_jobs=-1
                    )
    
    # # Training Model Regressor 
    model_regressor_rgb_temp = TrainModelRegressor(model_regressor)
    model_regressor_rgb_temp.fit(X_train, Y_train)

    # Save model as pickle file 
    path = "./model/models"
    model_name="model_regressor_rgb2temp"

    with open(f"{path}/{model_name}", "wb") as model:
            pkl.dump(model_regressor_rgb_temp, model)

    # model_regressor_rgb_temp.save_model(path = "./model/models", model_name="model_regressor_rgb_temp")

    # Invert Data to train model
    X_train_new = Y_train.copy()
    Y_train_new = X_train.copy()
    X_train = X_train_new
    Y_train = Y_train_new

    # Executando a otimização
    # best = fmin(fn=objective,
    #             space=space,
    #             algo=tpe.suggest,
    #             max_evals=100)

    # # Imprimindo os melhores hiperparâmetros encontrados
    # print("Melhores hiperparâmetros:")
    # print(best)

    # Create Model
    model_regressor = RandomForestRegressor(
                            n_estimators= 185,
                            min_impurity_decrease = 5.7327978505258836e-05, 
                            min_samples_leaf = 2,
                            min_samples_split = 5,
                            max_depth= 10, 
                            n_jobs=-1
                    ) 

    # Model Regressor X: Temperature Kelvin predict -> Y: R G B
    model_regressor_temp_rgb = TrainModelRegressor(model_regressor)
    model_regressor_temp_rgb.fit(X_train_new, Y_train_new)

    # Save model as pickle file 
    path = "./model/models"
    model_name="model_regressor_temp2rgb"

    with open(f"{path}/{model_name}", "wb") as model:
        pkl.dump(model_regressor_temp_rgb, model)

    # model_regressor_temp_rgb.save_model(path = "./model/models", model_name="model_regressor_temp_rgb")