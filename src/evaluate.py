from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_regression(y_true, y_pred):
    """
    Calcula las métricas principales de un problema de regresión.
    {y_true} es el valor real de y, {y_pred} es el valor de la predicción.
    
    """

    mae = mean_absolute_error(y_true,y_pred)
    rmse = np.sqrt(mean_squared_error(y_true,y_pred))
    r2 = r2_score(y_true,y_pred)

    return {

        "MAE" : mae,
        "RMSE" : rmse,
        "R2" : r2

    }