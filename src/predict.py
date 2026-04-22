import pandas as pd

from src.config import MODEL_FILE, PREPROCESSOR_FILE
from src.utils import load_pickle
from src.features import extract_brand, create_car_age, create_km_per_year
from src.preprocessing import group_rare_fuel_types

REQUIRED_INPUT_COLUMNS = [
    "name",
    "year",
    "km_driven",
    "fuel",
    "seller_type",
    "transmission",
    "owner"
]
MODEL_INPUT_COLUMNS = [
    "brand",
    "car_age",
    "km_driven",
    "km_per_year",
    "fuel",
    "seller_type",
    "transmission",
    "owner"
]

def prepare_input_data(input_data: dict) -> pd.DataFrame:
    validate_input_data(input_data)
    df = pd.DataFrame([input_data])
    return df

def prepare_features_for_prediction(df: pd.DataFrame) -> pd.DataFrame:
    df = extract_brand(df)
    df = create_car_age(df)
    df = create_km_per_year(df)
    df = group_rare_fuel_types(df)

    df = df[MODEL_INPUT_COLUMNS]
    return df

def predict_price(input_data: dict) -> float:
    model = load_pickle(MODEL_FILE)
    preprocessor = load_pickle(PREPROCESSOR_FILE)

    df = prepare_input_data(input_data)
    df = prepare_features_for_prediction(df)

    X_processed = preprocessor.transform(df)
    prediction = model.predict(X_processed)

    return float(prediction[0])

def validate_input_data(input_data: dict) -> None:
    missing_columns = [col for col in REQUIRED_INPUT_COLUMNS if col not in input_data]

    if missing_columns:
        raise ValueError(
            f"Missing required input columns: {missing_columns}"
        )

if __name__ == "__main__":
    test_cars = [
        {
            "name": "Maruti Swift Dzire VDI",
            "year": 2014,
            "km_driven": 145500,
            "fuel": "Diesel",
            "seller_type": "Individual",
            "transmission": "Manual",
            "owner": "First Owner"
        },
        {
            "name": "Hyundai i20 Sportz",
            "year": 2019,
            "km_driven": 25000,
            "fuel": "Petrol",
            "seller_type": "Dealer",
            "transmission": "Manual",
            "owner": "First Owner"
        }
    ]

    for car in test_cars:
        predicted_price = predict_price(car)
        print(f"{car['name']} -> {predicted_price:.2f}")