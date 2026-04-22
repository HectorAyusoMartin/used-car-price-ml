import pandas as pd

from src.config import MODEL_FILE, PREPROCESSOR_FILE
from src.utils import load_pickle
from src.features import extract_brand, create_car_age, create_km_per_year
from src.preprocessing import group_rare_fuel_types


def prepare_input_data(input_data: dict) -> pd.DataFrame:
    """
    Convierte un diccionario con los datos de un coche en un DataFrame
    de una sola fila.
    """
    df = pd.DataFrame([input_data])
    return df


def prepare_features_for_prediction(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica la misma ingeniería y preparación de variables usada en entrenamiento,
    pero sin incluir la variable objetivo.
    """
    df = extract_brand(df)
    df = create_car_age(df)
    df = create_km_per_year(df)
    df = group_rare_fuel_types(df)

    selected_columns = [
        "brand",
        "car_age",
        "km_driven",
        "km_per_year",
        "fuel",
        "seller_type",
        "transmission",
        "owner"
    ]

    df = df[selected_columns]
    return df


def predict_price(input_data: dict) -> float:
    """
    Carga el modelo y el preprocesador entrenados, prepara los datos
    de entrada y devuelve el precio predicho.
    """
    model = load_pickle(MODEL_FILE)
    preprocessor = load_pickle(PREPROCESSOR_FILE)

    df = prepare_input_data(input_data)
    df = prepare_features_for_prediction(df)

    X_prepared = preprocessor.transform(df)
    prediction = model.predict(X_prepared)

    return float(prediction[0])


if __name__ == "__main__":
    sample_car = {
        "name": "Maruti Swift Dzire VDI",
        "year": 2026,
        "km_driven": 1455,
        "fuel": "Diesel",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First Owner"
    }

    predicted_price = predict_price(sample_car)
    print(f"Predicted selling price: {predicted_price:.2f}")